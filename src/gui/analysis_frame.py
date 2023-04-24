import customtkinter
import tkinter as tk
from tkinter import filedialog as fd
from services.compressservice import CompressManagement


class AnalysisFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_rowconfigure(1)
        self.grid_columnconfigure(1, weight=1)

        self.text_var = tk.StringVar()
        self.text_var.set("No file selected")

        self.original_var = tk.StringVar()
        self.original_var.set("")

        self.huffman_var = tk.StringVar()
        self.huffman_var.set("")

        self.lzw_var = tk.StringVar()
        self.lzw_var.set("")

        self.header = customtkinter.CTkLabel(
            self, text="Analysis", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.header.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

        self.input_label = customtkinter.CTkLabel(
            self, text="Select file to analyse:")
        self.input_label.grid(row=1, column=0, columnspan=2,
                              sticky="w", padx=(10, 0), pady=(0, 0))

        self.input = customtkinter.CTkEntry(
            self, textvariable=self.text_var, width=400)
        self.input.grid(row=2, column=0, columnspan=2,
                        sticky="ew", padx=(10, 0), pady=(0, 20))
        self.input.configure(textvariable=self.text_var)

        self.input_button = customtkinter.CTkButton(
            master=self, text="Open", command=self.get_file, width=100)
        self.input_button.grid(row=2, column=2, sticky="ew",
                               padx=(20, 20), pady=(0, 20))

        self.run_button = customtkinter.CTkButton(
            self, text="Run analysis", width=100, command=self._handle_run_analysis)
        self.run_button.grid(row=3, column=0, sticky="w",
                             padx=(10, 20), pady=(0, 5))

        self.result_header = customtkinter.CTkLabel(
            self, text="Results", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.result_header.grid(row=4, column=0, padx=(10, 10), pady=(10, 5))

        self.original_label = customtkinter.CTkLabel(
            self, text="Original file size: ", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.original_label.grid(
            row=5, column=0, sticky="w", padx=(10, 10), pady=(10, 0))

        self.original_size_label = customtkinter.CTkLabel(
            self, textvariable=self.original_var, font=customtkinter.CTkFont(size=12))
        self.original_size_label.grid(
            row=5, column=1, sticky="w", padx=(10, 10), pady=(10, 0))

        self.huffman_label = customtkinter.CTkLabel(
            self, text="Huffman file size: ", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.huffman_label.grid(row=6, column=0, sticky="w", padx=(10, 10))

        self.huffman_size_label = customtkinter.CTkLabel(
            self, textvariable=self.huffman_var, font=customtkinter.CTkFont(size=12))
        self.huffman_size_label.grid(
            row=6, column=1, sticky="w", padx=(10, 10))

        self.lzw_label = customtkinter.CTkLabel(
            self, text="LZW file size: ", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.lzw_label.grid(row=7, column=0, sticky="w", padx=(10, 10))

        self.lzw_size_label = customtkinter.CTkLabel(
            self, textvariable=self.lzw_var, font=customtkinter.CTkFont(size=12))
        self.lzw_size_label.grid(row=7, column=1, sticky="w", padx=(10, 10))

    def get_file(self):
        filetypes = (("Text files", "*.txt"),
                     ("Compressed files", "*.huf *.lzw"))
        self.file_path = fd.askopenfilename(
            title="Select a file", filetypes=filetypes)
        self.text_var.set(self.file_path)

    def _handle_run_analysis(self):
        original, huffman, lzw, huff_comp, lzw_comp = CompressManagement(
        ).run_analysis(self.file_path)
        original_string = f"{original} bytes."
        self.original_var.set(original_string)
        huffman_string = f"{huffman} bytes. Compression ratio: {huff_comp:.2f}%"
        self.huffman_var.set(huffman_string)
        lzw_string = f"{lzw} bytes. Compression ratio: {lzw_comp:.2f}%"
        self.lzw_var.set(lzw_string)
