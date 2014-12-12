from process import PCB


class PCBCreator :

    def __init__(self):
        self._currentID = 0

    def create_pcb(self, amount_instructions, program):
        pcb = PCB(self._currentID, amount_instructions, program)
        self._currentID += 1
        return pcb