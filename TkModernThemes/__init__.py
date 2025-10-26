"""
TkModernThemes - Modern Tkinter Theme Library 2025
Inspired by PySide6 and modern web design (Nexus UI)
A collection of contemporary themes with advanced styling

Installation:
    1. Create a directory named 'TkModernThemes'
    2. Save this file as '__init__.py' inside that directory
    3. Place the directory in your project or Python path

Usage:
    import TkModernThemes as TKMT
    
    root = tk.Tk()
    theme = TKMT.ThemedTk(root)
    theme.set_theme("nexus_dark")
"""

import tkinter as tk
from tkinter import ttk

__version__ = "2.0.0"
__author__ = "TkModernThemes"
__all__ = ["ThemedTk", "THEMES", "create_card", "create_sidebar", "create_demo"]


# Enhanced theme definitions with PySide6 and Nexus UI inspiration
THEMES = {
    "nexus_dark": {
        "name": "Nexus Dark",
        "bg": "#0a0a0a",
        "fg": "#e4e4e7",
        "accent": "#3b82f6",
        "secondary": "#8b5cf6",
        "surface": "#18181b",
        "surface_variant": "#27272a",
        "border": "#3f3f46",
        "hover": "#1e293b",
        "success": "#22c55e",
        "warning": "#f59e0b",
        "error": "#ef4444",
        "font": ("Segoe UI", 9),
        "heading_font": ("Segoe UI", 16, "bold"),
        "radius": 8
    },
    "nexus_light": {
        "name": "Nexus Light",
        "bg": "#ffffff",
        "fg": "#18181b",
        "accent": "#2563eb",
        "secondary": "#7c3aed",
        "surface": "#f4f4f5",
        "surface_variant": "#e4e4e7",
        "border": "#d4d4d8",
        "hover": "#f1f5f9",
        "success": "#16a34a",
        "warning": "#ea580c",
        "error": "#dc2626",
        "font": ("Segoe UI", 9),
        "heading_font": ("Segoe UI", 16, "bold"),
        "radius": 8
    },
    "pyside_fusion": {
        "name": "PySide Fusion",
        "bg": "#353535",
        "fg": "#dddddd",
        "accent": "#308cc6",
        "secondary": "#9575cd",
        "surface": "#3d3d3d",
        "surface_variant": "#454545",
        "border": "#5a5a5a",
        "hover": "#4a4a4a",
        "success": "#66bb6a",
        "warning": "#ffa726",
        "error": "#ef5350",
        "font": ("Segoe UI", 9),
        "heading_font": ("Segoe UI", 14, "bold"),
        "radius": 4
    },
    "material_deep": {
        "name": "Material Deep",
        "bg": "#121212",
        "fg": "#e0e0e0",
        "accent": "#bb86fc",
        "secondary": "#03dac6",
        "surface": "#1e1e1e",
        "surface_variant": "#2c2c2c",
        "border": "#383838",
        "hover": "#272727",
        "success": "#4caf50",
        "warning": "#ffb74d",
        "error": "#cf6679",
        "font": ("Roboto", 9),
        "heading_font": ("Roboto", 16, "bold"),
        "radius": 12
    },
    "fluent_dark": {
        "name": "Fluent Dark",
        "bg": "#202020",
        "fg": "#ffffff",
        "accent": "#0078d4",
        "secondary": "#8961d6",
        "surface": "#2b2b2b",
        "surface_variant": "#363636",
        "border": "#414141",
        "hover": "#323232",
        "success": "#107c10",
        "warning": "#ff8c00",
        "error": "#d13438",
        "font": ("Segoe UI", 9),
        "heading_font": ("Segoe UI", 16, "bold"),
        "radius": 4
    },
    "fluent_light": {
        "name": "Fluent Light",
        "bg": "#f3f3f3",
        "fg": "#000000",
        "accent": "#0067c0",
        "secondary": "#744da9",
        "surface": "#ffffff",
        "surface_variant": "#f9f9f9",
        "border": "#d1d1d1",
        "hover": "#f5f5f5",
        "success": "#0e700e",
        "warning": "#ff8c00",
        "error": "#c42b1c",
        "font": ("Segoe UI", 9),
        "heading_font": ("Segoe UI", 16, "bold"),
        "radius": 4
    },
    "cyber_nexus": {
        "name": "Cyber Nexus",
        "bg": "#0d0d0f",
        "fg": "#00ffff",
        "accent": "#ff00ff",
        "secondary": "#00ff00",
        "surface": "#1a1a1f",
        "surface_variant": "#25252e",
        "border": "#ff00ff",
        "hover": "#2d2d3a",
        "success": "#00ff88",
        "warning": "#ffaa00",
        "error": "#ff0055",
        "font": ("Consolas", 9),
        "heading_font": ("Consolas", 16, "bold"),
        "radius": 0
    },
    "nord_frost": {
        "name": "Nord Frost",
        "bg": "#2e3440",
        "fg": "#eceff4",
        "accent": "#88c0d0",
        "secondary": "#81a1c1",
        "surface": "#3b4252",
        "surface_variant": "#434c5e",
        "border": "#4c566a",
        "hover": "#434c5e",
        "success": "#a3be8c",
        "warning": "#ebcb8b",
        "error": "#bf616a",
        "font": ("Segoe UI", 9),
        "heading_font": ("Segoe UI", 16, "bold"),
        "radius": 6
    }
}


class ThemedTk:
    """Advanced theme manager with PySide6 and Nexus UI inspired styling"""
    
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
            theme_name: Name of the theme to apply
            
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
        
        # Use clam as base theme for better customization
        self.style.theme_use('clam')
        
        # Configure base elements with modern styling
        self.style.configure(".",
                           background=theme["bg"],
                           foreground=theme["fg"],
                           fieldbackground=theme["surface"],
                           bordercolor=theme["border"],
                           font=theme["font"],
                           borderwidth=1,
                           relief="flat")
        
        # TFrame - Base frames
        self.style.configure("TFrame",
                           background=theme["bg"],
                           borderwidth=0,
                           relief="flat")
        
        # Card Frame - Elevated surface
        self.style.configure("Card.TFrame",
                           background=theme["surface"],
                           relief="flat",
                           borderwidth=1,
                           bordercolor=theme["border"])
        
        # Sidebar Frame
        self.style.configure("Sidebar.TFrame",
                           background=theme["surface_variant"],
                           relief="flat")
        
        # Toolbar Frame
        self.style.configure("Toolbar.TFrame",
                           background=theme["surface"],
                           relief="flat",
                           borderwidth=0)
        
        # TLabel - All label variants
        self.style.configure("TLabel",
                           background=theme["bg"],
                           foreground=theme["fg"],
                           font=theme["font"],
                           padding=2)
        
        self.style.configure("Heading.TLabel",
                           font=theme["heading_font"],
                           foreground=theme["accent"],
                           background=theme["bg"])
        
        self.style.configure("Card.TLabel",
                           background=theme["surface"],
                           foreground=theme["fg"])
        
        self.style.configure("Sidebar.TLabel",
                           background=theme["surface_variant"],
                           foreground=theme["fg"])
        
        self.style.configure("Muted.TLabel",
                           background=theme["bg"],
                           foreground=theme["border"])
        
        # Success/Warning/Error labels
        self.style.configure("Success.TLabel",
                           background=theme["bg"],
                           foreground=theme["success"])
        
        self.style.configure("Warning.TLabel",
                           background=theme["bg"],
                           foreground=theme["warning"])
        
        self.style.configure("Error.TLabel",
                           background=theme["bg"],
                           foreground=theme["error"])
        
        # TButton - Modern button styling
        self.style.configure("TButton",
                           background=theme["accent"],
                           foreground="#ffffff",
                           borderwidth=0,
                           focuscolor=theme["accent"],
                           padding=(16, 8),
                           font=theme["font"],
                           relief="flat")
        
        self.style.map("TButton",
                      background=[("active", theme["secondary"]),
                                ("pressed", theme["accent"]),
                                ("disabled", theme["border"])],
                      foreground=[("disabled", theme["fg"])],
                      relief=[("pressed", "flat")])
        
        # Secondary button - Outlined style
        self.style.configure("Secondary.TButton",
                           background=theme["surface"],
                           foreground=theme["fg"],
                           borderwidth=1,
                           bordercolor=theme["border"],
                           padding=(16, 8))
        
        self.style.map("Secondary.TButton",
                      background=[("active", theme["hover"]),
                                ("pressed", theme["surface"])],
                      bordercolor=[("active", theme["accent"]),
                                 ("pressed", theme["accent"])])
        
        # Accent button
        self.style.configure("Accent.TButton",
                           background=theme["secondary"],
                           foreground="#ffffff",
                           borderwidth=0,
                           padding=(16, 8))
        
        self.style.map("Accent.TButton",
                      background=[("active", theme["accent"]),
                                ("pressed", theme["secondary"])])
        
        # Success/Warning/Error buttons
        self.style.configure("Success.TButton",
                           background=theme["success"],
                           foreground="#ffffff",
                           borderwidth=0,
                           padding=(16, 8))
        
        self.style.configure("Warning.TButton",
                           background=theme["warning"],
                           foreground="#ffffff",
                           borderwidth=0,
                           padding=(16, 8))
        
        self.style.configure("Error.TButton",
                           background=theme["error"],
                           foreground="#ffffff",
                           borderwidth=0,
                           padding=(16, 8))
        
        # TEntry - Modern input fields
        self.style.configure("TEntry",
                           fieldbackground=theme["surface"],
                           foreground=theme["fg"],
                           bordercolor=theme["border"],
                           lightcolor=theme["surface"],
                           darkcolor=theme["surface"],
                           insertcolor=theme["accent"],
                           padding=10,
                           relief="flat")
        
        self.style.map("TEntry",
                      fieldbackground=[("focus", theme["surface"]),
                                     ("readonly", theme["surface_variant"])],
                      bordercolor=[("focus", theme["accent"]),
                                 ("invalid", theme["error"])],
                      lightcolor=[("focus", theme["accent"])],
                      darkcolor=[("focus", theme["accent"])])
        
        # TCheckbutton - Modern checkbox
        self.style.configure("TCheckbutton",
                           background=theme["bg"],
                           foreground=theme["fg"],
                           indicatorcolor=theme["surface"],
                           bordercolor=theme["border"],
                           padding=5)
        
        self.style.map("TCheckbutton",
                      indicatorcolor=[("selected", theme["accent"]),
                                    ("active", theme["hover"])],
                      background=[("active", theme["bg"])])
        
        # Card Checkbutton
        self.style.configure("Card.TCheckbutton",
                           background=theme["surface"],
                           foreground=theme["fg"])
        
        self.style.map("Card.TCheckbutton",
                      background=[("active", theme["surface"])])
        
        # TRadiobutton
        self.style.configure("TRadiobutton",
                           background=theme["bg"],
                           foreground=theme["fg"],
                           indicatorcolor=theme["surface"],
                           padding=5)
        
        self.style.map("TRadiobutton",
                      indicatorcolor=[("selected", theme["accent"]),
                                    ("active", theme["hover"])],
                      background=[("active", theme["bg"])])
        
        # Card Radiobutton
        self.style.configure("Card.TRadiobutton",
                           background=theme["surface"],
                           foreground=theme["fg"])
        
        # TCombobox - Dropdown styling
        self.style.configure("TCombobox",
                           fieldbackground=theme["surface"],
                           background=theme["surface"],
                           foreground=theme["fg"],
                           bordercolor=theme["border"],
                           arrowcolor=theme["fg"],
                           padding=10,
                           relief="flat")
        
        self.style.map("TCombobox",
                      fieldbackground=[("focus", theme["surface"]),
                                     ("readonly", theme["surface"])],
                      bordercolor=[("focus", theme["accent"])],
                      arrowcolor=[("active", theme["accent"])])
        
        # TProgressbar - Modern progress bar
        self.style.configure("TProgressbar",
                           background=theme["accent"],
                           troughcolor=theme["surface"],
                           bordercolor=theme["border"],
                           lightcolor=theme["accent"],
                           darkcolor=theme["accent"],
                           thickness=10)
        
        # Success/Warning/Error progressbars
        self.style.configure("Success.TProgressbar",
                           background=theme["success"],
                           troughcolor=theme["surface"])
        
        self.style.configure("Warning.TProgressbar",
                           background=theme["warning"],
                           troughcolor=theme["surface"])
        
        self.style.configure("Error.TProgressbar",
                           background=theme["error"],
                           troughcolor=theme["surface"])
        
        # TScale - Slider styling
        self.style.configure("TScale",
                           background=theme["bg"],
                           troughcolor=theme["surface"],
                           bordercolor=theme["border"],
                           sliderthickness=20,
                           sliderrelief="flat")
        
        self.style.map("TScale",
                      background=[("active", theme["accent"])])
        
        # TScrollbar - Modern scrollbar
        self.style.configure("TScrollbar",
                           background=theme["surface_variant"],
                           troughcolor=theme["bg"],
                           bordercolor=theme["border"],
                           arrowcolor=theme["fg"],
                           relief="flat")
        
        self.style.map("TScrollbar",
                      background=[("active", theme["accent"]),
                                ("pressed", theme["accent"])])
        
        # Notebook (Tabs) - Modern tab styling
        self.style.configure("TNotebook",
                           background=theme["bg"],
                           bordercolor=theme["border"],
                           tabmargins=[2, 5, 2, 0],
                           borderwidth=0)
        
        self.style.configure("TNotebook.Tab",
                           background=theme["surface"],
                           foreground=theme["fg"],
                           padding=[20, 10],
                           bordercolor=theme["border"],
                           focuscolor=theme["accent"])
        
        self.style.map("TNotebook.Tab",
                      background=[("selected", theme["accent"]),
                                ("active", theme["hover"])],
                      foreground=[("selected", "#ffffff"),
                                ("active", theme["fg"])],
                      expand=[("selected", [1, 1, 1, 0])])
        
        # TSeparator - Divider lines
        self.style.configure("TSeparator",
                           background=theme["border"])
        
        # Treeview - List/Table view
        self.style.configure("Treeview",
                           background=theme["surface"],
                           foreground=theme["fg"],
                           fieldbackground=theme["surface"],
                           borderwidth=0,
                           relief="flat")
        
        self.style.configure("Treeview.Heading",
                           background=theme["surface_variant"],
                           foreground=theme["fg"],
                           borderwidth=1,
                           relief="flat")
        
        self.style.map("Treeview",
                      background=[("selected", theme["accent"])],
                      foreground=[("selected", "#ffffff")])
        
        self.style.map("Treeview.Heading",
                      background=[("active", theme["hover"])])
        
        # Menubutton
        self.style.configure("TMenubutton",
                           background=theme["surface"],
                           foreground=theme["fg"],
                           borderwidth=1,
                           bordercolor=theme["border"],
                           padding=(10, 5),
                           relief="flat")
        
        self.style.map("TMenubutton",
                      background=[("active", theme["hover"])],
                      bordercolor=[("active", theme["accent"])])
        
        # Labelframe
        self.style.configure("TLabelframe",
                           background=theme["bg"],
                           foreground=theme["fg"],
                           bordercolor=theme["border"],
                           borderwidth=1,
                           relief="flat")
        
        self.style.configure("TLabelframe.Label",
                           background=theme["bg"],
                           foreground=theme["accent"],
                           font=theme["font"])
        
        # Spinbox
        self.style.configure("TSpinbox",
                           fieldbackground=theme["surface"],
                           foreground=theme["fg"],
                           bordercolor=theme["border"],
                           arrowcolor=theme["fg"],
                           padding=10,
                           relief="flat")
        
        self.style.map("TSpinbox",
                      fieldbackground=[("focus", theme["surface"])],
                      bordercolor=[("focus", theme["accent"])],
                      arrowcolor=[("active", theme["accent"])])
        
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
    
    def create_sidebar(self, parent, width=250, **kwargs):
        """
        Create a styled sidebar frame
        
        Args:
            parent: Parent widget
            width: Width of sidebar
            **kwargs: Additional arguments
            
        Returns:
            ttk.Frame with Sidebar style
        """
        sidebar = ttk.Frame(parent, style="Sidebar.TFrame", width=width, **kwargs)
        return sidebar
    
    def create_toolbar(self, parent, **kwargs):
        """
        Create a styled toolbar frame
        
        Args:
            parent: Parent widget
            **kwargs: Additional arguments
            
        Returns:
            ttk.Frame with Toolbar style
        """
        toolbar = ttk.Frame(parent, style="Toolbar.TFrame", **kwargs)
        return toolbar


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


def create_sidebar(parent, width=250, **kwargs):
    """
    Utility function to create a styled sidebar
    
    Args:
        parent: Parent widget
        width: Sidebar width
        **kwargs: Additional arguments
        
    Returns:
        ttk.Frame with Sidebar style
    """
    return ttk.Frame(parent, style="Sidebar.TFrame", width=width, **kwargs)


def create_demo():
    """Launch an advanced demo application showcasing all themes"""
    root = tk.Tk()
    root.title("TkModernThemes - PySide6 & Nexus Inspired")
    root.geometry("1200x800")
    
    # Initialize theme manager
    theme = ThemedTk(root)
    theme.set_theme("nexus_dark")
    
    # Create main layout with sidebar
    sidebar = theme.create_sidebar(root, width=250)
    sidebar.pack(side=tk.LEFT, fill=tk.Y)
    
    # Main content area
    main_container = ttk.Frame(root)
    main_container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    # Toolbar
    toolbar = theme.create_toolbar(main_container)
    toolbar.pack(fill=tk.X, padx=20, pady=(20, 0))
    
    # Main content
    main_frame = ttk.Frame(main_container, padding=20)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Sidebar content
    ttk.Label(sidebar, text="🎨 TkModernThemes", 
             style="Heading.TLabel").pack(pady=20, padx=15)
    
    ttk.Label(sidebar, text="Select Theme:", 
             style="Sidebar.TLabel").pack(anchor=tk.W, padx=15, pady=(10, 5))
    
    theme_var = tk.StringVar(value="nexus_dark")
    theme_listbox_frame = ttk.Frame(sidebar)
    theme_listbox_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))
    
    def change_theme(event=None):
        selected = theme_listbox.curselection()
        if selected:
            theme_name = theme.get_theme_list()[selected[0]]
            theme.set_theme(theme_name)
            create_demo_components()
    
    # Listbox for themes
    theme_listbox = tk.Listbox(theme_listbox_frame,
                               bg=theme._theme_data["surface_variant"],
                               fg=theme._theme_data["fg"],
                               selectbackground=theme._theme_data["accent"],
                               selectforeground="#ffffff",
                               borderwidth=0,
                               highlightthickness=0,
                               font=theme._theme_data["font"])
    theme_listbox.pack(fill=tk.BOTH, expand=True)
    
    for t in theme.get_theme_list():
        theme_listbox.insert(tk.END, t.replace('_', ' ').title())
    
    theme_listbox.bind("<<ListboxSelect>>", change_theme)
    theme_listbox.selection_set(0)
    
    # Toolbar content
    ttk.Label(toolbar, text="Component Showcase").pack(side=tk.LEFT, padx=5)
    ttk.Button(toolbar, text="Refresh", style="Secondary.TButton",
              command=create_demo_components).pack(side=tk.RIGHT, padx=5)
    
    # Demo components container
    demo_container = ttk.Frame(main_frame)
    demo_container.pack(fill=tk.BOTH, expand=True)
    
    def create_demo_components():
        # Clear existing components
        for widget in demo_container.winfo_children():
            widget.destroy()
        
        # Create scrollable canvas
        canvas = tk.Canvas(demo_container, bg=theme._theme_data["bg"],
                          highlightthickness=0)
        scrollbar = ttk.Scrollbar(demo_container, orient="vertical",
                                 command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Card 1: Buttons
        card1 = theme.create_card(scrollable_frame, padding=20)
        card1.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Label(card1, text="Buttons", style="Card.TLabel",
                 font=("", 12, "bold")).pack(anchor=tk.W, pady=(0, 15))
        
        btn_frame = ttk.Frame(card1)
        btn_frame.pack(fill=tk.X)
        
        ttk.Button(btn_frame, text="Primary").grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(btn_frame, text="Secondary",
                  style="Secondary.TButton").grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(btn_frame, text="Accent",
                  style="Accent.TButton").grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(btn_frame, text="Success",
                  style="Success.TButton").grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(btn_frame, text="Warning",
                  style="Warning.TButton").grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(btn_frame, text="Error",
                  style="Error.TButton").grid(row=1, column=2, padx=5, pady=5)
        
        # Card 2: Input Fields
        card2 = theme.create_card(scrollable_frame, padding=20)
        card2.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Label(card2, text="Input Fields", style="Card.TLabel",
                 font=("", 12, "bold")).pack(anchor=tk.W, pady=(0, 15))
        
        input_frame = ttk.Frame(card2)
        input_frame.pack(fill=tk.X)
        
        ttk.Label(input_frame, text="Username:", style="Card.TLabel").grid(
            row=0, column=0, sticky=tk.W, pady=8, padx=(0, 10))
        ttk.Entry(input_frame, width=35).grid(
            row=0, column=1, sticky=tk.EW, pady=8)
        
        ttk.Label(input_frame, text="Password:", style="Card.TLabel").grid(
            row=1, column=0, sticky=tk.W, pady=8, padx=(0, 10))
        ttk.Entry(input_frame, width=35, show="●").grid(
            row=1, column=1, sticky=tk.EW, pady=8)
        
        ttk.Label(input_frame, text="Country:", style="Card.TLabel").grid(
            row=2, column=0, sticky=tk.W, pady=8, padx=(0, 10))
        ttk.Combobox(input_frame, values=["USA", "UK", "Canada"], 
                    state="readonly", width=33).grid(
            row=2, column=1, sticky=tk.EW, pady=8)
        
        input_frame.columnconfigure(1, weight=1)
        
        # Card 3: Selections
        card3 = theme.create_card(scrollable_frame, padding=20)
        card3.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Label(card3, text="Selection Controls", style="Card.TLabel",
                 font=("", 12, "bold")).pack(anchor=tk.W, pady=(0, 15))
        
        check_frame = ttk.Frame(card3)
        check_frame.pack(fill=tk.X)
        
        ttk.Checkbutton(check_frame, text="Enable notifications",
                       style="Card.TCheckbutton").pack(anchor=tk.W, pady=5)
        ttk.Checkbutton(check_frame, text="Auto-save changes",
                       style="Card.TCheckbutton").pack(anchor=tk.W, pady=5)
        ttk.Checkbutton(check_frame, text="Dark mode",
                       style="Card.TCheckbutton").pack(anchor=tk.W, pady=5)
        
        ttk.Separator(check_frame, orient=tk.HORIZONTAL).pack(
            fill=tk.X, pady=15)
        
        radio_var = tk.StringVar(value="option1")
        ttk.Radiobutton(check_frame, text="Option A", variable=radio_var,
                       value="option1", style="Card.TRadiobutton").pack(
            anchor=tk.W, pady=5)
        ttk.Radiobutton(check_frame, text="Option B", variable=radio_var,
                       value="option2", style="Card.TRadiobutton").pack(
            anchor=tk.W, pady=5)
        
        # Card 4: Progress & Status
        card4 = theme.create_card(scrollable_frame, padding=20)
        card4.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Label(card4, text="Progress & Status", style="Card.TLabel",
                 font=("", 12, "bold")).pack(anchor=tk.W, pady=(0, 15))
        
        progress_frame = ttk.Frame(card4)
        progress_frame.pack(fill=tk.X)
        
        ttk.Label(progress_frame, text="Default Progress:",
                 style="Card.TLabel").pack(anchor=tk.W, pady=5)
        ttk.Progressbar(progress_frame, length=500, mode='determinate',
                       value=65).pack(fill=tk.X, pady=(0, 15))
        
        ttk.Label(progress_frame, text="Success:",
                 style="Success.TLabel").pack(anchor=tk.W, pady=5)
        ttk.Progressbar(progress_frame, length=500, mode='determinate',
                       value=85, style="Success.TProgressbar").pack(
            fill=tk.X, pady=(0, 15))
        
        ttk.Label(progress_frame, text="Warning:",
                 style="Warning.TLabel").pack(anchor=tk.W, pady=5)
        ttk.Progressbar(progress_frame, length=500, mode='determinate',
                       value=45, style="Warning.TProgressbar").pack(
            fill=tk.X, pady=(0, 15))
        
        ttk.Label(progress_frame, text="Error:",
                 style="Error.TLabel").pack(anchor=tk.W, pady=5)
        ttk.Progressbar(progress_frame, length=500, mode='determinate',
                       value=25, style="Error.TProgressbar").pack(
            fill=tk.X, pady=(0, 15))
        
        # Card 5: Scale & Sliders
        card5 = theme.create_card(scrollable_frame, padding=20)
        card5.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Label(card5, text="Sliders & Controls", style="Card.TLabel",
                 font=("", 12, "bold")).pack(anchor=tk.W, pady=(0, 15))
        
        scale_frame = ttk.Frame(card5)
        scale_frame.pack(fill=tk.X)
        
        ttk.Label(scale_frame, text="Volume:", style="Card.TLabel").pack(
            anchor=tk.W, pady=5)
        ttk.Scale(scale_frame, from_=0, to=100, orient=tk.HORIZONTAL,
                 length=500).pack(fill=tk.X, pady=(0, 15))
        
        ttk.Label(scale_frame, text="Brightness:", style="Card.TLabel").pack(
            anchor=tk.W, pady=5)
        ttk.Scale(scale_frame, from_=0, to=100, orient=tk.HORIZONTAL,
                 length=500).pack(fill=tk.X, pady=(0, 15))
        
        # Card 6: Notebook (Tabs)
        card6 = theme.create_card(scrollable_frame, padding=20)
        card6.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Label(card6, text="Tabbed Interface", style="Card.TLabel",
                 font=("", 12, "bold")).pack(anchor=tk.W, pady=(0, 15))
        
        notebook = ttk.Notebook(card6)
        notebook.pack(fill=tk.BOTH, expand=True)
        
        for i in range(3):
            tab = ttk.Frame(notebook, padding=20)
            notebook.add(tab, text=f"Tab {i+1}")
            ttk.Label(tab, text=f"Content for Tab {i+1}",
                     style="Card.TLabel").pack(pady=20)
        
        # Card 7: Treeview
        card7 = theme.create_card(scrollable_frame, padding=20)
        card7.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Label(card7, text="Data Table", style="Card.TLabel",
                 font=("", 12, "bold")).pack(anchor=tk.W, pady=(0, 15))
        
        tree_frame = ttk.Frame(card7)
        tree_frame.pack(fill=tk.BOTH, expand=True)
        
        tree_scroll = ttk.Scrollbar(tree_frame)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        tree = ttk.Treeview(tree_frame, columns=("Name", "Status", "Progress"),
                           show="headings", height=5,
                           yscrollcommand=tree_scroll.set)
        tree_scroll.config(command=tree.yview)
        
        tree.heading("Name", text="Name")
        tree.heading("Status", text="Status")
        tree.heading("Progress", text="Progress")
        
        tree.column("Name", width=200)
        tree.column("Status", width=150)
        tree.column("Progress", width=100)
        
        sample_data = [
            ("Project Alpha", "Active", "85%"),
            ("Project Beta", "Pending", "45%"),
            ("Project Gamma", "Complete", "100%"),
            ("Project Delta", "Active", "62%"),
        ]
        
        for item in sample_data:
            tree.insert("", tk.END, values=item)
        
        tree.pack(fill=tk.BOTH, expand=True)
        
        # Card 8: Labels & Typography
        card8 = theme.create_card(scrollable_frame, padding=20)
        card8.pack(fill=tk.X)
        
        ttk.Label(card8, text="Typography & Labels", style="Card.TLabel",
                 font=("", 12, "bold")).pack(anchor=tk.W, pady=(0, 15))
        
        typography_frame = ttk.Frame(card8)
        typography_frame.pack(fill=tk.X)
        
        ttk.Label(typography_frame, text="Heading Label",
                 style="Heading.TLabel").pack(anchor=tk.W, pady=5)
        ttk.Label(typography_frame, text="Regular text label",
                 style="Card.TLabel").pack(anchor=tk.W, pady=5)
        ttk.Label(typography_frame, text="Muted text (secondary)",
                 style="Muted.TLabel").pack(anchor=tk.W, pady=5)
        ttk.Label(typography_frame, text="✓ Success message",
                 style="Success.TLabel").pack(anchor=tk.W, pady=5)
        ttk.Label(typography_frame, text="⚠ Warning message",
                 style="Warning.TLabel").pack(anchor=tk.W, pady=5)
        ttk.Label(typography_frame, text="✗ Error message",
                 style="Error.TLabel").pack(anchor=tk.W, pady=5)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind mousewheel
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
    
    create_demo_components()
    
    root.mainloop()


# Allow running as standalone demo
if __name__ == "__main__":
    create_demo()