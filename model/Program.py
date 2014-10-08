import unittest

from model.Instruction import *


class Program:

    def __init__(self, instructions, name):       
        self._instructions = instructions
        self._name = name

    def getInstructions(self):
        return self._instructions

    def name(self):
        return self._name

    def addInstruction(self, instruction):
        self._instructions.append(instruction)

class TestProgram(unittest.TestCase):

    #Arrange
    def setUp(self):
        self.program = Program([], "Word")

    def test_whenIHaveAProgramWithoutInstructionsAndIAddOne_thenIHaveAProgramWithOneInstruction(self):
        inst1 = Instruction("Ejecutando Instruccion 1...")
        self.program.addInstruction(inst1)
        self.assertEqual(len(self.program.getInstructions()), 1)
        
    def test_whenIHaveAProgramWithInstructionsAndIAddOne_thenIHaveAProgramWithOneMoreInstruction(self):
        inst1 = Instruction("Ejecutando Instruccion 1...")
        self.program.addInstruction(inst1)
        previousSize = len(self.program.getInstructions())
        inst2 = Instruction("Ejecutando Instruccion 2...")
        self.program.addInstruction(inst2)
        self.assertEqual(previousSize + 1 , len(self.program.getInstructions()))
        
suite = unittest.TestLoader().loadTestsFromTestCase(TestProgram)
unittest.TextTestRunner(verbosity=2).run(suite)
