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

