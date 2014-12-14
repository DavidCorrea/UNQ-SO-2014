from threading import *


class IOQueue(Thread):

    def __init__(self, memoryManager, scheduler):
        Thread.__init__(self)
        self._waiting = []
        self._lock = Semaphore(0)
        self._memory_manager = memoryManager
        self._scheduler = scheduler

    def addToWaiting(self, process):
        self._waiting.append(process)
        self._lock.release()

    def dispatch(self):
        self._scheduler.add(self._waiting[0])
        self._waiting.remove(0)

    def run(self):
        while True:
            self._lock.acquire()
            current_process = self._waiting[0]
            while self._memory_manager.read(current_process.get_pc).isIO():
                current_process.increment()
            self.dispatch()
