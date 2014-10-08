


class IOQueue:

    def __init__(self):
        self._waiting = []

    def addToWaiting(self, process):
        self._waiting.append(process)

    def dispatchAll(self, scheduler):
        map(lambda x : scheduler.add(x), self._waiting)
        self._waiting = []