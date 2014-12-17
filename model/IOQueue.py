from threading import *
from main.CustomLogger import Logger


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
        Logger.ok("Returning to Ready Q")
        item_to_remove = self._waiting[0]
        self._waiting.remove(item_to_remove)
        self._scheduler.add(item_to_remove)

    def run(self):
        while True:
            self._lock.acquire()
            current_process = self._waiting[0]
            while self._memory_manager.read(current_process.get_pc()).isIO():
                if current_process.has_finished():
                    current_process.increment()
                    break
                Logger.info("Managing IO Instruction")
                current_process.increment()
            Logger.warning("Dispatching PCB!")
            self.dispatch()
