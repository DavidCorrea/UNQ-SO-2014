__author__ = 'robot'


class KernelConfig:

    def __init__(self):
        self._functions = []

    def add_function(self, function):
        self._functions.append(function)

    def configure(self, kernel):
        map(lambda f: f(kernel), self._functions)

