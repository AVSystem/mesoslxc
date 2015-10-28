import os
import subprocess
import threading
import time
import sys

from mesos.interface import Executor

from mesoslxc.interface import mesos_pb2


class MesosLXCExecutor(Executor):
    def __init__(self, log):
        self.process = None
        self.log = log

    def registered(self, driver, executorInfo, frameworkInfo, slaveInfo):
        self.log.debug("ex registered")
        return

    def reregistered(self, driver, slaveInfo):
        self.log.debug("ex reregistered")
        return

    def disconnected(self, driver):
        self.log.debug("ex disconnected")
        return

    def killTask(self, driver, taskId):
        self.log.debug("Killing task")
        self.kill_sub_process()
        return

    def kill_sub_process(self):
        if self.process is None:
            return

        self.process.terminate()
        time.sleep(1)
        if self.is_process_exists(self.process):
            time.sleep(5)
            self.sig_kill(self.process)
        else:
            return

    @staticmethod
    def sig_kill(process):
        try:
            process.kill()
        except:
            pass

    @staticmethod
    def is_process_exists(process):
        try:
            os.kill(process.pid, 0)
            return True
        except OSError:
            return False

    def frameworkMessage(self, driver, message):
        self.log.debug("Framework message")
        self.log.debug(message)
        return

    def shutdown(self, driver):
        self.log.debug("Shutdown")
        self.kill_sub_process()
        return

    def error(self, error, message):
        self.log.debug("Error")
        return

    def launchTask(self, driver, task):
        def run_task():

            self.log.info('Launching task with ID:  %s' % task.task_id.value)

            status = mesos_pb2.TaskStatus()
            status.task_id.value = task.task_id.value
            status.state = mesos_pb2.TASK_STARTING
            self.log.debug("Sending status STARTING")
            driver.sendStatusUpdate(status)

            self.log.debug("Running task: %s" % task.command.value)
            self.process = subprocess.Popen(task.command.value.split(" "), stdout=sys.stdout, stderr=sys.stderr)
            status.state = mesos_pb2.TASK_RUNNING
            driver.sendStatusUpdate(status)
            exitCode = self.process.wait()
            self.log.debug("Exit code %d" % exitCode)

            if exitCode == 0:
                status.state = mesos_pb2.TASK_FINISHED
                self.log.debug("Sending status FINISHED")
            elif (exitCode == -15) or (exitCode == -9):
                status.state = mesos_pb2.TASK_KILLED
                self.log.debug("Sending status KILLED")
            else:
                status.state = mesos_pb2.TASK_FAILED
                self.log.debug("Sending status FAILED")

            driver.sendStatusUpdate(status)
            driver.stop()
            return

        thread = threading.Thread(target=run_task)
        thread.start()
