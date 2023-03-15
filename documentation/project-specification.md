# Project specification

This is a project for the University of Helsinki course "Data Structures and Algorithms". The goal is to compare two lossless data compression algorithms: Huffman coding and Lempel-Ziv-Welch coding.

## Study program

Tietojenkäsittelytieteen kandidaatti (TKT)

## Project language

Documentation will be in English.
Programming language will be Python.

## Algorithms used

The algorithms used are Huffman coding and Lempel-Ziv-Welch LZW coding.

## Solving the problem

The aim of the project is to compare the two algorithms in terms of compression ratio and time complexity. The algorithms will be implemented in Python. A desired outcome for compression ratio is at least 40-60% of the original file size. File should also be decompressed without losing any information.

## Time complexity

**Huffman:**
Time complexity of the Huffman algorithm is O(n log n) where n is the number of unique characters being coded. The algorithm is using a heap data structure, which has a time complexity of O(log n).

**LZW:**
Time complexity of the LZW algorithm is O(n) where n is the number of characters in the file. The algorithm is using a dictionary data structure, which has a time complexity of O(1) on average.

## Sources

**Huffman coding:**

- [Wikipedia: Huffman coding](https://en.wikipedia.org/wiki/Huffman_coding)
- [The University of Auckland: Huffman Encoding](https://www.cs.auckland.ac.nz/software/AlgAnim/huffman.html)

**Lempel-Ziv-Welch LZW coding:**

- [Wikipedia: Lempel-Ziv-Welch](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch)
- [Youtube: Lempel-Ziv-Welch (LZW) Compression - Data Structures](https://www.youtube.com/watch?v=IskLTLrQYag)
