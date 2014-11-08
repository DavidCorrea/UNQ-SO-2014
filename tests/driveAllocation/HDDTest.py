from process.Program import *
from driveAllocation.HDD import *


class TestHDD(unittest.TestCase):

    #Arrange
    def setUp(self):
        self.program1 = Program(range(0,10), "Word")
        self.hdd = HDD()
        self.hdd.add_folder("programs")

    def test_when_i_search_for_word_and_its_in_then_i_get_it(self):
        self.hdd.add_program("/root/programs/", self.program1)
        self.assertEquals(self.program1.name(), self.hdd.get_program("/root/programs", "Word").name())

    def test_when_i_search_for_word_and_its_not_in_then_i_get_an_exception(self):
        self.assertRaises(IndexError, self.hdd.get_program("/root/fail", "Word"))


suite = unittest.TestLoader().loadTestsFromTestCase(TestHDD)
unittest.TextTestRunner(verbosity=2).run(suite)