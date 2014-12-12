import unittest

from model.Instruction import *
from process.Program import Program


class TestProgram(unittest.TestCase):

    #Arrange
    def setUp(self):
        self.program = Program([], "Word")

    def test_whenIHaveAProgramWithoutInstructionsAndIAddOne_thenIHaveAProgramWithOneInstruction(self):
        inst1 = Instruction("Ejecutando Instruccion 1...")
        self.program.add_instruction(inst1)
        self.assertEqual(len(self.program.get_instructions()), 1)

    def test_whenIHaveAProgramWithInstructionsAndIAddOne_thenIHaveAProgramWithOneMoreInstruction(self):
        inst1 = Instruction("Ejecutando Instruccion 1...")
        self.program.add_instruction(inst1)
        self.previous_size = len(self.program.get_instructions())
        inst2 = Instruction("Ejecutando Instruccion 2...")
        self.program.add_instruction(inst2)
        self.assertEqual(self.previous_size + 1, len(self.program.get_instructions()))

suite = unittest.TestLoader().loadTestsFromTestCase(TestProgram)
unittest.TextTestRunner(verbosity=2).run(suite)
