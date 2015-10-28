from mesoslxc.ec.argument import Argument


class RecoverArgument(Argument):
    def do(self):
        self.log.info("Action recover is not supported")
        return
