from threading import Semaphore

from memory.MemoryManager import MemoryManager
from model.Console import *
from process.pcbCreator import PCBCreator
from InterruptionHandler import Handler
from IOQueue import IOQueue
from CPU import CPU
from scheduling.LongTermScheduler import LTScheduler
from scheduling.Scheduler import Scheduler


class Kernel:

    def __init__(self, policy_scheduler, hdd, policy_memory):
        self._console = Console()
        self._hdd = hdd
        self._fileSystem = self._hdd.generate_file_system()
        self._memoryManager = MemoryManager(self)
        self._creatorPCB = PCBCreator()
        self._scheduler = Scheduler()
        policy_scheduler(self._scheduler)
        policy_memory(self._memoryManager)
        self._long_term_scheduler = LTScheduler(self._scheduler, self._memoryManager)
        self._ioQueue = IOQueue(self._memoryManager, self._scheduler)
        self._handler = Handler(self._scheduler, self._memoryManager, self._ioQueue)
        self._lock = Semaphore(0)
        self._cpu = CPU(self)
        self._ioQueue.start()

    def run(self, program_name):
        program = self._fileSystem.get_program(program_name)
        pcb = self._creatorPCB.create_pcb(len(program.getInstructions()), program)
        self._long_term_scheduler.init_process(pcb)


    def handle_this(self, interruption):
        self._handler.handle(interruption)
        self._lock.release()

    def get_memory_manager(self):
        return self._memoryManager

    def get_scheduler(self):
        return self._scheduler

    def get_io_queue(self):
        return self._ioQueue

    def get_lock(self):
        return self._lock
