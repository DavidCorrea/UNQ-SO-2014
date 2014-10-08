import PCB

class PCBCreator :

    def __init__(self):
        self._currentID = 0

    def createPCB(self, firstMemoryDir, amountInstructions):
        PCB(self._currentID, firstMemoryDir, amountInstructions)