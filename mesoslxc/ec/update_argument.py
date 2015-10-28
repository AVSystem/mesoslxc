from mesoslxc.ec.argument import Argument
from mesoslxc.ec.communication_utils import ComminicationUtils
from mesoslxc.interface import containerizer_pb2


class UpdateArgument(Argument):
    def do(self):
        self.log.info("Action update is not supported")
        updateMessage = containerizer_pb2.Update()
        updateMessage.ParseFromString(ComminicationUtils.receive(self.log))
        self.log.debug(updateMessage)
        return
