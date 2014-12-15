__author__ = 'David'

from time import strftime


class Bcolors:
    INFO = '\033[90m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class Logger:

    @staticmethod
    def ok(message):
        print(Bcolors.OKBLUE + "[ OK ] [ " + strftime('%H:%M:%S') + " ] " + message + Bcolors.ENDC)

    @staticmethod
    def warning(message):
        print(Bcolors.WARNING + "[ WARNING ] [ " + strftime('%H:%M:%S') + " ] " + message + Bcolors.ENDC)

    @staticmethod
    def info(message):
        print(Bcolors.INFO + "[ INFO ] [ " + strftime('%H:%M:%S') + " ] " + message + Bcolors.ENDC)


