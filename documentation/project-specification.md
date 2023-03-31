# Project specification

This is a project for the University of Helsinki course "Data Structures and Algorithms". The goal is to compare two lossless data compression algorithms: Huffman coding and Lempel-Ziv-Welch coding.

## Study program

Tietojenkäsittelytieteen kandidaatti (TKT)

## Project language

Documentation will be in English.

Programming language will be Python.

## Algorithms used

The algorithms used are Huffman coding and Lempel-Ziv-Welch LZW coding.

### Huffman pseudocode

```
1. Create a node for each character-frequency pair and add it to a min heap
2. While heap.length > 1
    1. Poll two nodes and count the sum of their frequencies (= res)
    2. Create new node with a frequency of res and set the summed nodes as it's children
    3. Add the node to the heap
3. Remaining node is the root of the Huffman tree
```

### LZW pseudocode

```
1. Initialize the dictionary to contain all strings of length one.
2. Find the longest string W in the dictionary that matches the current input.
3. Emit the dictionary index for W to output and remove W from the input.
4. Add W followed by the next symbol in the input to the dictionary.
5. Go to Step 2.
```

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
- [Huffman Encoding & Python Implementation](https://towardsdatascience.com/huffman-encoding-python-implementation-8448c3654328)

**Lempel-Ziv-Welch LZW coding:**

- [Wikipedia: Lempel-Ziv-Welch](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch)
- [Youtube: Lempel-Ziv-Welch (LZW) Compression - Data Structures](https://www.youtube.com/watch?v=IskLTLrQYag)
