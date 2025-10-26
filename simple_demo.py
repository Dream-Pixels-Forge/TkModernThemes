import customtkinter as ctk

class SimpleDemo(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("Simple CustomTkinter Demo")
        self.geometry("800x600")
        
        # Set appearance mode (light/dark)
        ctk.set_appearance_mode("dark")
        
        # Create main container
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # Create sidebar
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew")
        
        # Sidebar title
        self.logo_label = ctk.CTkLabel(
            self.sidebar, 
            text="Simple Demo",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.logo_label.pack(padx=20, pady=(20, 10))
        
        # Appearance mode
        self.appearance_mode_label = ctk.CTkLabel(
            self.sidebar, 
            text="Appearance Mode:",
            font=ctk.CTkFont(weight="bold")
        )
        self.appearance_mode_label.pack(padx=20, pady=(20, 0))
        
        self.appearance_mode_menu = ctk.CTkOptionMenu(
            self.sidebar, 
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode
        )
        self.appearance_mode_menu.pack(padx=20, pady=(10, 10))
        
        # Main content area
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)
        
        # Title
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="Welcome to CustomTkinter",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.title_label.pack(padx=20, pady=20)
        
        # Button
        self.button = ctk.CTkButton(
            self.main_frame,
            text="Click Me!",
            command=self.button_clicked
        )
        self.button.pack(pady=10)
        
        # Entry
        self.entry = ctk.CTkEntry(
            self.main_frame,
            placeholder_text="Type something..."
        )
        self.entry.pack(pady=10, padx=20, fill="x")
        
        # Checkbox
        self.checkbox = ctk.CTkCheckBox(
            self.main_frame,
            text="Check me"
        )
        self.checkbox.pack(pady=10)
        
        # Slider
        self.slider = ctk.CTkSlider(
            self.main_frame,
            from_=0,
            to=100
        )
        self.slider.pack(pady=10, padx=20, fill="x")
        self.slider.set(50)
        
        # Status bar
        self.status_bar = ctk.CTkLabel(
            self,
            text="Ready",
            anchor="w",
            font=ctk.CTkFont(size=10)
        )
        self.status_bar.grid(row=1, column=0, columnspan=2, padx=20, pady=(0, 10), sticky="ew")
    
    def button_clicked(self):
        text = self.entry.get()
        checked = "checked" if self.checkbox.get() else "not checked"
        self.status_bar.configure(
            text=f"Button clicked! Entry: '{text}'. Checkbox is {checked}. "
                 f"Slider value: {int(self.slider.get())}"
        )
    
    def change_appearance_mode(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode.lower())

if __name__ == "__main__":
    app = SimpleDemo()
    app.mainloop()
