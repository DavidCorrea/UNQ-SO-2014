from PCBInfoHolder import *


class PCB:

    def __init__(self, _id, amount_instructions, m_policy):
        self._id = _id
        self._amountInstructions = amount_instructions
        self._priority = None
        self._info_holder = m_policy

    def get_info_holder(self):
        return self._info_holder

    def __str__(self):
        return 'ID: ' + self._id

    def increment(self):
        self._info_holder.increment()

    def get_pc(self):
        return self._info_holder.current_mem_dir()

    def get_instructions(self):
        return self._info_holder.instructions()

    def get_amount_of_instructions(self):
        return self._amountInstructions

    def has_finished(self):
        return self._info_holder.has_finished()

    def needs_reload(self):
        return self._info_holder.needs_reload()

    def set_priority(self, priority):
        self._priority = priority

    def increase_priority(self):
        if self._priority == 3:
            self._priority = PCBPriorities().getPriorities().MEDIUM
        elif self._priority == 2:
            self._priority = PCBPriorities().getPriorities().HIGH

class PCBPriorities:

    def __init__(self):
        self._priorities = self.enum(HIGH=1, MEDIUM=2, LOW=3)

    def getPriorities(self):
        return self._priorities

    def enum(self, **enums):
        return type('Enum', (), enums)