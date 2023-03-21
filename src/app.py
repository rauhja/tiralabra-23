import customtkinter
from gui.comp_frame import CompFrame

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Lossless Compression Comparison")
        self.geometry("800x600")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(
            self.navigation_frame, text="Lossless \n Compression \n Comparison",
            font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.compress_button = customtkinter.CTkButton(self.navigation_frame,
            corner_radius=0, height=40, border_spacing=10, text="Compress/Decompress",
            fg_color="transparent", text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"), command=self.compress_button_event)
        self.compress_button.grid(row=1, column=0, sticky="ew")

        self.analysis_button = customtkinter.CTkButton(self.navigation_frame,
            corner_radius=0, height=40, border_spacing=10, text="Run Analysis",
            fg_color="transparent", text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"), command=self.analysis_button_event)
        self.analysis_button.grid(row=2, column=0, sticky="ew")

        self.about_button = customtkinter.CTkButton(self.navigation_frame,
            corner_radius=0, height=40, border_spacing=10, text="About",
            fg_color="transparent", text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"), command=self.about_button_event)
        self.about_button.grid(row=3, column=0, sticky="ew")

        self.quit_button = customtkinter.CTkButton(self.navigation_frame,
            corner_radius=0, height=40, border_spacing=10, text="Quit",
            fg_color="#FF2511", text_color="white", hover_color=("#BA0F30", "#FF2511"),
            command=self.quit_button_event)
        self.quit_button.grid(row=5, column=0, sticky="nsew")

        self.compressed_frame = CompFrame(self)
        self.compressed_frame.grid(row=0, column=1, padx=20, pady=0)

        self.analysis_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")

        self.about_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")

    def select_frame_by_name(self, name):
        if name == "compressed_frame":
            self.compressed_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.compressed_frame.grid_forget()
        if name == "analysis_frame":
            self.analysis_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.analysis_frame.grid_forget()
        if name == "about_frame":
            self.about_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.about_frame.grid_forget()

    def compress_button_event(self):
        self.select_frame_by_name("compress_frame")

    def analysis_button_event(self):
        self.select_frame_by_name("analysis_frame")

    def about_button_event(self):
        self.select_frame_by_name("about_frame")

    def quit_button_event(self):
        self.quit()

if __name__ == "__main__":
    app = App()
    app.mainloop()
