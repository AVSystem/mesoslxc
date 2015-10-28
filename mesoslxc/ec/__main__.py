#!/usr/bin/env python

import sys
import logging
import traceback

from configobj import ConfigObj
from mesoslxc.ec.argument_dispatcher import ArgumentDispatcher


def main(argv=None):
    log = logging.getLogger('ec')
    try:
        config = ConfigObj('/etc/mesos/mesoslxc.cfg')
        argument = argv[1] if len(argv) > 1 else ""
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s (%(process)d - ' + argument + ') - %(levelname)s - %(message)s')
        log.setLevel(logging.DEBUG)
        sh = logging.StreamHandler(sys.__stderr__)
        sh.setFormatter(formatter)
        sh.setLevel(logging.DEBUG)
        log.addHandler(sh)
        fh = logging.FileHandler("%smesoslxc-ec.log" % config['log_path'])
        fh.setFormatter(formatter)
        fh.setLevel(logging.DEBUG)
        log.addHandler(fh)

        log.debug("Starting with argument: %s" % argument)

        action = ArgumentDispatcher(argument, log, config)
        action.do()

        return 0
    except Exception:
        log.error(traceback.format_exc())
        log.error(traceback.format_stack())
        return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
