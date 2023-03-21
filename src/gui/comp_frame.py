import customtkinter
from tkinter import filedialog as fd
import tkinter as tk
from gui.components.method import Method


class CompFrame(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="Select File", **kwargs):
        super().__init__(*args, **kwargs)

        self.header_name = header_name
        self.text_var = tk.StringVar()
        self.text_var.set("No file selected")

        self.header = customtkinter.CTkLabel(
            self, text=self.header_name, font=customtkinter.CTkFont(size=15))
        self.header.grid(row=0, column=0, padx=(0, 0), pady=(5, 5))

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
            self, text="Decompress", width=100)
        self.decomp_button.grid(row=2, column=1, padx=(5, 0), pady=(0, 5))

        self.comp_button = customtkinter.CTkButton(
            self, text="Compress", width=100)
        self.comp_button.grid(row=2, column=2, sticky="e",
                              padx=(10, 20), pady=(0, 5))

    def get_file(self):
        filetypes = (("Text files", "*.txt"), ("Bin files", "*.bin"))
        filename = fd.askopenfilename(
            title="Select a file", filetypes=filetypes)
        self.text_var.set(filename)
