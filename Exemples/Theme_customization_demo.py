"""
Theme Customization Example for TkModernThemes

This example demonstrates how to customize themes dynamically
after initialization, allowing users to modify colors and properties.
"""

import tkinter as tk
from tkinter import ttk
import TkModernThemes as TKMT


class ThemeCustomizationDemo:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Theme Customization Demo - TkModernThemes")
        self.root.geometry("1000x700")
        
        # Initialize theme manager
        self.theme = TKMT.ThemedTk(self.root)
        self.theme.set_theme("nexus_dark")  # Start with a default theme
        
        # Store original theme for resetting
        self.original_theme = self.theme.get_theme_colors().copy()
        
        # Create the UI
        self.create_ui()
    
    def create_ui(self):
        """Create the user interface"""
        # Main container
        main_container = ttk.Frame(self.root)
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title = ttk.Label(main_container, text="Theme Customization Demo", style="Heading.TLabel")
        title.pack(pady=(0, 20))
        
        # Create main layout with two sections
        main_frame = ttk.Frame(main_container)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left side - Controls
        control_frame = self.theme.create_card(main_frame, padding=15)
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        
        # Theme selector
        ttk.Label(control_frame, text="Select Base Theme:", style="Card.TLabel").pack(anchor=tk.W, pady=(0, 5))
        self.theme_var = tk.StringVar(value="nexus_dark")
        theme_selector = ttk.Combobox(
            control_frame,
            textvariable=self.theme_var,
            values=self.theme.get_theme_list(),
            state="readonly"
        )
        theme_selector.pack(fill=tk.X, pady=(0, 15))
        theme_selector.bind("<<ComboboxSelected>>", self.on_theme_change)
        
        # Color customization section
        ttk.Label(control_frame, text="Customize Colors:", style="Heading.TLabel").pack(anchor=tk.W, pady=(10, 10))
        
        # Background color
        bg_frame = ttk.Frame(control_frame)
        bg_frame.pack(fill=tk.X, pady=2)
        ttk.Label(bg_frame, text="BG:", style="Card.TLabel").pack(side=tk.LEFT)
        self.bg_color_var = tk.StringVar(value=self.original_theme['bg'])
        bg_entry = ttk.Entry(bg_frame, textvariable=self.bg_color_var, width=10)
        bg_entry.pack(side=tk.LEFT, padx=(5, 0))
        ttk.Button(bg_frame, text="Change", command=lambda: self.update_color('bg', self.bg_color_var.get())).pack(side=tk.LEFT, padx=(5, 0))
        
        # Foreground color
        fg_frame = ttk.Frame(control_frame)
        fg_frame.pack(fill=tk.X, pady=2)
        ttk.Label(fg_frame, text="FG:", style="Card.TLabel").pack(side=tk.LEFT)
        self.fg_color_var = tk.StringVar(value=self.original_theme['fg'])
        fg_entry = ttk.Entry(fg_frame, textvariable=self.fg_color_var, width=10)
        fg_entry.pack(side=tk.LEFT, padx=(5, 0))
        ttk.Button(fg_frame, text="Change", command=lambda: self.update_color('fg', self.fg_color_var.get())).pack(side=tk.LEFT, padx=(5, 0))
        
        # Accent color
        accent_frame = ttk.Frame(control_frame)
        accent_frame.pack(fill=tk.X, pady=2)
        ttk.Label(accent_frame, text="Accent:", style="Card.TLabel").pack(side=tk.LEFT)
        self.accent_color_var = tk.StringVar(value=self.original_theme['accent'])
        accent_entry = ttk.Entry(accent_frame, textvariable=self.accent_color_var, width=10)
        accent_entry.pack(side=tk.LEFT, padx=(5, 0))
        ttk.Button(accent_frame, text="Change", command=lambda: self.update_color('accent', self.accent_color_var.get())).pack(side=tk.LEFT, padx=(5, 0))
        
        # Surface color
        surface_frame = ttk.Frame(control_frame)
        surface_frame.pack(fill=tk.X, pady=2)
        ttk.Label(surface_frame, text="Surface:", style="Card.TLabel").pack(side=tk.LEFT)
        self.surface_color_var = tk.StringVar(value=self.original_theme['surface'])
        surface_entry = ttk.Entry(surface_frame, textvariable=self.surface_color_var, width=10)
        surface_entry.pack(side=tk.LEFT, padx=(5, 0))
        ttk.Button(surface_frame, text="Change", command=lambda: self.update_color('surface', self.surface_color_var.get())).pack(side=tk.LEFT, padx=(5, 0))
        
        # Reset button
        ttk.Button(control_frame, text="Reset to Original", command=self.reset_theme).pack(pady=20)
        
        # Preview area
        preview_frame = self.theme.create_card(main_frame, padding=20)
        preview_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Preview title
        ttk.Label(preview_frame, text="Theme Preview", style="Heading.TLabel").pack(anchor=tk.W, pady=(0, 20))
        
        # Create sample widgets for preview
        self.create_preview_widgets(preview_frame)
    
    def create_preview_widgets(self, parent):
        """Create sample widgets to preview the theme"""
        # Button examples
        button_frame = ttk.Frame(parent)
        button_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(button_frame, text="Buttons:", style="Card.TLabel").pack(anchor=tk.W)
        ttk.Button(button_frame, text="Primary Button").pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(button_frame, text="Secondary Button", style="Secondary.TButton").pack(side=tk.LEFT)
        
        # Entry example
        entry_frame = ttk.Frame(parent)
        entry_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(entry_frame, text="Entry Field:", style="Card.TLabel").pack(anchor=tk.W)
        ttk.Entry(entry_frame).pack(fill=tk.X, pady=(5, 0))
        
        # Checkboxes
        checkbox_frame = ttk.Frame(parent)
        checkbox_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(checkbox_frame, text="Checkboxes:", style="Card.TLabel").pack(anchor=tk.W)
        ttk.Checkbutton(checkbox_frame, text="Option 1").pack(anchor=tk.W)
        ttk.Checkbutton(checkbox_frame, text="Option 2").pack(anchor=tk.W)
        
        # Progress bar
        progress_frame = ttk.Frame(parent)
        progress_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(progress_frame, text="Progress:", style="Card.TLabel").pack(anchor=tk.W)
        self.progress = ttk.Progressbar(progress_frame, mode='determinate', value=75)
        self.progress.pack(fill=tk.X, pady=(5, 0))
        
        # Card example
        card_example = self.theme.create_card(parent, padding=15)
        card_example.pack(fill=tk.X, pady=10)
        
        ttk.Label(card_example, text="Card Component", style="Heading.TLabel").pack(anchor=tk.W)
        ttk.Label(card_example, text="This is a card with custom styling", style="Card.TLabel").pack(anchor=tk.W, pady=5)
    
    def on_theme_change(self, event):
        """Handle theme change"""
        theme_name = self.theme_var.get()
        self.theme.set_theme(theme_name)
        
        # Update color variables to match the new theme
        theme_colors = self.theme.get_theme_colors()
        self.original_theme = theme_colors.copy()
        
        self.bg_color_var.set(theme_colors['bg'])
        self.fg_color_var.set(theme_colors['fg'])
        self.accent_color_var.set(theme_colors['accent'])
        self.surface_color_var.set(theme_colors['surface'])
    
    def update_color(self, color_type, color_value):
        """Update a specific color in the current theme"""
        try:
            # Validate the color
            self.root.winfo_rgb(color_value)
            
            # Update the theme's color
            current_theme = self.theme.current_theme
            TKMT.THEMES[current_theme][color_type] = color_value
            
            # Reapply the theme to see changes
            self.theme.set_theme(current_theme)
            
        except tk.TclError:
            # Invalid color, show error
            error_window = tk.Toplevel(self.root)
            error_window.title("Invalid Color")
            error_window.geometry("300x100")
            ttk.Label(error_window, text=f"Invalid color value: {color_value}").pack(pady=20)
            ttk.Button(error_window, text="OK", command=error_window.destroy).pack(pady=5)
    
    def reset_theme(self):
        """Reset to the original theme colors"""
        current_theme = self.theme.current_theme
        for key, value in self.original_theme.items():
            TKMT.THEMES[current_theme][key] = value
        
        # Reapply the theme
        self.theme.set_theme(current_theme)
        
        # Update the color variables
        self.bg_color_var.set(self.original_theme['bg'])
        self.fg_color_var.set(self.original_theme['fg'])
        self.accent_color_var.set(self.original_theme['accent'])
        self.surface_color_var.set(self.original_theme['surface'])
    
    def run(self):
        """Run the application"""
        self.root.mainloop()


if __name__ == "__main__":
    app = ThemeCustomizationDemo()
    app.run()