import unittest
import os
from entities.lzw import LZWCoding
from services.fileservice import FileManagementService


class TestLZW(unittest.TestCase):
    def setUp(self):
        self.lzw = LZWCoding()
        self.FM = FileManagementService()

    def test_compress(self):
        data = "abacabad"
        result = self.lzw.compress(data)
        self.assertEqual(result, [97, 98, 97, 99, 256, 97, 100])

    def test_run_analysis(self):
        data = self.FM.get_uncompressed_file("test-data/test.txt")
        self.lzw.lzw_run_analysis(data, "test-data/test.txt")
        result = self.FM.get_uncompressed_file("test-data/test_decomp_lzw.txt")
        self.assertEqual(data, result)
        os.remove("test-data/test_decomp_lzw.txt")
        os.remove("test-data/test.lzw")

    def test_run_analysis(self):
        data = self.FM.get_uncompressed_file("test-data/gutenberg-top-10.txt")
        self.lzw.lzw_run_analysis(data, "test-data/gutenberg-top-10.txt")
        result = self.FM.get_uncompressed_file(
            "test-data/gutenberg-top-10_decomp_lzw.txt")
        self.assertEqual(data, result)
        os.remove("test-data/gutenberg-top-10_decomp_lzw.txt")
        os.remove("test-data/gutenberg-top-10.lzw")
