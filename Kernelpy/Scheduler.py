from CORBA import __init__
from Queue import PriorityQueue

class Scheduler:

    def __init__(self):
        self._policy = None


    def setAsFifo(self):
        self._policy = FifoScheduler()

    def setAsPQ(self):
        self._policy = PriorityoScheduler()

    def setAsRR(self):
        self._policy = RoundRobinScheduler()

    def add(self, pcb):
        self._policy.add(pcb)

    def getPCB(self):
        return self._policy.getPCB()

class FifoScheduler(Scheduler):

    def __init__(self):
        self._readyQ = []

    def add(self, pcb):
        self._readyQ.append(pcb)

    def getPCB(self):
        retPCB = self._readyQ[0]
        self._readyQ.remove(0)
        return retPCB


class PriorityoScheduler(Scheduler):

    def __init__(self):
        self._readyQ = PriorityQueue

    def add(self, pcb):
        self._readyQ._put(pcb)

    def getPCB(self):
        sorted(list(self._readyQ))[0]

class RoundRobinScheduler(Scheduler):
