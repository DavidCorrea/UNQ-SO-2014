__author__ = 'robot'


class Folder:

    def __init__(self, address):
        self._address = '/'
        self._files = []
        self._childrens = []

    def new_file(self, file):
        self._files.append(file)

    def new_folder(self, folder_name):
        folder = Folder(self._address + folder_name + "/")
        self._childrens.append(folder)

    def get_file(self, file_name):
        return filter(lambda f: f.name.equals(file_name), self._files)

    def get_files(self):
        return self._files

    def get_folders(self):
        return self._childrens


class File:

    def __init__(self, name):
        self._name = name
        self._diskBlocks = []

    def get_name(self):
        return  self._name