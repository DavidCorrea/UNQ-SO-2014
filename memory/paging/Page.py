__author__ = 'David'

class Page:

    def __init__(self, index, starting_index, ending_index, amount_of_instructions):
        self._index = index
        self._amount_of_instructions = amount_of_instructions
        self._starting_index = starting_index
        self._ending_index = ending_index
        self._used = False
        self._assigned = False

    def set_used(self):
        self._used = True

    def has_been_used(self):
        return self._used

    def set_assign(self):
        self._assigned = True

    def set_unassigned(self):
        self._assigned = False

    def get_starting_index(self):
        return self._starting_index

    def get_ending_index(self):
        return self._ending_index

    def get_amount_of_instructions(self):
        return self._amount_of_instructions