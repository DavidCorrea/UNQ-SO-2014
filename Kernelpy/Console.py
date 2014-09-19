class Console:

    def __init__(self):
        self._prints = []

    def save(self, instruction):
        self._prints.append(instruction.text())

    def printStrings(self):
        return self._prints
                