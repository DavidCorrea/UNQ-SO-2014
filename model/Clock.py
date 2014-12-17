from threading import Thread
import time


class Clock(Thread):

    def __init__(self, cpu, lock):
        Thread.__init__(self)
        self._cpu = cpu
        self._lock = lock

    def run(self):
        self._cpu.receive_pcb()
        while True:
            time.sleep(0.2)
            self._cpu.run_tick()
            self._lock.acquire()
