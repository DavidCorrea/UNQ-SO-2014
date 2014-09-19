from enum import Enum

class PCB:

	def __init__(self,id, startM, amountInstructions):
		self._id = id
		self._startM = startM
		self._amountInstructions = amountInstructions
		self._pc = startM
		self._status = PCBStatus.new

	def changeStatus(self, newStatus):
		self._status = newStatus

	def increment(self):
		self._pc += 1

	def hasFinished(self):
		return self._pc == (self._startM + self._amountInstructions)
		

class PCBStatus(Enum):
	new = "New"
	ready = "Ready"
	busy = "Busy"
	waiting = "Waiting"
	running = "Running"
	complete = "Complete"	

class PCBPriority(Enum):
	low = "Low"
	medium = "Medium"
	high = "High"