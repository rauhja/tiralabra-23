from heapq import heappush, heappop
from services.fileservice import FileManagementService


class HuffmanCoding:
    def __init__(self):
        self.heap = []
        self.codes = {}
        self.freq = {}
        self.decode_mapping = {}

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
            self.decode_mapping[current_code] = root.char
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
    
    def remove_extra_bits(self, bit_string):
        bit_info = bit_string[:8]
        no_extra_bits = int(bit_info, 2)
        bit_string = bit_string[8:]
        return bit_string[:-1 * no_extra_bits]
    
    def decode_data(self, encoded_data):
        current_code = ""
        decoded_data = ""
        for bit in encoded_data:
            current_code += bit
            if current_code in self.decode_mapping:
                character = self.decode_mapping[current_code]
                decoded_data += character
                current_code = ""
        return decoded_data
    
    def huffman_decode(self, compressed_data):
        bit_string = ""
        for byte in compressed_data:
            bits = bin(byte)[2:].rjust(8, "0")
            bit_string += bits
        encoded_data = self.remove_extra_bits(bit_string)
        decoded_data = self.decode_data(encoded_data)
        return decoded_data
    
    def huffman_run_analysis(self, data, filename):
        compressed = self.huffman_encode(data)
        FileManagementService().create_compressed_file(filename[:-3] + "huff", compressed)
        decompressed = self.huffman_decode(compressed)
        FileManagementService().create_txt_file(filename[:-4] + "_decomp.txt", decompressed)    
