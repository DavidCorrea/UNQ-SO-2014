from Console import *
from Program import *
from PCB import *
from MemoryManager import *
from Memory import *
from HDD import *

class Kernel:

    #Se debería agregar el Scheduler (First In First Out, Priority, Round Robbin)
    def __init__(self, scheduler):
        self._console = Console()
        self._hdd = HDD()
        self._memoryManager = MemoryManager(Memory())
        self._nextPCBIndex = 1
        self._scheduler = scheduler

    def run(self, program):
        program = self._hdd.getProgram(program.getName())
        begin = self._memoryManager.write(program) #Se asigna el número de la primera Instrucción.
        pcb = PCB(self._nextPCBIndex, begin, len(program.getInstructions()))
        self.addToScheduler(pcb)

    def addToScheduler(self, pcb):
        self._nextPCBIndex += 1
        pcb.changeStatus(PCBStatus.ready) #Va a haber validaciones para esto.
        self._scheduler.add(pcb)
             
class TestKernel(unittest.TestCase):

    #Arrange
    def setUp(self):
        self.kernelUT = Kernel(Console(), None, None)
        listInst = [Instruction("Number one"), Instruction("Number two")]
        self.program = Program(listInst, "Word")

    def test_whenILoadAProgramAndIrunIt_thenIgetTwoInstructions(self):
        self.assertEquals(2, len(self.kernelUT.run(self.program)))

    def test_whenILoadAProgram_ThenIgetOutputInOrder(self):
        instruction = self.kernelUT.run(self.program)
        self.assertEquals("Number one", instruction[0])
        self.assertEquals("Number two", instruction[1])

suite = unittest.TestLoader().loadTestsFromTestCase(TestKernel)
unittest.TextTestRunner(verbosity=2).run(suite)

