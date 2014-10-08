class Instruction:

    def __init__(self, text):
        self._text = text

    def text(self):
    	return self._text

    def execute(self, console):
        console.save(self)

class InstructionIO(Instruction):

    def __init__(self, text):
        super(text)

    def isIO(self):
        return True

class InstructionCPU(Instruction):

    def __init__(self, text):
        super(text)

    def isIO(self):
        return False

