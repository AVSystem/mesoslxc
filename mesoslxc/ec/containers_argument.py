import subprocess

from mesoslxc.ec.argument import Argument
from mesoslxc.ec.communication_utils import ComminicationUtils
from mesoslxc.interface import containerizer_pb2


class ContainersArgument(Argument):
    def do(self):
        containersCommand = ['lxc-ls', '--active', '-1']
        containersMessage = containerizer_pb2.Containers()
        self.log.debug(containersCommand)
        output = subprocess.check_output(containersCommand)
        self.log.debug("Running containers: %s" % output)
        for line in output.splitlines():
            if len(line) > 0:
                container = containersMessage.containers.add()
                container.value = line
        ComminicationUtils.send(containersMessage.SerializeToString())
