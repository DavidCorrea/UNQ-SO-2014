import unittest
from model.Program import *
from model.HDD import *


class TestHDD(unittest.TestCase):

	#Arrange
    def setUp(self):
    	self.program1 = Program([], "Word")
        self.hdd = HDD()

	def test_whenISearchForWordAndItsIn_thenIGetIt(self):
		self.hdd.addProgram(self.program1)
		self.assertEquals(self.program1, self.hdd.getProgram("Word"))

    def test_whenISearchForWordAndItsNotIn_thenIGetAnException(self):
        self.assertRaises(IndexError, self.hdd.getProgram("Word"))


suite = unittest.TestLoader().loadTestsFromTestCase(TestHDD)
unittest.TextTestRunner(verbosity=2).run(suite)