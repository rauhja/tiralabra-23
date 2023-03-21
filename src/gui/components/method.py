import customtkinter

class Method(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.header = customtkinter.CTkLabel(
            self, text="Method", font=customtkinter.CTkFont(size=15))
        self.header.grid(row=0, column=0, padx=(0, 0), pady=(5, 5))

        self.method_huff = customtkinter.CTkRadioButton(
            self, text="Huffman", value=1)
        self.method_huff.grid(row=1, column=0, sticky="w",
                              padx=(10, 0), pady=(0, 5))

        self.method_lzw = customtkinter.CTkRadioButton(
            self, text="LZW", value=2)
        self.method_lzw.grid(row=2, column=0, sticky="w",
                             padx=(10, 0), pady=(0, 5))
