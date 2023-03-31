import customtkinter


class AboutFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_rowconfigure(1)
        self.grid_columnconfigure((0, 1), weight=1)

        self.header = customtkinter.CTkLabel(
            self, text="About", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.header.grid(row=0, column=0, columnspan=2,
                         padx=(10, 10), pady=(10, 10))

        self.text_label = customtkinter.CTkLabel(self, text="This is a lab project for the course Data Structures and Algorithms at the University of Helsinki. The goal is to compare two lossless data compression algorithms: Huffman coding and Lempel-Ziv-Welch coding.",
                                                 anchor="n", justify="left", wraplength=500)
        self.text_label.grid(row=1, column=0, columnspan=2,
                             padx=(10, 10), pady=(10, 10))
