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

    def test_lzw_algorithm(self):
        data = "abacabad"
        compress = self.lzw.run_compress(data)
        self.FM.create_compressed_file("test-data/test.lzw", compress)
        self.assertTrue(os.path.exists("test-data/test.lzw"))
        comp_file = self.FM.get_compressed_file("test-data/test.lzw")
        decomp = self.lzw.run_decompress(comp_file)
        self.assertEqual(data, decomp)
        os.remove("test-data/test.lzw")

    def test_lzw_large(self):
        data = self.FM.get_uncompressed_file("test-data/gutenberg-top-10.txt")
        compress = self.lzw.run_compress(data)
        self.FM.create_compressed_file("test-data/gutenberg-top-10.lzw", compress)
        self.assertTrue(os.path.exists("test-data/gutenberg-top-10.lzw"))
        comp_file = self.FM.get_compressed_file("test-data/gutenberg-top-10.lzw")
        result = self.lzw.run_decompress(comp_file)
        self.assertEqual(data, result)
        os.remove("test-data/gutenberg-top-10.lzw")
