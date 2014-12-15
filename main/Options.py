__author__ = 'David'


class Options:

    def __init__(self):
        self._scheduler_options = { 1 : "FIFO", 2 : "PRIORITY", 3 : "ROUNDROBIN"}
        self._memory_options = { 1 : "CA", 2 : "PAGING"}
        self._continuous_assignment_options = { 1 : "BESTFIT", 2 : "WORSTFIT", 3 : "FIRSTFIT"}

    def eval_scheduler_option(self, option, quantum=None):
        if self._scheduler_options[option] == "FIFO":
            return lambda k: k.get_scheduler().set_as_fifo()
        elif self._scheduler_options[option] == "PRIORITY":
            return lambda k: k.get_scheduler().set_as_pq()
        else:
            return lambda k: k.get_scheduler().set_as_rr(quantum)

    def eval_memory_option(self, option, page_size=None):
        if self._memory_options[option] == "CA":
            return lambda k: k.get_memory_manager().set_as_ca()
        else:
            return lambda k: k.get_memory_manager().set_as_paging(page_size)

    def eval_continuous_assignment_option(self, option):
        if self._continuous_assignment_options[option] == "BESTFIT":
            return lambda k: k.get_memory_manager().get_policy().set_as_best_fit()
        elif self._continuous_assignment_options[option] =="WORSTFIT":
            return lambda k: k.get_memory_manager().get_policy().set_as_worst_fit()
        else:
            return lambda k: k.get_memory_manager().get_policy().set_as_first_fit()

    def get_scheduler_options(self):
        return self._scheduler_options

    def get_memory_options(self):
        return self._memory_options

    def get_continuous_assignment_options(self):
        return self._continuous_assignment_options