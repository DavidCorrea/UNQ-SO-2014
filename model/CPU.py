from Interruptions import *
from Clock import Clock

class CPU():

    def __init__(self, kernel):
        self._kernel = kernel
        self._current_pcb = None
        self._quantum = kernel.get_scheduler().get_quantum()
        self._memory_manager = kernel.get_memory_manager()
        self._currentInstruction = None
        self._scheduler = kernel.get_scheduler()
        self._builderRQ = BuilderInterruption(self._kernel.get_ioQueue(),self._memory_manager,self._scheduler )
        Clock(self, self._kernel.get_lock() ).run()

    def receive_pcb(self):
        self._current_pcb = self._scheduler.next()

    def fetch(self):
        self._currentInstruction = self._memory_manager.read(self._current_pcb.pc)
        self._current_pcb.increment()

    def reset_quantum(self):
        self._quantum = self._kernel.get_scheduler().get_quantum()

    def runTick(self):
        if self._current_pcb.pc.hasFinished():
            self._kernel.handleThis(self._builderRQ.buildKillRQ(self._current_pcb))
            self.receive_pcb()
        elif self._quantum == 0:
            self.reset_quantum()
            self._kernel.handleThis(self._builderRQ.buildTimeoutRQ(self._current_pcb))
            self.receive_pcb()
        elif self._currentInstruction.isIO():
            self._kernel.handleThis(self._builderRQ.buildIORQ(self._current_pcb))
            self.receive_pcb()
        else:
            self.fetch()
            self._quantum -= 1
