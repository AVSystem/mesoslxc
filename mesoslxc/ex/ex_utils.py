import os
import socket
import time
import sys


class EXUtils(object):
    def __init__(self, log):
        self.log = log

    def check_needed_envs(self):
        required_envs = ['LIBPROCESS_IP', 'LIBPROCESS_PORT', 'MESOS_SLAVE_ID', 'MESOS_SLAVE_PID',
                         'MESOS_NATIVE_LIBRARY',
                         'MESOS_CHECKPOINT', 'MESOS_WORK_DIRECTORY', 'MESOS_EXECUTOR_ID', 'MESOS_DIRECTORY',
                         'MESOS_FRAMEWORK_ID', 'MESOS_RECOVERY_TIMEOUT', 'MESOS_LIBEXEC_DIRECTORY']

        for required_env in required_envs:
            if required_env not in os.environ:
                self.log.debug("Missing ENV: %s You need to pass required ENVs: %s" % (required_env, required_envs))
                sys.exit(1)

    def wait_for_network_connectivity(self):
        while True:
            s = socket.socket()
            try:
                s.connect((os.environ['LIBPROCESS_IP'], int(os.environ['LIBPROCESS_PORT'])))
                s.close()
                self.log.debug("Connectivity to Mesos-slave: OK")
                break
            except socket.error:
                time.sleep(1)
                self.log.debug("Connectivity to Mesos-slave: FAILED (retrying in 1s)")
                s.close()
                continue
