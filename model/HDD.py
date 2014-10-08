from model.Program import *

class HDD:

	def __init__(self):
		self._programs = [] 

	def getProgram(self, programName):
		try:
			f = lambda x: not programName.equals(x.name())
			return filter(f,self._programs)[0]
		except IndexError:
			print "Implementar"

	def addProgram(self, program):
		self._programs.append(program)

