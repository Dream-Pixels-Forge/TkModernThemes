import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

class ModernThemesApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("Modern Themes Demo")
        self.geometry("1000x700")
        
        # Set appearance mode and color theme
        ctk.set_appearance_mode("dark")  # Can be "light" or "dark"
        ctk.set_default_color_theme("blue")  # Default theme
        
        # Create main container
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Create sidebar
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar.grid_rowconfigure(4, weight=1)
        
        # Sidebar title
        self.logo_label = ctk.CTkLabel(
            self.sidebar, 
            text="Modern Themes",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        # Theme selector
        self.theme_label = ctk.CTkLabel(
            self.sidebar, 
            text="Select Theme:",
            font=ctk.CTkFont(weight="bold")
        )
        self.theme_label.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="w")
        
        # Only using the default 'blue' theme for maximum compatibility
        self.theme_var = ctk.StringVar(value="blue")
        self.theme_menu = ctk.CTkOptionMenu(
            self.sidebar, 
            values=["blue"],  # Only the default theme to ensure compatibility
            command=self.change_theme,
            variable=self.theme_var
        )
        self.theme_menu.configure(state="disabled")  # Disable since we only have one theme
        self.theme_menu.grid(row=2, column=0, padx=20, pady=(0, 10), sticky="ew")
        
        # Appearance mode
        self.appearance_mode_label = ctk.CTkLabel(
            self.sidebar, 
            text="Appearance Mode:",
            font=ctk.CTkFont(weight="bold")
        )
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0), sticky="s")
        
        self.appearance_mode_menu = ctk.CTkOptionMenu(
            self.sidebar, 
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode
        )
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=(10, 10), sticky="s")
        
        # Main content area
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)
        
        # Title
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="Modern UI Components",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.title_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
        
        # Create tabs
        self.tabview = ctk.CTkTabview(self.main_frame)
        self.tabview.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="nsew")
        
        # Add tabs
        self.tabview.add("Buttons")
        self.tabview.add("Inputs")
        self.tabview.add("Sliders")
        
        # Buttons tab
        self.tabview.tab("Buttons").grid_columnconfigure(0, weight=1)
        
        # Regular button
        self.button_1 = ctk.CTkButton(
            self.tabview.tab("Buttons"), 
            text="Primary Button"
        )
        self.button_1.grid(row=0, column=0, padx=20, pady=10, sticky="ew")
        
        # Secondary button
        self.button_2 = ctk.CTkButton(
            self.tabview.tab("Buttons"),
            text="Secondary Button",
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE")
        )
        self.button_2.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        
        # Success button
        self.button_3 = ctk.CTkButton(
            self.tabview.tab("Buttons"),
            text="Success",
            fg_color="#2ecc71",
            hover_color="#27ae60"
        )
        self.button_3.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        
        # Inputs tab
        self.tabview.tab("Inputs").grid_columnconfigure(0, weight=1)
        
        # Entry
        self.entry = ctk.CTkEntry(
            self.tabview.tab("Inputs"),
            placeholder_text="Enter text here"
        )
        self.entry.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        
        # Checkboxes
        self.checkbox_1 = ctk.CTkCheckBox(
            self.tabview.tab("Inputs"),
            text="Option 1"
        )
        self.checkbox_1.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        
        self.checkbox_2 = ctk.CTkCheckBox(
            self.tabview.tab("Inputs"),
            text="Option 2"
        )
        self.checkbox_2.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        
        # Radio buttons
        self.radio_var = tk.IntVar(value=0)
        
        self.radio_1 = ctk.CTkRadioButton(
            self.tabview.tab("Inputs"),
            text="Radio 1",
            variable=self.radio_var,
            value=0
        )
        self.radio_1.grid(row=3, column=0, padx=20, pady=10, sticky="w")
        
        self.radio_2 = ctk.CTkRadioButton(
            self.tabview.tab("Inputs"),
            text="Radio 2",
            variable=self.radio_var,
            value=1
        )
        self.radio_2.grid(row=4, column=0, padx=20, pady=10, sticky="w")
        
        # Sliders tab
        self.tabview.tab("Sliders").grid_columnconfigure(0, weight=1)
        
        # Slider
        self.slider = ctk.CTkSlider(
            self.tabview.tab("Sliders"),
            from_=0,
            to=100,
            number_of_steps=10
        )
        self.slider.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        
        # Progress bar
        self.progressbar = ctk.CTkProgressBar(self.tabview.tab("Sliders"))
        self.progressbar.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        self.progressbar.set(0.7)  # Set progress to 70%
        
        # Switch
        self.switch = ctk.CTkSwitch(
            self.tabview.tab("Sliders"),
            text="Enable Feature"
        )
        self.switch.grid(row=2, column=0, padx=20, pady=20, sticky="w")
        
        # Add some sample text
        self.textbox = ctk.CTkTextbox(self.main_frame, height=100)
        self.textbox.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="nsew")
        self.textbox.insert("0.0", "This is a sample text area.\n\n" + 
                               "CustomTkinter provides modern looking widgets " +
                               "that can be easily themed and customized.")
        
        # Status bar
        self.status_bar = ctk.CTkLabel(
            self,
            text="Ready",
            anchor="w",
            font=ctk.CTkFont(size=10)
        )
        self.status_bar.grid(row=1, column=0, columnspan=2, padx=20, pady=(0, 10), sticky="ew")
    
    def change_theme(self, new_theme):
        ctk.set_default_color_theme(new_theme.lower())
        self.status_bar.configure(text=f"Theme changed to: {new_theme}")
    
    def change_appearance_mode(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode.lower())
        self.status_bar.configure(text=f"Appearance mode changed to: {new_appearance_mode}")

if __name__ == "__main__":
    app = ModernThemesApp()
    app.mainloop()
