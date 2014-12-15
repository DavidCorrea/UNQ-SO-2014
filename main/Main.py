__author__ = 'David'

import cmd
from main.CustomLogger import Logger
from main.CmdAppModel import CmdAppModel
from Options import Options
from main.KernelConfigurations import KernelConfig


class Main(cmd.Cmd):

    prompt = 'SO :: '

    def __init__(self):
        cmd.Cmd.__init__(self)
        Logger.ok("Initializing App...")
        self._appModel = CmdAppModel()
        self._options = Options()
        self._config = KernelConfig()


    def welcome_message(self):
        print "Welcome! This is the SO-2014 Command Prompt. \n"

    def start_setup(self):
        print ":: Kernel Setup \n"
        self.memory_policies_message()
        self.scheduler_policies_message()
        self._appModel.build_kernel(self._config)

    def memory_policies_message(self):
        print """Memory Policies :: Please, select one of the next options:

        1 - Continuous Assignment
        2 - Paging
        """
        option_selected = int(raw_input("Policy: "))
        if option_selected is 1:
            self._config.add_function(self._options.eval_memory_option(option_selected))
            self.continuous_assignment_policies_message()
        else:
            page_size = int(input("Page Size: "))
            self._config.add_function(self._options.eval_memory_option(option_selected, page_size))

    def scheduler_policies_message(self):
        print """Scheduler Policies :: Please, select one of the next options:

        1 - First in, First out
        2 - Priority
        3 - Round Robin
        """
        option_selected = input("Policy: ")
        if option_selected is 3:
            quantum = input("Quantum: ")
            self._config.add_function(self._options.eval_scheduler_option(option_selected, quantum))
        else:
            self._config.add_function(self._options.eval_scheduler_option(option_selected))

    def continuous_assignment_policies_message(self):
        print """Continuous Assignment Policies :: Please, select one of the next options:

        1 - First Fit
        2 - Worst Fit
        3 - Best Fit
        """
        option_selected = input("Policy: ")
        self._config.add_function(self._options.eval_continuous_assignment_option(option_selected))

    def do_run(self, program_name):
        self._appModel.run(program_name)

    def do_list(self, files):
        files = [fl.get_name() for fl in self._appModel.get_kernel().get_file_system().list_files()]
        print '\n'.join(files)


if __name__ == '__main__':
    app = Main()
    app.welcome_message()
    app.start_setup()
    app.do_run()
    app.do_list()
    app.cmdloop()
