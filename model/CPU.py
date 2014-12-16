from Interruptions import *
from Clock import Clock
from main.CustomLogger import Logger


class CPU():

    def __init__(self, kernel):
        self._kernel = kernel
        self._current_pcb = None
        self._quantum = kernel.get_scheduler().get_quantum()
        self._memory_manager = kernel.get_memory_manager()
        self._currentInstruction = None
        self._scheduler = kernel.get_scheduler()
        self._builderRQ = BuilderInterruption(self._kernel.get_io_queue(), self._memory_manager, self._scheduler)
        self._lock = self._kernel.get_lock()
        Clock(self, self._lock).start()

    def receive_pcb(self):
        self._current_pcb = self._scheduler.next()

    def fetch(self):
        Logger.info("Fetching next instruction...")
        if self._current_pcb.needs_reload():
            self._memory_manager.write(self._current_pcb)
        self._currentInstruction = self._memory_manager.read(self._current_pcb.get_pc())
        self._current_pcb.increment()

    def reset_quantum(self):
        self._quantum = self._kernel.get_scheduler().get_quantum()

    def run_tick(self):
        if self._current_pcb.has_finished():
            self._kernel.handle_this(self._builderRQ.buildKillRQ(self._current_pcb))
            Logger.warning("Kill RQ.")
            self.receive_pcb()
        elif self._quantum == 0:
            self.reset_quantum()
            self._kernel.handle_this(self._builderRQ.buildTimeoutRQ(self._current_pcb))
            Logger.warning("Timeout RQ.")
            self.receive_pcb()
        elif self._currentInstruction.isIO():
            self._kernel.handle_this(self._builderRQ.buildIORQ(self._current_pcb))
            Logger.warning("IO RQ.")
            self.receive_pcb()
        else:
            self.fetch()
            self._lock.release()
            self._quantum -= 1
