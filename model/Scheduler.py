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
        self._policy = RoundRobinScheduler()
        self._quantum = quantum

    def add(self, pcb):
        self._policy.add(pcb)

    def next(self):
        return self._policy.getPCB


class FifoScheduler():

    def __init__(self):
        self._readyq = []

    def add(self, pcb):
        self._readyq.append(pcb)

    def get_pcb(self):
        ret_pcb = self._readyq[0]
        self._readyq.remove(0)
        return ret_pcb


class PriorityScheduler():

    def __init__(self):
        self._readyq = PriorityQueue

    def add(self, pcb):
        self._readyq.put(pcb)

    def get_pcb(self):
        sorted(list(self.readyq))[0]


class RoundRobinScheduler():

    def __init__(self, quantum):
        self._readyq = []
        self._quantum = quantum

    def add(self,pcb):
        self._readyq.append(pcb)

    def get_pcb(self):
        ret_pcb = self.readyq[0]
        self._readyq.remove(0)
        return ret_pcb
