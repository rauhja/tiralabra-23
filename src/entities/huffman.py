from heapq import heappush, heappop
import json
from services.fileservice import FileManagementService as FM


class HuffmanCoding:
    def __init__(self):
        """Constructor for HuffmanCoding class. Initializes the heap,
        the codes dictionary and the frequency dictionary"""
        self.heap = []
        self.codes = {}
        self.freq = {}
        self.decode_mapping = {}

    class HuffmanNode:
        def __init__(self, char, freq):
            """Constructor for HuffmanNode class. Initializes the node's character,
            frequency, left and right child"""
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None

        def __lt__(self, other_node):
            """Compares the frequency of two nodes"""
            return self.freq < other_node.freq

    def calc_frequency(self, data):
        """Calculates the frequency of each character in a string
            Args:
                data (str): The string to be analyzed
            Returns:
                freq (dict): A dictionary containing the frequency of each character
        """
        for char in data:
            if not char in self.freq:
                self.freq[char] = 0
            self.freq[char] += 1
        return self.freq

    def make_heap(self, freq):
        """Creates a heap of HuffmanNodes
            Args:
                freq (dict): A dictionary containing the frequency of each character
        """
        for key in freq:
            node = self.HuffmanNode(key, freq[key])
            heappush(self.heap, node)

    def build_huffman_tree(self):
        """Builds the Huffman tree
        """
        while len(self.heap) > 1:
            left = heappop(self.heap)
            right = heappop(self.heap)
            merged = self.HuffmanNode(None, left.freq + right.freq)
            merged.left = left
            merged.right = right
            heappush(self.heap, merged)

    def encode_helper(self, root, current_code):
        """Helper function for encoding the data
            Args:
                root (HuffmanNode): The root of the Huffman tree
                current_code (str): The current code
        """
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
        """Encodes the data using the codes dictionary
            Args:
                data (str): The string to be encoded
            Returns:
                encoded_data (str): The encoded data as binary string
        """
        encoded_data = ""
        for char in data:
            encoded_data += self.codes[char]
        return encoded_data

    def get_extra_bits(self, encoded_data):
        """Adds extra bits to the encoded data to make it a multiple of 8
            Args:
                encoded_data (str): The encoded data as binary string
            Returns:
                encoded_data (str): The encoded data as binary string with extra bits and bit info
        """
        extra_bits = 8 - len(encoded_data) % 8
        for _ in range(extra_bits):
            encoded_data += "0"
        bit_info = f'{extra_bits:08b}'
        encoded_data = bit_info + encoded_data
        return encoded_data

    def get_compressed_array(self, encoded_data, encoded_map):
        """Creates a bytearray containing the encoded data and the encoded map
            Args:
                encoded_data (str): The encoded data as binary string with extra bits and bit info
                encoded_map (str): The dictionary containing the encoded characters
            Returns:
                bits (bytearray): The compressed data
        """
        bits = bytearray()
        for i in range(0, len(encoded_data), 8):
            byte = encoded_data[i:i+8]
            bits.append(int(byte, 2))
        map_size = len(encoded_map).to_bytes(2, byteorder='big')
        bits = map_size + encoded_map + bits
        return bits

    def get_encoded_decode_map(self):
        """Returns the encoded decode map"""
        return json.dumps(self.decode_mapping).encode(encoding="utf-8", errors="strict")

    def huffman_encode(self, data):
        """Encodes the data using the Huffman algorithm

            Args:
                data (str): The string to be encoded
            Returns:
                compressed (bytearray): The compressed data
        """
        freq = self.calc_frequency(data)
        self.make_heap(freq)
        self.build_huffman_tree()
        self.encode()

        encoded_data = self.get_encoded_data(data)
        extra_bits_data = self.get_extra_bits(encoded_data)
        encoded_decode_map = self.get_encoded_decode_map()
        compressed = self.get_compressed_array(
            extra_bits_data, encoded_decode_map)
        return compressed

    def remove_dictionary(self, compressed_data):
        """Removes the decoding dictionary from the compressed data
            Args:
                compressed_data (bytearray): The compressed data
            Returns:
                compressed_data (bytearray): The compressed data without the decoding dictionary
                decoder (dict): The decoding dictionary
        """
        dict_size = int.from_bytes(compressed_data[:2], byteorder='big')
        get_decoder_dict = compressed_data[2:dict_size+2]
        decoder = json.loads(get_decoder_dict.decode(
            encoding="utf-8", errors="strict"))
        compressed_data = compressed_data[dict_size+2:]
        return compressed_data, decoder

    def remove_extra_bits(self, bit_string):
        """Removes the extra bits from the bit string
            Args:
                bit_string (str): The bit string
            Returns:
                bit_string (str): The bit string without the extra bits
        """
        bit_info = bit_string[:8]
        no_extra_bits = int(bit_info, 2)
        bit_string = bit_string[8:]
        return bit_string[:-1 * no_extra_bits]

    def decode_data(self, encoded_data, decoder):
        """Decodes the encoded data using the decoding dictionary
            Args:
                encoded_data (str): The encoded data
                decoder (dict): The decoding dictionary
            Returns:
                decoded_data (str): The decoded data
        """
        current_code = ""
        decoded_data = ""
        for bit in encoded_data:
            current_code += bit
            if current_code in decoder:
                character = decoder[current_code]
                decoded_data += character
                current_code = ""
        return decoded_data

    def huffman_decode(self, compressed_data):
        """Decodes the compressed data using the Huffman algorithm
            Args:
                compressed_data (bytearray): The compressed data
            Returns:
                decoded_data (str): The decoded data
        """
        bit_string = ""
        compressed_data, decoder = self.remove_dictionary(compressed_data)
        for byte in compressed_data:
            bits = bin(byte)[2:].rjust(8, "0")
            bit_string += bits
        encoded_data = self.remove_extra_bits(bit_string)
        decoded_data = self.decode_data(encoded_data, decoder)
        return decoded_data
