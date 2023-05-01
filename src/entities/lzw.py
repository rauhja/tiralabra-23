from io import StringIO
import struct
from services.fileservice import FileManagementService as FM


class LZWCoding:
    def __init__(self):
        pass

    def compress(self, data):
        """Compresses a string to a list of output symbols.
            Args:
                data (str): The string to be compressed
            Returns:
                compressed_data (list): A list containing the compressed data
        """
        dict_size = 256
        dict = {chr(i): i for i in range(dict_size)}
        w = ""
        compressed_data = []
        for char in data:
            wchar = w + char
            if wchar in dict:
                w = wchar
            else:
                compressed_data.append(dict[w])
                dict[wchar] = dict_size
                dict_size += 1
                w = char
        if w:
            compressed_data.append(dict[w])
        return compressed_data

    def decompress(self, compressed_data):
        """Decompresses a list of output symbols to a string.
            Args:
                compressed_data (list): A list containing the compressed data
            Returns:
                decompressed_data (str): The decompressed string
        """
        dict_size = 256
        dict = {i: chr(i) for i in range(dict_size)}
        decompressed_data = StringIO()
        w = chr(compressed_data.pop(0))
        decompressed_data.write(w)
        for k in compressed_data:
            if k in dict:
                entry = dict[k]
            elif k == len(dict):
                entry = w + w[0]
            else:
                raise ValueError("Bad compressed k: %s" % k)
            decompressed_data.write(entry)
            dict[dict_size] = w + entry[0]
            dict_size += 1
            w = entry
        return decompressed_data.getvalue()

    def encode(self, compressed_data):
        """Encodes a list of integers to a binary string.
            Args:
                compressed_data (list): A list containing the compressed data
            Returns:
                binary_data (str): The encoded binary string
        """
        binary_data = struct.pack('>%dI' % len(
            compressed_data), *compressed_data)
        return binary_data

    def decode(self, encoded_data):
        """Decodes a binary string to a list of integers.
            Args:
                encoded_data (str): The encoded binary string
            Returns:
                decoded_data (list): A list containing the decoded data
        """
        decoded_data = list(struct.unpack('>%dI' %
                            (len(encoded_data) // 4), encoded_data))
        return decoded_data

    def run_compress(self, data):
        """Calls the compression algorithm.
            Args:
                data (str): The string to be compressed
            Returns:
                encoded_data (str): The encoded binary string
        """
        compressed = self.compress(data)
        encoded_data = self.encode(compressed)
        return encoded_data

    def run_decompress(self, data):
        """Calls the decompression algorithm.
            Args:
                data (str): The encoded binary string
            Returns:
                decompressed (str): The decompressed string
        """
        decoded_data = self.decode(data)
        decompressed = self.decompress(decoded_data)
        return decompressed

