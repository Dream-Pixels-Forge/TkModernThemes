"""
TkModernThemes - Modern Tkinter Theme Library 2025
A collection of 6 contemporary themes following latest design trends

Installation:
    1. Create a directory named 'TkModernThemes'
    2. Save this file as '__init__.py' inside that directory
    3. Place the directory in your project or Python path

Usage:
    import TkModernThemes as TKMT
    
    root = tk.Tk()
    theme = TKMT.ThemedTk(root)
    theme.set_theme("glassmorphism")
"""

import tkinter as tk
from tkinter import ttk

__version__ = "1.0.0"
__author__ = "TkModernThemes"
__all__ = ["ThemedTk", "THEMES", "create_card", "create_demo"]


# Theme definitions with 2025 design trends
THEMES = {
    "glassmorphism": {
        "name": "Glassmorphism Dark",
        "bg": "#0f0f1e",
        "fg": "#e0e0ff",
        "accent": "#6366f1",
        "secondary": "#8b5cf6",
        "surface": "#1a1a2e",
        "border": "#4338ca",
        "hover": "#4f46e5",
        "font": ("SF Pro Display", 10),
        "heading_font": ("SF Pro Display", 14, "bold")
    },
    "neomorphism": {
        "name": "Neomorphism Light",
        "bg": "#e0e5ec",
        "fg": "#2c3e50",
        "accent": "#6c5ce7",
        "secondary": "#a29bfe",
        "surface": "#e0e5ec",
        "border": "#a0a0a0",
        "hover": "#d1d6dd",
        "font": ("Inter", 10),
        "heading_font": ("Inter", 14, "bold")
    },
    "cyberpunk": {
        "name": "Cyberpunk Neon",
        "bg": "#0a0e27",
        "fg": "#00ff9f",
        "accent": "#ff2a6d",
        "secondary": "#05d9e8",
        "surface": "#1a1f3a",
        "border": "#d1f7ff",
        "hover": "#ff2a6d",
        "font": ("JetBrains Mono", 10),
        "heading_font": ("JetBrains Mono", 14, "bold")
    },
    "aurora": {
        "name": "Aurora Gradient",
        "bg": "#0f1419",
        "fg": "#e6edf3",
        "accent": "#ff6b9d",
        "secondary": "#c38fff",
        "surface": "#1c2128",
        "border": "#7ee787",
        "hover": "#ffa198",
        "font": ("Segoe UI", 10),
        "heading_font": ("Segoe UI", 14, "bold")
    },
    "minimal_zen": {
        "name": "Minimal Zen",
        "bg": "#fafafa",
        "fg": "#1a1a1a",
        "accent": "#2dd4bf",
        "secondary": "#14b8a6",
        "surface": "#ffffff",
        "border": "#d4d4d4",
        "hover": "#f5f5f5",
        "font": ("Helvetica Neue", 10),
        "heading_font": ("Helvetica Neue", 14, "bold")
    },
    "dark_pro": {
        "name": "Dark Pro",
        "bg": "#1e1e1e",
        "fg": "#d4d4d4",
        "accent": "#007acc",
        "secondary": "#4fc3f7",
        "surface": "#252526",
        "border": "#3e3e42",
        "hover": "#2d2d30",
        "font": ("Consolas", 10),
        "heading_font": ("Consolas", 14, "bold")
    }
}


class ThemedTk:
    """Main theme manager class for Tkinter applications"""
    
    def __init__(self, root):
        """
        Initialize the theme manager
        
        Args:
            root: Tkinter root window or Toplevel widget
        """
        self.root = root
        self.current_theme = None
        self.style = ttk.Style()
        self._theme_data = None
        
    def set_theme(self, theme_name):
        """
        Apply a theme to the Tkinter window
        
        Args:
            theme_name: Name of the theme to apply (e.g., "glassmorphism")
            
        Raises:
            ValueError: If theme name is not found
        """
        if theme_name not in THEMES:
            available = ", ".join(THEMES.keys())
            raise ValueError(f"Theme '{theme_name}' not found. Available themes: {available}")
        
        theme = THEMES[theme_name]
        self.current_theme = theme_name
        self._theme_data = theme
        
        # Configure root window
        self.root.configure(bg=theme["bg"])
        
        # Configure ttk styles
        self.style.theme_use('clam')
        
        # Configure base elements
        self.style.configure(".", 
                           background=theme["bg"],
                           foreground=theme["fg"],
                           fieldbackground=theme["surface"],
                           bordercolor=theme["border"],
                           font=theme["font"])
        
        # TFrame
        self.style.configure("TFrame",
                           background=theme["bg"],
                           borderwidth=0)
        
        self.style.configure("Card.TFrame",
                           background=theme["surface"],
                           relief="flat",
                           borderwidth=1)
        
        # TLabel
        self.style.configure("TLabel",
                           background=theme["bg"],
                           foreground=theme["fg"],
                           font=theme["font"])
        
        self.style.configure("Heading.TLabel",
                           font=theme["heading_font"],
                           foreground=theme["accent"])
        
        self.style.configure("Card.TLabel",
                           background=theme["surface"],
                           foreground=theme["fg"])
        
        # TButton
        self.style.configure("TButton",
                           background=theme["accent"],
                           foreground="#ffffff",
                           borderwidth=0,
                           focuscolor=theme["accent"],
                           padding=(20, 10),
                           font=theme["font"])
        
        self.style.map("TButton",
                      background=[("active", theme["hover"]),
                                ("pressed", theme["secondary"])],
                      relief=[("pressed", "flat")])
        
        # Secondary button
        self.style.configure("Secondary.TButton",
                           background=theme["surface"],
                           foreground=theme["fg"],
                           borderwidth=1,
                           bordercolor=theme["border"])
        
        self.style.map("Secondary.TButton",
                      background=[("active", theme["hover"])],
                      bordercolor=[("active", theme["accent"])])
        
        # TEntry
        self.style.configure("TEntry",
                           fieldbackground=theme["surface"],
                           foreground=theme["fg"],
                           bordercolor=theme["border"],
                           lightcolor=theme["border"],
                           darkcolor=theme["border"],
                           insertcolor=theme["fg"],
                           padding=10)
        
        self.style.map("TEntry",
                      fieldbackground=[("focus", theme["surface"])],
                      bordercolor=[("focus", theme["accent"])])
        
        # TCheckbutton
        self.style.configure("TCheckbutton",
                           background=theme["bg"],
                           foreground=theme["fg"],
                           indicatorcolor=theme["surface"],
                           bordercolor=theme["border"])
        
        self.style.map("TCheckbutton",
                      indicatorcolor=[("selected", theme["accent"])],
                      background=[("active", theme["bg"])])
        
        # TRadiobutton
        self.style.configure("TRadiobutton",
                           background=theme["bg"],
                           foreground=theme["fg"],
                           indicatorcolor=theme["surface"])
        
        self.style.map("TRadiobutton",
                      indicatorcolor=[("selected", theme["accent"])],
                      background=[("active", theme["bg"])])
        
        # TCombobox
        self.style.configure("TCombobox",
                           fieldbackground=theme["surface"],
                           background=theme["surface"],
                           foreground=theme["fg"],
                           bordercolor=theme["border"],
                           arrowcolor=theme["fg"],
                           padding=10)
        
        self.style.map("TCombobox",
                      fieldbackground=[("focus", theme["surface"])],
                      bordercolor=[("focus", theme["accent"])])
        
        # Progressbar
        self.style.configure("TProgressbar",
                           background=theme["accent"],
                           troughcolor=theme["surface"],
                           bordercolor=theme["border"],
                           lightcolor=theme["accent"],
                           darkcolor=theme["accent"],
                           thickness=8)
        
        # Scale
        self.style.configure("TScale",
                           background=theme["bg"],
                           troughcolor=theme["surface"],
                           bordercolor=theme["border"],
                           sliderthickness=20)
        
        # Scrollbar
        self.style.configure("TScrollbar",
                           background=theme["surface"],
                           troughcolor=theme["bg"],
                           bordercolor=theme["border"],
                           arrowcolor=theme["fg"])
        
        self.style.map("TScrollbar",
                      background=[("active", theme["accent"])])
        
        # Notebook (Tabs)
        self.style.configure("TNotebook",
                           background=theme["bg"],
                           bordercolor=theme["border"],
                           tabmargins=[2, 5, 2, 0])
        
        self.style.configure("TNotebook.Tab",
                           background=theme["surface"],
                           foreground=theme["fg"],
                           padding=[20, 10],
                           bordercolor=theme["border"])
        
        self.style.map("TNotebook.Tab",
                      background=[("selected", theme["accent"])],
                      foreground=[("selected", "#ffffff")],
                      expand=[("selected", [1, 1, 1, 0])])
        
    def get_theme_list(self):
        """Return list of available theme names"""
        return list(THEMES.keys())
    
    def get_current_theme(self):
        """Return current theme name"""
        return self.current_theme
    
    def get_theme_colors(self, theme_name=None):
        """
        Get color dictionary for a theme
        
        Args:
            theme_name: Name of theme (uses current theme if None)
            
        Returns:
            Dictionary of theme colors
        """
        if theme_name is None:
            return self._theme_data
        return THEMES.get(theme_name)
    
    def create_card(self, parent, **kwargs):
        """
        Create a styled card frame
        
        Args:
            parent: Parent widget
            **kwargs: Additional arguments passed to ttk.Frame
            
        Returns:
            ttk.Frame with Card style
        """
        card = ttk.Frame(parent, style="Card.TFrame", **kwargs)
        return card


def create_card(parent, **kwargs):
    """
    Utility function to create a styled card frame
    
    Args:
        parent: Parent widget
        **kwargs: Additional arguments passed to ttk.Frame
        
    Returns:
        ttk.Frame with Card style
    """
    return ttk.Frame(parent, style="Card.TFrame", **kwargs)


def create_demo():
    """Launch a demo application showcasing all themes"""
    root = tk.Tk()
    root.title("TkModernThemes Demo - 2025 Edition")
    root.geometry("900x700")
    
    # Initialize theme manager
    theme = ThemedTk(root)
    theme.set_theme("glassmorphism")
    
    # Main container with padding
    main_frame = ttk.Frame(root, padding=30)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Header
    header = ttk.Label(main_frame, 
                       text="🎨 TkModernThemes - 2025 Edition",
                       style="Heading.TLabel")
    header.pack(pady=(0, 20))
    
    # Theme selector
    selector_frame = ttk.Frame(main_frame)
    selector_frame.pack(fill=tk.X, pady=(0, 20))
    
    ttk.Label(selector_frame, text="Select Theme:").pack(side=tk.LEFT, padx=(0, 10))
    
    theme_var = tk.StringVar(value="glassmorphism")
    theme_combo = ttk.Combobox(selector_frame, 
                               textvariable=theme_var,
                               values=theme.get_theme_list(),
                               state="readonly",
                               width=20)
    theme_combo.pack(side=tk.LEFT)
    
    def change_theme(event=None):
        theme.set_theme(theme_var.get())
        create_demo_components()
    
    theme_combo.bind("<<ComboboxSelected>>", change_theme)
    
    # Demo components container
    demo_container = ttk.Frame(main_frame)
    demo_container.pack(fill=tk.BOTH, expand=True)
    
    def create_demo_components():
        for widget in demo_container.winfo_children():
            widget.destroy()
        
        # Card 1: Buttons
        card1 = theme.create_card(demo_container, padding=20)
        card1.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Label(card1, text="Buttons", style="Card.TLabel", 
                 font=("", 12, "bold")).pack(anchor=tk.W, pady=(0, 10))
        
        btn_frame = ttk.Frame(card1)
        btn_frame.pack(fill=tk.X)
        
        ttk.Button(btn_frame, text="Primary Action").pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(btn_frame, text="Secondary", style="Secondary.TButton").pack(side=tk.LEFT)
        
        # Card 2: Input Fields
        card2 = theme.create_card(demo_container, padding=20)
        card2.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Label(card2, text="Input Fields", style="Card.TLabel",
                 font=("", 12, "bold")).pack(anchor=tk.W, pady=(0, 10))
        
        entry_frame = ttk.Frame(card2)
        entry_frame.pack(fill=tk.X)
        
        ttk.Label(entry_frame, text="Email:", style="Card.TLabel").grid(row=0, column=0, 
                                                                         sticky=tk.W, pady=5)
        ttk.Entry(entry_frame, width=30).grid(row=0, column=1, sticky=tk.W, padx=10)
        
        ttk.Label(entry_frame, text="Password:", style="Card.TLabel").grid(row=1, column=0,
                                                                            sticky=tk.W, pady=5)
        ttk.Entry(entry_frame, width=30, show="*").grid(row=1, column=1, sticky=tk.W, padx=10)
        
        # Card 3: Selections
        card3 = theme.create_card(demo_container, padding=20)
        card3.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Label(card3, text="Selections", style="Card.TLabel",
                 font=("", 12, "bold")).pack(anchor=tk.W, pady=(0, 10))
        
        check_frame = ttk.Frame(card3)
        check_frame.pack(fill=tk.X)
        
        ttk.Checkbutton(check_frame, text="Enable notifications").pack(anchor=tk.W, pady=3)
        ttk.Checkbutton(check_frame, text="Dark mode").pack(anchor=tk.W, pady=3)
        
        ttk.Separator(check_frame, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=10)
        
        radio_var = tk.StringVar(value="option1")
        ttk.Radiobutton(check_frame, text="Option 1", variable=radio_var, 
                       value="option1").pack(anchor=tk.W, pady=3)
        ttk.Radiobutton(check_frame, text="Option 2", variable=radio_var,
                       value="option2").pack(anchor=tk.W, pady=3)
        
        # Card 4: Progress & Scale
        card4 = theme.create_card(demo_container, padding=20)
        card4.pack(fill=tk.X)
        
        ttk.Label(card4, text="Progress & Controls", style="Card.TLabel",
                 font=("", 12, "bold")).pack(anchor=tk.W, pady=(0, 10))
        
        progress = ttk.Progressbar(card4, length=300, mode='determinate', value=65)
        progress.pack(pady=5, anchor=tk.W)
        
        ttk.Scale(card4, from_=0, to=100, orient=tk.HORIZONTAL, length=300).pack(pady=5, anchor=tk.W)
    
    create_demo_components()
    
    root.mainloop()


# Allow running as standalone demo
if __name__ == "__main__":
    create_demo()