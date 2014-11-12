
class PCB:

    def __init__(self, id, startM, amountInstructions):
        self._id = id
        self._startM = startM
        self._amountInstructions = amountInstructions
        self._pc = startM
        self._priority = None
        self._block = None
        #self._status = PCBStatus.new

    def set_block(self, block):
        self._block = block

    def get_block(self):
        return self._block

    def __str__(self):
        return 'ID: ' + self._id

    def increment(self):
        self._pc += 1

    def get_pc(self):
        return self._pc

    def set_priority(self, priority):
        self._priority = priority

    def has_finished(self):
        return self._pc == (self._startM + self._amountInstructions)

    def increase_priority(self):
        if self._priority == 3 :
            self._priority = PCBPriorities().getPriorities().MEDIUM
        elif self._priority == 2 :
            self._priority = PCBPriorities().getPriorities().HIGH

    def get_amount_of_instructions(self):
        return self._amountInstructions

'''
class PCBStatus(Enum):
    new = "New"
    ready = "Ready"
    busy = "Busy"
    waiting = "Waiting"
    running = "Running"
    complete = "Complete"
'''


class PCBPriorities:

    def __init__(self):
        self._priorities = self.enum(HIGH=1, MEDIUM=2, LOW=3)

    def getPriorities(self):
        return self._priorities

    def enum(self, **enums):
        return type('Enum', (), enums)