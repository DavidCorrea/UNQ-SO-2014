from threading import Thread


class Clock(Thread):

    def __init__(self, cpu, lock):
        Thread.__init__(self)
        self._cpu = cpu
        self._lock = lock

    def run(self):
        while True:
            self._cpu.run_tick()
            self._lock.acquire()