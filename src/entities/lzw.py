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
        binary_data = struct.pack('>%dI' % len(compressed_data), *compressed_data)
        return binary_data
    
    def decode(self, encoded_data):
        decoded_data = list(struct.unpack('>%dI' % (len(encoded_data) // 4), encoded_data))
        return decoded_data
    
    def lzw_run_analysis(self, data, filename):
        compressed = self.compress(data)
        encoded_data = self.encode(compressed)
        FM().create_compressed_file(filename[:-3] + "lzw", encoded_data)
        decoded_data = self.decode(encoded_data)
        decompressed = self.decompress(decoded_data)
        FM().create_txt_file(filename[:-4] + "_decomp_lzw.txt", decompressed)
        
