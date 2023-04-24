import customtkinter
import tkinter as tk
from tkinter import filedialog as fd
from gui.components.method import Method
from services.compressservice import CompressManagement


class CompFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_rowconfigure(1)
        self.grid_columnconfigure(1, weight=1)

        self.text_var = tk.StringVar()
        self.text_var.set("No file selected")

        self.header = customtkinter.CTkLabel(
            self, text="Compress/Decompress", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.header.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

        self.input = customtkinter.CTkEntry(
            self, textvariable=self.text_var, width=400)
        self.input.grid(row=1, column=0, columnspan=2,
                        sticky="ew", padx=(10, 0), pady=(0, 20))
        self.input.configure(textvariable=self.text_var)

        self.input_button = customtkinter.CTkButton(
            master=self, text="Open", command=self.get_file, width=100)
        self.input_button.grid(row=1, column=2, sticky="ew",
                               padx=(20, 20), pady=(0, 20))

        self.comp_method = Method(self)
        self.comp_method.grid(row=2, column=0, sticky="w",
                              padx=(10, 0), pady=(0, 5))

        self.decomp_button = customtkinter.CTkButton(
            self, text="Decompress", width=100, command=self._handle_decompress)
        self.decomp_button.grid(row=2, column=2, padx=(5, 0), pady=(0, 5))

        self.comp_button = customtkinter.CTkButton(
            self, text="Compress", width=100, command=self._handle_compress)
        self.comp_button.grid(row=2, column=1, sticky="e",
                              padx=(10, 20), pady=(0, 5))

        self.status_var = tk.StringVar()
        self.status_var.set("")
        self.status_label = customtkinter.CTkLabel(self, textvariable=self.status_var,
                                                   font=customtkinter.CTkFont(size=13, weight="bold"))
        self.status_label.grid(row=3, column=0, columnspan=3, sticky="ew",
                               padx=(10, 10), pady=(0, 10))

    def get_file(self):
        filetypes = (("Text files", "*.txt"),
                     ("Compressed files", "*.huf *.lzw"))
        self.file_path = fd.askopenfilename(
            title="Select a file", filetypes=filetypes)
        self.text_var.set(self.file_path)

    def _handle_compress(self):
        method = self.comp_method.get_value()
        try:
            CompressManagement().compress_file(self.file_path, method)
            self.status_var.set("Compress Success")
        except:
            self.status_var.set("Compress Error")

    def _handle_decompress(self):
        try:
            CompressManagement().decompress_file(self.file_path)
            self.status_var.set("Decompress Success")
        except:
            self.status_var.set("Decompress Error")
