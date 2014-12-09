import unittest
from driveAllocation.FileSystemComponents import *
from driveAllocation.HDD import *
from process.Program import Program


class FileSystemComponentsTest(unittest.TestCase):

    def setUp(self):
        self._hdd = HDD(10)
        self.folder = Folder(None, "/")

    def test_getting_folder_name(self):
        print self.folder.get_absolute_address()
        self.assertEqual(self.folder.get_absolute_address(), "/")

    def test_adding_a_sibling(self):
        self.folder.new_folder("mario")
        self.assertEqual(len(self.folder.get_folders()), 1)

    def test_adding_a_file(self):
        self.folder.new_file(self._hdd.get_drive_saver(), "mario", Program(range(0, 10), "mario") )
        self.assertEqual(len(self.folder.get_files()), 1)


suite = unittest.TestLoader().loadTestsFromTestCase(FileSystemComponentsTest)
unittest.TextTestRunner(verbosity=2).run(suite)