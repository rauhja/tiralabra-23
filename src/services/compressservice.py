from entities.huffman import HuffmanCoding
from entities.lzw import LZWCoding
from services.fileservice import FileManagementService


class CompressManagement:
    def __init__(self):
        """Constructor for CompressManagement class. Initializes the FileManagementService, 
        the HuffmanCoding and the Lempel-Ziv-Welch class"""
        self.filemgmt = FileManagementService()
        self.huffman = HuffmanCoding()
        self.lzw = LZWCoding()

    def compress_file(self, filename, method):
        """Compresses a file using the Huffman or Lempel-Ziv-Welch algorithm and
        creates a new file with the compressed data

            Args:
                filename (str): The name of the file to be compressed
                method (str): The method to be used for compression. 1 for Huffman,
                2 for Lempel-Ziv-Welch
        """
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
        """Decompresses a file using the Huffman or Lempel-Ziv-Welch algorithm and creates
        a new file with the decompressed data.

            Args:
                filename (str): The name of the file to be decompressed
        """
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
            raise Exception("Invalid file type")
