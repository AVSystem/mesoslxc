from mesoslxc.ec.containers_argument import ContainersArgument
from mesoslxc.ec.destroy_argument import DestroyArgument
from mesoslxc.ec.help_argument import HelpArgument
from mesoslxc.ec.launch_argument import LaunchArgument
from mesoslxc.ec.recover_argument import RecoverArgument
from mesoslxc.ec.update_argument import UpdateArgument
from mesoslxc.ec.usage_argument import UsageArgument
from mesoslxc.ec.wait_argument import WaitArgument


class ArgumentDispatcher(object):
    def __init__(self, argument, log, config):

        if argument == "launch":
            self.argument_object = LaunchArgument(log, config)
        elif argument == "recover":
            self.argument_object = RecoverArgument(log, config)
        elif argument == "containers":
            self.argument_object = ContainersArgument(log, config)
        elif argument == "wait":
            self.argument_object = WaitArgument(log, config)
        elif argument == "update":
            self.argument_object = UpdateArgument(log, config)
        elif argument == "usage":
            self.argument_object = UsageArgument(log, config)
        elif argument == "destroy":
            self.argument_object = DestroyArgument(log, config)
        else:
            self.argument_object = HelpArgument(log, config)

    def do(self):
        self.argument_object.do()
