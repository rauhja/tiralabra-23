from entities.huffman import HuffmanCoding
from services.fileservice import FileManagementService

class CompressManagement:
    def __init__(self):
        self.filemgmt = FileManagementService()
        self.huffman = HuffmanCoding()
    
    def compress_file(self, filename, method):
        data = self.filemgmt.get_uncompressed_file(filename)
        if method == "1":
            compress = self.huffman.huffman_encode(data)
            self.filemgmt.create_compressed_file(filename[:-3] + "huff", compress)
        else:
            raise Exception("Invalid method")
    
    def decompress_file(self, filename, method):
        data = self.filemgmt.get_compressed_file(filename)
        if method == "1":
            decompress = self.huffman.huffman_decode(data)
            print("decode:",decompress)
            self.filemgmt.create_txt_file(filename[:-5] + "_decomp.txt", decompress)
        else:
            raise Exception("Invalid method")
    
    def run_analysis(self, filename):
        data = self.filemgmt.get_uncompressed_file(filename)
        self.huffman.huffman_run_analysis(data, filename)