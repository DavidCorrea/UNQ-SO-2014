
class MemoryManager:

    def __init__(self, memory, policy):
        self._memory = memory
        self._next_index = 0
        self._policy = policy

    def write(self, program):
        begin = self._next_index
        for i in program.getInstructions():
            # self._memory.put(self._next_index, i.text())
            self._memory.put(i.text())
            self._next_index += 1
        return begin

    def read(self, mem_dir):
        try:
            return self._memory.get(mem_dir)
        except IndexError:
            print "Implementar"

    def set_as_AC(self):
        self._policy = Asignacion_continua()

    def set_as_Paginacion(self):
        self._policy = Paginacion()


class Asignacion_continua:

    def __init__(self):
        self._bloque = [Bloque()]


class Paginacion: