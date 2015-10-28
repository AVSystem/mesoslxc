import os
import time
import errno

from lockfile.pidlockfile import PIDLockFile
from mesoslxc.ec.argument import Argument
from mesoslxc.ec.communication_utils import ComminicationUtils
from mesoslxc.ec.destroy_argument import DestroyArgument
from mesoslxc.interface import containerizer_pb2


class WaitArgument(Argument):
    def do(self):
        waitMessage = containerizer_pb2.Wait()
        waitMessage.ParseFromString(ComminicationUtils.receive(self.log))
        containerId = waitMessage.container_id.value
        self.log.debug("Waiting for EOL of container with ID: %s" % containerId)
        pidFilePath = "%s%s.pid" % (self.config['tmp_path'], containerId)
        self.log.debug("EX PID file: %s" % pidFilePath)
        self.waitPID(int(PIDLockFile(pidFilePath).read_pid()))
        DestroyArgument.destroy_container(containerId)
        terminationMessage = containerizer_pb2.Termination()
        terminationMessage.killed = False
        terminationMessage.message = ""
        terminationMessage.status = 0
        ComminicationUtils.send(terminationMessage.SerializeToString())

    @staticmethod
    def waitPID(pid):
        try:
            while True:
                os.kill(pid, 0)
                time.sleep(1)
        except OSError as err:
            if err.errno == errno.ESRCH:
                return
