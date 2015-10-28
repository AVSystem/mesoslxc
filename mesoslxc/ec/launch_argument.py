import os
import subprocess

import daemon
from configobj import ConfigObj
from lockfile.pidlockfile import PIDLockFile
from mesoslxc.ec.argument import Argument
from mesoslxc.ec.communication_utils import ComminicationUtils
from mesoslxc.interface import containerizer_pb2


class LaunchArgument(Argument):
    def do(self):
        launchMessage = containerizer_pb2.Launch()
        launchMessage.ParseFromString(ComminicationUtils.receive(self.log))
        containerId = launchMessage.container_id.value
        self.log.debug(
            "Launching container with ID: %s (Task ID: %s)" % (containerId, launchMessage.task_info.task_id.value))
        if launchMessage.task_info.container.docker.image == '':
            self.log.error("You need to specify image")
            return
        self.log.debug("lxc-clone")
        cloneCommand = ['lxc-clone', '-s', launchMessage.task_info.container.docker.image, containerId]
        self.log.debug(cloneCommand)
        subprocess.check_call(cloneCommand)
        self.log.debug("Preparing LXC config")
        self.prepareLxcConfig(launchMessage)
        self.log.debug("lxc-start")
        startCommand = ['lxc-start', '-d', '-n', containerId, '--logfile', '/dev/stderr']
        self.log.debug(startCommand)
        subprocess.check_call(startCommand)
        self.log.debug("lxc-wait")
        waitCommand = ['lxc-wait', '-n', containerId, '--state', 'RUNNING']
        self.log.debug(waitCommand)
        subprocess.check_call(waitCommand)
        self.log.debug("lxc-attach")
        self.log.debug(os.environ)
        if not os.path.exists(self.config['tmp_path']):
            os.mkdir(self.config['tmp_path'])
        context = daemon.DaemonContext(pidfile=PIDLockFile(self.config['tmp_path'] + containerId + ".pid"))

        with context:
            self.launchExecutor(containerId, self.config['executor'], launchMessage.directory)
        return

    @staticmethod
    def launchExecutor(containerId, executor, directory):
        with open("%s/stdout" % directory, "a") as stdoutFile, open("%s/stderr" % directory, "a") as stderrFile:
            attachCommand = ['lxc-attach', '--keep-env', '-n', containerId, '--', executor]
            subprocess.check_call(attachCommand, env=os.environ.copy(), stdout=stdoutFile, stderr=stderrFile)
        return

    def prepareLxcConfig(self, launchMessage):
        lxcConfig = ConfigObj("/var/lib/lxc/%s/config" % launchMessage.container_id.value)

        for parameter in launchMessage.task_info.container.docker.parameters:
            lxcConfig[parameter.key] = parameter.value

        for resource in launchMessage.task_info.resources:
            self.log.debug(resource)
            if resource.name == "cpus":
                lxcConfig['lxc.cgroup.cpu.shares'] = int(resource.scalar.value * 1024)
            if resource.name == "mem":
                lxcConfig['lxc.cgroup.memory.limit_in_bytes'] = "%dM" % int(resource.scalar.value)
        lxcConfig.write()
        return
