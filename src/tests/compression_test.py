import unittest
import os
from services.compressservice import CompressManagement
from services.fileservice import FileManagementService


class TestCompressionService(unittest.TestCase):
    def setUp(self):
        self.compress = CompressManagement()
        self.FM = FileManagementService()

    def test_compress_file_huffman(self):
        filename = "test-data/test.txt"
        method = "1"
        self.compress.compress_file(filename, method)
        self.assertTrue(os.path.exists("test-data/test.huf"))

    def test_compress_file_lzw(self):
        filename = "test-data/test.txt"
        method = "2"
        self.compress.compress_file(filename, method)
        self.assertTrue(os.path.exists("test-data/test.lzw"))

    def test_compress_file_invalid_method(self):
        filename = "test-data/test.txt"
        method = ""
        with self.assertRaises(Exception):
            self.compress.compress_file(filename, method)

    def test_decompress_file_huffman(self):
        filename = "test-data/test.huf"
        self.compress.decompress_file(filename)
        self.assertTrue(os.path.exists("test-data/test_decomp_huf.txt"))
        os.remove("test-data/test_decomp_huf.txt")
        os.remove("test-data/test.huf")

    def test_decompress_file_lzw(self):
        filename = "test-data/test.lzw"
        self.compress.decompress_file(filename)
        self.assertTrue(os.path.exists("test-data/test_decomp_lzw.txt"))
        os.remove("test-data/test_decomp_lzw.txt")
        os.remove("test-data/test.lzw")

    def test_decompress_file_invalid_file_type(self):
        filename = "test-data/test.huff"
        self.FM.create_compressed_file(filename, b"")
        with self.assertRaises(Exception):
            self.compress.decompress_file(filename)
        os.remove(filename)
