import customtkinter
import tkinter as tk
import os
from tkinter import filedialog as fd
from services.compressservice import CompressManagement


class AnalysisFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_rowconfigure(1)
        self.grid_columnconfigure(1, weight=1)

        self.text_var = tk.StringVar()
        self.text_var.set("No file selected")

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

    def get_file(self):
        filetypes = (("Text files", "*.txt"),
                     ("Compressed files", "*.huff *.lzw"))
        self.file_path = fd.askopenfilename(
            title="Select a file", filetypes=filetypes)
        self.text_var.set(self.file_path)

    def _handle_run_analysis(self):
        CompressManagement().run_analysis(self.file_path)
