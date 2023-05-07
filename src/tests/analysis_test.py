import unittest
import os
from services.analysisservice import AnalysisService
from services.compressservice import CompressManagement
from services.fileservice import FileManagementService


class TestAnalysisService(unittest.TestCase):
    def setUp(self):
        self.compress = CompressManagement()
        self.FM = FileManagementService()
        self.analysis = AnalysisService()

    def test_analyze_file(self):
        filename = "test-data/test.txt"
        log = self.analysis.run_analysis(filename)
        self.assertTrue(os.path.exists("test-data/test.huf"))
        self.assertTrue(os.path.exists("test-data/test.lzw"))
        self.assertTrue(os.path.exists("test-data/test_decomp_huf.txt"))
        self.assertTrue(os.path.exists("test-data/test_decomp_lzw.txt"))
        self.assertTrue(log['original_size'])
        os.remove("test-data/test.huf")
        os.remove("test-data/test.lzw")
        os.remove("test-data/test_decomp_huf.txt")
        os.remove("test-data/test_decomp_lzw.txt")
