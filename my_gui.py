import customtkinter
import keyboard

from main import get_gpt_ans, get_pattern_list, add_pattern

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="ChatGPT GUI",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))

        self.patterns = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                    values=get_pattern_list(),
                                                    command=self.add_pattern)
        self.patterns.grid(row=3, column=0, padx=20, pady=(10, 20))

        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                               values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        self.entry = customtkinter.CTkEntry(self, placeholder_text="Write ur question...")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2,
                                                     text_color=("gray10", "#DCE4EE"), text='Send',
                                                     command=self.own_func)
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.textbox = customtkinter.CTkTextbox(self, width=500)
        self.textbox.grid(row=0, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")


        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def add_pattern(self, pattern: str = '+ add new template'):
        if pattern == '+ add new template':
            self.new_pattern_frame = customtkinter.CTkToplevel()
            self.new_pattern_frame.geometry("500x400")
            self.entry_title_patt = customtkinter.CTkEntry(self.new_pattern_frame,
                                                           placeholder_text="Type a template title", width=400)
            self.entry_title_patt.grid(row=1, column=1, columnspan=2, padx=(20, 0),
                                       pady=(20, 20), sticky="nsew")

            self.entry_patt = customtkinter.CTkEntry(self.new_pattern_frame,
                                                     placeholder_text="Type a template in format (example: Describe ur trip to [prompt])",
                                                     width=400)
            self.entry_patt.grid(row=2, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

            self.submit_button = customtkinter.CTkButton(self.new_pattern_frame, text='Save', bg_color='blue',
                                                         command=self.submit_pattern)
            self.submit_button.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

            self.new_pattern_frame.attributes('-topmost', True)

    def own_func(self):
        text = self.entry.get()

        self.entry.delete(first_index=0, last_index=len(text) + 1)

        template = self.patterns.get()

        answer = get_gpt_ans(text, template)

        self.textbox.insert('0.0', answer)

    def submit_pattern(self):
        add_pattern(self.entry_title_patt.get(), self.entry_patt.get())
        self.new_pattern_frame.withdraw()


def main():
    App().mainloop()


if __name__ == "__main__":
    keyboard.add_hotkey('ctrl+alt+a', main)
    keyboard.wait()
