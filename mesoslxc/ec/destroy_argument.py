import subprocess

from mesoslxc.ec.argument import Argument
from mesoslxc.ec.communication_utils import ComminicationUtils
from mesoslxc.interface import containerizer_pb2


class DestroyArgument(Argument):
    def do(self):
        destroyMessage = containerizer_pb2.Destroy()
        destroyMessage.ParseFromString(ComminicationUtils.receive(self.log))
        self.destroy_container(destroyMessage.container_id.value)

    @staticmethod
    def destroy_container(containerId):
        destroyCommand = ['lxc-destroy', '-f', '-n', containerId]
        try:
            subprocess.check_call(destroyCommand)
        except subprocess.CalledProcessError:
            pass
