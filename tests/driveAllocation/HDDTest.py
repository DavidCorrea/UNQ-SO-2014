from process.Program import *
from driveAllocation.HDD import *


class TestHDD(unittest.TestCase):

    #Arrange
    def setUp(self):
        self.program1 = Program(range(0,10), "Word")
        self.hdd = HDD()
        self.hdd.add_folder("/programs/")
        self.hdd.add_folder("/programs/office/")

    # The HDD starts at "root" so it can be ignored.
    def test_when_i_search_for_word_and_its_in_then_i_get_it(self):
        self.hdd.add_program("/programs/office/", self.program1)
        # self.hdd.get_program(...) returns a File! Shouldn't return a Program?
        self.assertEquals(self.program1.name(), self.hdd.get_program("/programs/office/", "Word").get_name())

    def test_when_I_have_a_complex_directory_and_I_look_for_many_files_then_I_get_them_all(self):
        self.hdd.add_folder("/programs/games/")
        self.hdd.add_folder("/programs/programmingStuff/")
        self.hdd.add_folder("/programs/tools/")

        self.program2 = Program(range(0,200), "League of Legends")
        self.program3 = Program(range(0,100), "WinHugs")
        self.program4 = Program(range(0,50), "Paint")

        self.hdd.add_program("/programs/office/", self.program1)
        self.hdd.add_program("/programs/games/", self.program2)
        self.hdd.add_program("/programs/programmingStuff/", self.program3)
        self.hdd.add_program("/programs/tools/", self.program4)

        self.assertEquals(self.program1.name(), self.hdd.get_program("/programs/office/", "Word").get_name())
        self.assertEquals(self.program2.name(), self.hdd.get_program("/programs/games/", "League of Legends").get_name())
        self.assertEquals(self.program3.name(), self.hdd.get_program("/programs/programmingStuff/", "WinHugs").get_name())
        self.assertEquals(self.program4.name(), self.hdd.get_program("/programs/tools/", "Paint").get_name())

    def test_when_i_search_for_word_and_its_not_in_then_i_get_an_exception(self):
        self.assertRaises(IndexError, self.hdd.get_program("/root/fail", "Word"))


suite = unittest.TestLoader().loadTestsFromTestCase(TestHDD)
unittest.TextTestRunner(verbosity=2).run(suite)