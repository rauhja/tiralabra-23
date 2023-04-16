# Lossless data compression

This is a project for the University of Helsinki course "Data Structures and Algorithms". The goal is to compare two lossless data compression algorithms: Huffman coding and Lempel-Ziv-Welch (LZW) coding.

Please see the project documentation for more information.

## Project documentation

- [Project specification](documentation/project-specification.md)
- [Testing documentation](documentation/test-documentation.md)
- [Implementation document](documentation/implementation-document.md)

- Weekly reports:
  - [Week 1](documentation/weekly-report-1.md)
  - [Week 2](documentation/weekly-report-2.md)
  - [Week 3](documentation/weekly-report-3.md)
  - [Week 4](documentation/weekly-report-4.md)

## Installation

To install the project run the following command:

```bash
poetry install
```

## Usage

To start the project use the following command:

```bash
poetry run invoke start
```

To run the tests use the following command:

```bash
poetry run invoke test
```

To run the tests with coverage use the following command:

```bash
poetry run invoke coverage-report
```
