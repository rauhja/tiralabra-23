import os

class FileManagementService:
    def __init__(self):
        pass

    def get_uncompressed_file(self, filename):
        with open(filename, "r", encoding="utf-8") as uncompressed_file:
            return uncompressed_file.read()

    def get_compressed_file(self, filename):
        with open(filename, "rb") as compressed_file:
            return compressed_file.read()

    def create_compressed_file(self, filename, data):
        with open(filename, "wb") as compressed_file:
            compressed_file.write(data)

    def create_txt_file(self, filename, data):
        with open(filename, "w", encoding="utf-8") as uncompressed_file:
            uncompressed_file.write(data)

    def get_file_size(self, filename):
        return os.path.getsize(filename)