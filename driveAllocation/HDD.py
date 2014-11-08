from directoryTree import *


class HDD:

    def __init__(self):
        self._directory = Folder("root")

    def get_program(self, program_route, file_name):
        directories = program_route[1:-1].split("/")
        try:
            result = self._directory
            for d in directories:
                result = result.get_folder(d)
            return result.get_file(file_name)
        except IndexError:
            "No existe el directorio o el archivo."

    def add_program(self, program_route, program):
        #A la hora de agregar un programa, la direccion ya debe existir
        directories = program_route[1:-1].split("/")
        try:
            result = self._directory
            for d in directories:
                result = result.get_folder(d)
            result.new_file(File(program.name, program.get_instructions))
        except IndexError:
            "No existe el directorio, este debe existir para que agregue el programa"

    def add_folder(self, folder_name):
        self._directory.new_folder(folder_name)

