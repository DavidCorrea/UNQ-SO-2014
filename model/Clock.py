from threading import Thread


class Clock(Thread):

    def __init__(self, cpu, lock, lock_programs):
        Thread.__init__(self)
        self._cpu = cpu
        self._lock = lock
        self.lock_programs = lock_programs

    def run(self):

        while True:
            self.lock_programs.acquire()
            self._cpu.run_tick()
            self._lock.acquire()
