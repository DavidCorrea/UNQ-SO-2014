__author__ = 'David'


class PageHolder:

    def __init__(self, program):
        self._pc = 0
        self._pages = []
        self._current = 0
        self._policy_result = None
        self._program = program

    def increment(self):
        self._pc += 1

    def has_finished(self):
        return self._pages[len(self._pages)-1].has_been_used()

    def needs_reload(self):
        if self._current is len(self._pages)-1:
            self._pages[self._current].set_used()
        answer = self._pages[self._current].has_been_read(self._pc)
        if answer:
            self._pages[self._current].set_used()
            self._current += 1
        return answer

    def instructions(self):
        blocks = self._program.fetch_blocks()
        return blocks[self._current].get_data()

    def current_mem_dir(self):
        return self._pages[self._current].get_real_instruction_number(self._pc)

    def set_hold(self, hold):
        self._pages = hold

    def get_hold(self):
        return self._pages

    def is_holding(self):
        return self._pages


class BlockHolder:

    def __init__(self, program):
        self._dirs = None
        self._pc = 0
        self._program = program

    def increment(self):
        self._pc += 1

    def has_finished(self):
        return (self._dirs[1] - self.current_mem_dir()) <= 0

    def needs_reload(self):
        return False

    def instructions(self):
        blocks = map(lambda b: b.get_data(), self._program.fetch_blocks())
        return [item for sublist in blocks for item in sublist]

    def current_mem_dir(self):
        return self._dirs[0] + self._pc

    def get_hold(self):
        return self._dirs

    def is_holding(self):
        return self._dirs is not None

    def set_hold(self, hold):
        self._dirs = hold