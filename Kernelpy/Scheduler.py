class Scheduler

	def __init__(self):
		self._queue = Queue()

	def setFIFO(self):
		self._queue =