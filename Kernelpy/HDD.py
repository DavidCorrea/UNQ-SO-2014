
import unittest
from Program import *

class HDD:

	def __init__(self):
		self._programs = [] 

	def getProgram(self, programName):
		try:
			f = lambda x: not programName.equals(x.name())
			return filter(f,self._programs)[0]
		except IndexError:
			print "Implementar"

	def addProgram(self, program):
		self._programs.append(program)


class TestHDD(unittest.TestCase):

	#Arrange
    def setUp(self):
    	self.program1 = Program([], "Word")
        self.hdd = HDD()

	def test_whenISearchForWordAndItsIn_thenIGetIt(self):
		self.hdd.addProgram(self.program1)
		self.assertEquals(program1, self.hdd.getProgram("Word"))

    def test_whenISearchForWordAndItsNotIn_thenIGetAnException(self):
        self.assertRaises(IndexError, self.hdd.getProgram("Word"))


suite = unittest.TestLoader().loadTestsFromTestCase(TestHDD)
unittest.TextTestRunner(verbosity=2).run(suite)