from entities.huffman import HuffmanCoding
from entities.lzw import LZWCoding
from services.fileservice import FileManagementService


class CompressManagement:
    def __init__(self):
        self.filemgmt = FileManagementService()
        self.huffman = HuffmanCoding()
        self.lzw = LZWCoding()

    def compress_file(self, filename, method):
        data = self.filemgmt.get_uncompressed_file(filename)
        if method == "1":
            compress = self.huffman.huffman_encode(data)
            self.filemgmt.create_compressed_file(
                filename[:-3] + "huf", compress)
        elif method == "2":
            compress = self.lzw.run_compress(data)
            self.filemgmt.create_compressed_file(
                filename[:-3] + "lzw", compress)
        else:
            raise Exception("Invalid method")

    def decompress_file(self, filename):
        data = self.filemgmt.get_compressed_file(filename)
        method = filename[-3:]
        if method == "huf":
            decompress = self.huffman.huffman_decode(data)
            self.filemgmt.create_txt_file(
                filename[:-4] + "_decomp_huf.txt", decompress)
        elif method == "lzw":
            decompress = self.lzw.run_decompress(data)
            self.filemgmt.create_txt_file(
                filename[:-4] + "_decomp_lzw.txt", decompress)
        else:
            raise Exception("Invalid method")

    def get_compression_ratio(self, original, compressed):
        return ((original - compressed) / original) * 100

    def run_analysis(self, filename):
        data = self.filemgmt.get_uncompressed_file(filename)
        original = self.filemgmt.get_file_size(filename)
        huff_file_size = self.huffman.huffman_run_analysis(data, filename)
        huff_comp = self.get_compression_ratio(original, huff_file_size)
        lzw_file_size = self.lzw.lzw_run_analysis(data, filename)
        lzw_comp = self.get_compression_ratio(original, lzw_file_size)
        return original, huff_file_size, lzw_file_size, huff_comp, lzw_comp
