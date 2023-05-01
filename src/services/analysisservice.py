import time
from services.fileservice import FileManagementService as FM
from entities.huffman import HuffmanCoding as Huffman
from entities.lzw import LZWCoding as LZW

class AnalysisService:
    def __init__(self):
        self.log = {}
    
    def run_analysis(self, filename):
        data = FM().get_uncompressed_file(filename)
        self.log["original_size"] = FM().get_file_size(filename)
        
        huff_t0 = time.time()
        compressed = Huffman().huffman_encode(data)
        FM().create_compressed_file(filename[:-3] + "huf", compressed)
        huff_t1 = time.time()
        huff_comp_total = huff_t1 - huff_t0
        self.log["huff_comp_total"] = f"{huff_comp_total:.2f}"
        self.log["huff_comp_size"] = FM().get_file_size(filename[:-3] + "huf")
        self.log["huff_comp_ratio"] = self.get_compression_ratio(self.log["original_size"], self.log["huff_comp_size"])
        self.log["huff_comp_space_saving"] = self.get_space_saving(self.log["original_size"], self.log["huff_comp_size"])
        
        huff_t0 = time.time()
        decompressed = Huffman().huffman_decode(compressed)
        FM().create_txt_file(filename[:-4] + "_decomp_huf.txt", decompressed)
        huff_t1 = time.time()
        huff_decomp_total = huff_t1 - huff_t0
        self.log["huff_decomp_total"] = f"{huff_decomp_total:.2f}"
        
        lzw_t0 = time.time()
        compressed = LZW().run_compress(data)
        FM().create_compressed_file(filename[:-3] + "lzw", compressed)
        lzw_t1 = time.time()
        lzw_comp_total = lzw_t1 - lzw_t0
        self.log["lzw_comp_total"] = f"{lzw_comp_total:.2f}"
        self.log["lzw_comp_size"] = FM().get_file_size(filename[:-3] + "lzw")
        self.log["lzw_comp_ratio"] = self.get_compression_ratio(self.log["original_size"], self.log["lzw_comp_size"])
        self.log["lzw_comp_space_saving"] = self.get_space_saving(self.log["original_size"], self.log["lzw_comp_size"])
        
        lzw_t0 = time.time()
        decompressed = LZW().run_decompress(compressed)
        FM().create_txt_file(filename[:-4] + "_decomp_lzw.txt", decompressed)
        lzw_t1 = time.time()
        lzw_decomp_total = lzw_t1 - lzw_t0
        self.log["lzw_decomp_total"] = f"{lzw_decomp_total:.2f}"
        return self.log
        
        
    def get_space_saving(self, original, compressed):
        """Calculates the space saving of a file
            Args:
                original (int): The size of the original file
                compressed (int): The size of the compressed file
            Returns:
                float: The space saving in percentage
        """
        return (1-(compressed / original)) * 100
    
    def get_compression_ratio(self, original, compressed):
        """Calculates the compression ratio of a file
            Args:
                original (int): The size of the original file
                compressed (int): The size of the compressed file
            Returns:
                float: The compression ratio
        """
        return original / compressed