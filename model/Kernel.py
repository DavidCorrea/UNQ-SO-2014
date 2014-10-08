from model.Console import *
from model.MemoryManager import MemoryManager
from model.Memory import Memory
from model.HDD import HDD
from model.pcbCreator import PCBCreator
from Scheduler import Scheduler
from InterruptionHandler import Handler
from IOQueue import IOQueue
from threading import Semaphore
from CPU import CPU

class Kernel:

    #Se debería agregar el Scheduler (First In First Out, Priority, Round Robbin)
    def __init__(self, policyFor):
        self._console = Console()
        self._hdd = HDD()
        self._memoryManager = MemoryManager(Memory())
        self._creatorPCB = PCBCreator()
        self._scheduler = Scheduler()
        policyFor(self._scheduler)
        self._ioQueue = IOQueue()
        self._handler = Handler(self._scheduler, self._memoryManager, self._ioQueue)
        self._lock = Semaphore(0)
        self._cpu = CPU(self)

    def run(self, program):
        program = self._hdd.getProgram(program.getName())
        begin = self._memoryManager.write(program) #Se asigna el número de la primera Instrucción.
        pcb = self._creatorPCB.createPCB( begin, len(program.getInstructions()))
        self.addToScheduler(pcb)

    def addToScheduler(self, pcb):
        #pcb.changeStatus(PCBStatus.ready) #Va a haber validaciones para esto.
        self._scheduler.add(pcb)


    def handleThis(self, interruption):
        self._handler.handle(interruption)
        self._lock.release()

    def get_memory_manager(self):
        return self._memoryManager

    def get_scheduler(self):
        return self._scheduler

    def get_ioQueue(self):
        return self._ioQueue

    def get_lock(self):
        return self._lock