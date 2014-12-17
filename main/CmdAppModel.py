__author__ = 'David'

from CustomLogger import Logger
from main.Setup import Setup
from model.Kernel import Kernel


class CmdAppModel:

    def __init__(self):
        self._kernel = None
        self._setup = Setup()
        Logger.ok("App ready to use. \n")

    def build_kernel(self, config):
        self._kernel = Kernel(self._setup.get_hdd(), config)

    def run(self, program_name):
        self._kernel.run(program_name)

    def get_kernel(self):
        return self._kernel
