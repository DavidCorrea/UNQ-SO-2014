from Queue import PriorityQueue


class Scheduler:

    def __init__(self):
        self._policy = None
        self._quantum = None

    def set_as_fifo(self):
        self._policy = FifoScheduler()
        self._quantum = -1

    def set_as_pq(self):
        self._policy = PriorityScheduler()
        self._quantum = -1

    #El quantum debe ser mayor a 0.
    def set_as_rr(self, quantum):
        self._policy = RoundRobinScheduler(quantum)
        self._quantum = quantum

    def get_quantum(self):
        return self._quantum

    def add(self, pcb):
        self._policy.add(pcb)

    def next(self):
        return self._policy.get_pcb()

    def set_policy(self, policy):
        self._policy = policy


class FifoScheduler():

    def __init__(self):
        self._readyq = []

    def add(self, pcb):
        self._readyq.append(pcb)

    def get_pcb(self):
        ret_pcb = self._readyq[0]
        self._readyq.remove(ret_pcb)
        return ret_pcb

    def set_scheduler(self, scheduler):
        scheduler.set_as_fifo()


class PriorityScheduler():

    def __init__(self):
        self._readyq = PriorityQueue()
        self._pcbsQ = []
        self._counter = 0

    def add(self, pcb):
        self._readyq.put((pcb._priority, self._counter, pcb))
        self._pcbsQ.append(pcb)
        self._counter += 1

    def get_pcb(self):
        #El [2] es porque el next() me devuelve la tupla que guarda la PQ, por lo que le pido el objeto.
        self.pcb_to_give = self._readyq.get()[2]
        self._pcbsQ.remove(self.pcb_to_give)
        for pcb in self._pcbsQ:
            pcb.increase_priority()
        return self.pcb_to_give

    def set_scheduler(self, scheduler):
        scheduler.set_as_pq()


class RoundRobinScheduler():

    def __init__(self, quantum):
        self._readyq = []
        self._quantum = quantum

    def add(self,pcb):
        self._readyq.append(pcb)

    def get_pcb(self):
        ret_pcb = self._readyq[0]
        self._readyq.remove(ret_pcb)
        return ret_pcb

    def set_scheduler(self, scheduler):
        scheduler.set_as_rr(self._quantum)

    def get_quantum(self):
        return self._quantum