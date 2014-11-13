import unittest
from driveAllocation.FileSystem import *


class FolderTest(unittest.TestCase):

    def setUp(self):
        self.folder = Folder("programs")
        self.file = File("mario", range(0, 10))

    def test_getting_folder_name(self):
        self.assertEqual(self.folder.__str__(), "/programs/")

    def test_adding_a_sibling(self):
        self.folder.new_folder("mario")
        self.assertEqual(len(self.folder.get_folders()), 1)

    def test_adding_a_file(self):
        self.folder.new_file(self.file)
        self.assertEqual(len(self.folder.get_files()), 1)


suite = unittest.TestLoader().loadTestsFromTestCase(FolderTest)
unittest.TextTestRunner(verbosity=2).run(suite)