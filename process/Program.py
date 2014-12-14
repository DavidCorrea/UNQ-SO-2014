from main.CustomLogger import Logger

class Program:

    def __init__(self, instructions, name):
        Logger.ok("Program " + name + " created.")
        self._instructions = instructions
        self._name = name

    def get_instructions(self):
        return self._instructions

    def name(self):
        return self._name

    def add_instruction(self, instruction):
        self._instructions.append(instruction)

    def amount_of_instructions(self):
        return len(self._instructions)