import unittest
from services.compressservice import CompressManagement


class TestCompressionService(unittest.TestCase):
    def setUp(self):
        self.compress = CompressManagement()

    # def test_compress_file(self):
    #     self.compress.compress_file("test-data/test.txt", "1")
    #     data = self.compress.filemgmt.get_compressed_file("test-data/test.huff")
    #     self.assertEqual(data, "b'{"0": "a", "10": "c", "11": "b"}\x07\x1f\x00'")
