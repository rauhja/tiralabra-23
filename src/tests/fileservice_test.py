import unittest
from services.fileservice import FileManagementService


class TestFileService(unittest.TestCase):
    def setUp(self):
        self.flmgmt = FileManagementService()

    def test_get_uncompressed_file(self):
        data = self.flmgmt.get_uncompressed_file("test-data/test.txt")
        self.assertEqual(data, "aaabbc")

    def test_create_txt_file(self):
        self.flmgmt.create_txt_file("test-data/test.txt", "aaabbc")
        data = self.flmgmt.get_uncompressed_file("test-data/test.txt")
        self.assertEqual(data, "aaabbc")

    # def test_create_compressed_file(self):
    #     self.flmgmt.create_compressed_file("test-data/test.huff", "")
    #     data = self.flmgmt.get_compressed_file("test-data/test.huff")
    #     self.assertEqual(data, "aaabbc")
