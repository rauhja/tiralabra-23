from io import StringIO
import struct
from services.fileservice import FileManagementService as FM


class LZWCoding:
    def __init__(self):
        pass

    def compress(self, data):
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
        binary_data = struct.pack('>%dI' % len(
            compressed_data), *compressed_data)
        return binary_data

    def decode(self, encoded_data):
        decoded_data = list(struct.unpack('>%dI' %
                            (len(encoded_data) // 4), encoded_data))
        return decoded_data

    def run_compress(self, data):
        compressed = self.compress(data)
        encoded_data = self.encode(compressed)
        return encoded_data

    def run_decompress(self, data):
        decoded_data = self.decode(data)
        decompressed = self.decompress(decoded_data)
        return decompressed

    def run_validity_check(self, data, filename):
        decompressed = FM().get_uncompressed_file(
            filename[:-4] + "_decomp_lzw.txt")
        if data == decompressed:
            return True
        return False

    def lzw_run_analysis(self, data, filename):
        compress = self.run_compress(data)
        FM().create_compressed_file(
            filename[:-3] + "lzw", compress)
        compressed_file_size = FM().get_file_size(filename[:-3] + "lzw")
        compressed_file = FM().get_compressed_file(filename[:-3] + "lzw")
        decompress = self.run_decompress(compressed_file, filename)
        FM().create_txt_file(
            filename[:-4] + "_decomp_lzw.txt", decompress)
        valid = self.run_validity_check(data, filename)
        if not valid:
            raise Exception("Invalid decompression")
        return compressed_file_size
