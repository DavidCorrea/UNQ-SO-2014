__author__ = 'robot'


class LTScheduler():

    def __init__(self, short_term_scheduler, memory_manager):
        self._waitingPrograms = []
        self._shortTermS = short_term_scheduler
        self._memory_manager = memory_manager

    def init_process(self, pcb):
        if self._memory_manager.can_serve(pcb):
            self._memory_manager.write(pcb)
            self._shortTermS.add(pcb)
        else:
            self._waitingPrograms.append(pcb)

    def init_pending_process(self, process_size):
       pcb = next(i for i in self._waitingPrograms if i.get_amount_of_instructions is process_size)
       begin = self._memory_manager.write(pcb)
       pcb.set_start_instruction(begin)
       self._shortTermS.add(pcb)

    def amount_programs_waiting(self):
        return len(self._waitingPrograms)
