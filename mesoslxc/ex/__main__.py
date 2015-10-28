import sys
import os
import logging
import traceback

from mesos.interface import mesos_pb2

from mesos.native import MesosExecutorDriver
from mesoslxc.ex.ex_utils import EXUtils
from mesoslxc.ex.mesos_lxc_executor import MesosLXCExecutor

log = logging.getLogger('ex')
log.setLevel(logging.DEBUG)
fh = logging.StreamHandler(sys.__stderr__)
formatter = logging.Formatter('%(asctime)s - %(name)s (%(process)d) - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
log.addHandler(fh)


def main():
    try:
        ex_utils = EXUtils(log)
        ex_utils.check_needed_envs()
        ex_utils.wait_for_network_connectivity()

        os.environ['LIBPROCESS_PORT'] = "0"
        os.environ['LIBPROCESS_IP'] = "0.0.0.0"

        driver = MesosExecutorDriver(MesosLXCExecutor(log))

        log.debug('Running driver')
        return 0 if driver.run() == mesos_pb2.DRIVER_STOPPED else 1
    except Exception, e:
        log.error(traceback.format_exc())
        log.error(traceback.format_stack())
        return 1


if __name__ == "__main__":
    sys.exit(main())
