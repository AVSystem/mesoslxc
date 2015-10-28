import time

from mesoslxc.ec.argument import Argument
from mesoslxc.ec.communication_utils import ComminicationUtils
from mesoslxc.interface import mesos_pb2, containerizer_pb2


class UsageArgument(Argument):
    def do(self):
        usageMessage = containerizer_pb2.Usage()
        usageMessage.ParseFromString(ComminicationUtils.receive(self.log))
        containerId = usageMessage.container_id.value

        resourceStatisticsMessage = mesos_pb2.ResourceStatistics()
        resourceStatisticsMessage.timestamp = time.time()

        ComminicationUtils.send(resourceStatisticsMessage.SerializeToString())
        return
