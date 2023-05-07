import os
import matplotlib.pyplot as plt
import pandas as pd
from services.analysisservice import AnalysisService as AS

def main():
    inputs = "test-data/inputs/"
    analyze(inputs)

def analyze(inputs):
    ignore = ".DS_Store"
    analyzed_huf = []
    analyzed_lzw = []
    analyzed = []
    for file in sorted(os.listdir(inputs), key=lambda f: os.path.getsize(os.path.join(inputs, f))):
        if file != ignore:
            print("Analyzing: " + file)
            result = AS().run_analysis(inputs + file)
            analyzed.append(result)
            analyzed_huf.append(result["huff_comp_space_saving"])
            analyzed_lzw.append(result["lzw_comp_space_saving"])
    plot(analyzed_huf, analyzed_lzw)
    table(analyzed)
    
def plot(analyzed_huf, analyzed_lzw):
    plt.figure()
    plt.plot(range(1, len(analyzed_huf) + 1), analyzed_huf, marker='o', label="Huffman")
    plt.plot(range(1, len(analyzed_lzw) + 1), analyzed_lzw, marker='o', label="LZW")
    
    plt.xlabel("Original file size")
    plt.ylabel("Space saving (%)")
    plt.xticks(range(1, len(analyzed_huf) + 1), ('512','1kb','2kb','4kb','8kb','16kb','32kb','65kb','131kb','262kb','524kb','1Mb','2Mb', '4Mb'), rotation=45)

    plt.title("Space saving of Huffman and LZW")
    plt.legend(["Huffman", "LZW"])
    plt.savefig("test-data/outputs/space_saving.png")
    
def table(analyzed):
    df = pd.DataFrame(analyzed)
    columns = [
    'original_size',
    'huff_comp_total',
    'huff_comp_size',
    'huff_comp_ratio',
    'huff_comp_space_saving',
    'huff_decomp_total',
    'lzw_comp_total',
    'lzw_comp_size',
    'lzw_comp_ratio',
    'lzw_comp_space_saving',
    'lzw_decomp_total'
    ]
    df = df[columns]
    df.to_csv("test-data/outputs/analysis.csv", index=False)

main()