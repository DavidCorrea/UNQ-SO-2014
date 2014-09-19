
class MemoryManager:

	def __init__(self, memory):
		self._memory = memory
		self._nextIndex = 0

	def write(self,program):
		begin = self._nextIndex
		for i in program.getInstructions():
			self._memory.put(self._nextIndex, i.text())
			self._nextIndex += 1
		return begin

	def read(self, memDir):
		return self._memory.get(memDir)
		
		
