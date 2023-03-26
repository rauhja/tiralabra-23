from heapq import heappush, heappop


class HuffmanCoding:
    def __init__(self):
        self.heap = []
        self.codes = {}
        self.freq = {}

    class HuffmanNode:
        def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None

        def __lt__(self, other_node):
            return self.freq < other_node.freq

    def calc_frequency(self, data):
        for char in data:
            if not char in self.freq:
                self.freq[char] = 0
            self.freq[char] += 1
        return self.freq

    def make_heap(self, freq):
        for key in freq:
            node = self.HuffmanNode(key, freq[key])
            heappush(self.heap, node)

    def build_huffman_tree(self):
        while len(self.heap) > 1:
            left = heappop(self.heap)
            right = heappop(self.heap)
            merged = self.HuffmanNode(None, left.freq + right.freq)
            merged.left = left
            merged.right = right
            heappush(self.heap, merged)

    def encode_helper(self, root, current_code):
        if root is None:
            return

        if root.char is not None:
            self.codes[root.char] = current_code
            return

        self.encode_helper(root.left, current_code + "0")
        self.encode_helper(root.right, current_code + "1")

    def encode(self):
        root = heappop(self.heap)
        current_code = ""
        self.encode_helper(root, current_code)

    def get_encoded_data(self, data):
        encoded_data = ""
        for char in data:
            encoded_data += self.codes[char]
        return encoded_data

    def get_extra_bits(self, encoded_data):
        extra_bits = 8 - len(encoded_data) % 8
        for _ in range(extra_bits):
            encoded_data += "0"
        bit_info = f'{extra_bits:08b}'
        encoded_data = bit_info + encoded_data
        return encoded_data

    def get_compressed_array(self, encoded_data):
        bits = bytearray()
        for i in range(0, len(encoded_data), 8):
            byte = encoded_data[i:i+8]
            bits.append(int(byte, 2))
        return bits

    def huffman_encode(self, data):
        freq = self.calc_frequency(data)
        self.make_heap(freq)
        self.build_huffman_tree()
        self.encode()

        encoded_data = self.get_encoded_data(data)
        extra_bits_data = self.get_extra_bits(encoded_data)

        compressed = self.get_compressed_array(extra_bits_data)
        return compressed

huffman = HuffmanCoding()
text = "Hello World"
result = huffman.huffman_encode(text)
print(result)
