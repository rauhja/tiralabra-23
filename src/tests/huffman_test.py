import unittest
import os
from entities.huffman import HuffmanCoding
from services.fileservice import FileManagementService


class TestHuffman(unittest.TestCase):
    def setUp(self):
        self.huffman = HuffmanCoding()
        self.FM = FileManagementService()

    def test_calc_frequency(self):
        data = "abacabad"
        freq = self.huffman.calc_frequency(data)
        self.assertEqual(freq, {'a': 4, 'b': 2, 'c': 1, 'd': 1})

    def test_make_heap(self):
        freq = {'a': 4, 'b': 2, 'c': 1, 'd': 1}
        self.huffman.make_heap(freq)
        self.assertEqual(self.huffman.heap[0].freq, 1)
        self.assertEqual(self.huffman.heap[1].freq, 1)
        self.assertEqual(self.huffman.heap[2].freq, 2)
        self.assertEqual(self.huffman.heap[3].freq, 4)

    def test_build_huffman_tree(self):
        freq = {'a': 4, 'b': 2, 'c': 1, 'd': 1}
        self.huffman.make_heap(freq)
        self.huffman.build_huffman_tree()
        self.assertEqual(self.huffman.heap[0].freq, 8)
        self.assertEqual(self.huffman.heap[0].left.char, 'a')
        self.assertEqual(self.huffman.heap[0].right.char, None)
        self.assertEqual(self.huffman.heap[0].right.left.char, 'b')
        self.assertEqual(self.huffman.heap[0].right.right.char, None)
        self.assertEqual(self.huffman.heap[0].right.right.left.char, 'c')
        self.assertEqual(self.huffman.heap[0].right.right.right.char, 'd')
        
    def test_huffman_algorithm(self):
        data = "abacabad"
        compress = self.huffman.huffman_encode(data)
        self.FM.create_compressed_file("test-data/test.huf", compress)
        self.assertTrue(os.path.exists("test-data/test.huf"))
        compressed = self.FM.get_compressed_file("test-data/test.huf")
        decomp = self.huffman.huffman_decode(compressed)
        self.FM.create_txt_file("test-data/test_decomp_huf.txt", decomp)
        self.assertTrue(os.path.exists("test-data/test_decomp_huf.txt"))
        self.assertEqual(decomp, "abacabad")
        os.remove("test-data/test.huf")
        os.remove("test-data/test_decomp_huf.txt")

    def test_huffman_large(self):
        data = self.FM.get_uncompressed_file("test-data/gutenberg-top-10.txt")
        compress = self.huffman.huffman_encode(data)
        self.FM.create_compressed_file("test-data/gutenberg-top-10.huf", compress)
        self.assertTrue(os.path.exists("test-data/gutenberg-top-10.huf"))
        compressed = self.FM.get_compressed_file("test-data/gutenberg-top-10.huf")
        decomp = self.huffman.huffman_decode(compressed)
        self.FM.create_txt_file("test-data/gutenberg-top-10_decomp_huf.txt", decomp)
        self.assertTrue(os.path.exists("test-data/gutenberg-top-10_decomp_huf.txt"))
        self.assertEqual(decomp, data)
        os.remove("test-data/gutenberg-top-10.huf")
        os.remove("test-data/gutenberg-top-10_decomp_huf.txt")
