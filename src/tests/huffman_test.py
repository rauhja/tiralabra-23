import unittest
from entities.huffman import HuffmanCoding


class TestHuffman(unittest.TestCase):
    def setUp(self):
        self.huffman = HuffmanCoding()

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

        
