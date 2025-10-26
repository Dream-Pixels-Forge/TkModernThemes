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
__all__ = ["ThemedTk", "THEMES", "create_card",
           "create_sidebar", "create_demo"]


# Enhanced theme definitions with PySide6 and Nexus UI inspiration
THEMES = {
    "cyberpunk": {
        "name": "Cyberpunk",
        "bg": "#0a0a0f",
        "fg": "#00ff9d",
        "accent": "#ff2a6d",
        "secondary": "#ff9d00",
        "surface": "#151520",
        "surface_variant": "#1e1e2e",
        "border": "#2a2a40",
        "hover": "#2a1a2e",
        "success": "#00e6c7",
        "warning": "#ffcc00",
        "error": "#ff2a6d",
        "font": ("Courier New", 10, "bold"),
        "heading_font": ("Arial Black", 16, "bold"),
        "radius": 6
    },
    "minimal_zen": {
        "name": "Minimal Zen",
        "bg": "#f8f9fa",
        "fg": "#2d3436",
        "accent": "#6c5ce7",
        "secondary": "#a29bfe",
        "surface": "#ffffff",
        "surface_variant": "#f1f2f6",
        "border": "#dfe6e9",
        "hover": "#f1f2f6",
        "success": "#00b894",
        "warning": "#fdcb6e",
        "error": "#ff7675",
        "font": ("Inter", 9),
        "heading_font": ("Inter", 16, "light"),
        "radius": 4
    },
    "dark_pro": {
        "name": "Dark Pro",
        "bg": "#121212",
        "fg": "#e0e0e0",
        "accent": "#7c4dff",
        "secondary": "#00bcd4",
        "surface": "#1e1e1e",
        "surface_variant": "#2d2d2d",
        "border": "#3a3a3a",
        "hover": "#2a2a2a",
        "success": "#4caf50",
        "warning": "#ff9800",
        "error": "#f44336",
        "font": ("Roboto", 9),
        "heading_font": ("Roboto", 16, "medium"),
        "radius": 6
    },
    "glassmorphism": {
        "name": "Glassmorphism",
        "bg": "rgba(255, 255, 255, 0.1)",
        "fg": "#ffffff",
        "accent": "#6366f1",
        "secondary": "#8b5cf6",
        "surface": "rgba(255, 255, 255, 0.1)",
        "surface_variant": "rgba(255, 255, 255, 0.15)",
        "border": "rgba(255, 255, 255, 0.18)",
        "hover": "rgba(255, 255, 255, 0.2)",
        "success": "#10b981",
        "warning": "#f59e0b",
        "error": "#ef4444",
        "font": ("Segoe UI", 9),
        "heading_font": ("Segoe UI", 16, "semibold"),
        "radius": 16,
        "blur": True
    },
    "neomorphism": {
        "name": "Neomorphism",
        "bg": "#e0e5ec",
        "fg": "#4a4a4a",
        "accent": "#5c6bc0",
        "secondary": "#7e57c2",
        "surface": "#e0e5ec",
        "surface_variant": "#e4ebf5",
        "border": "#d1d9e6",
        "hover": "#f0f0f0",
        "success": "#4caf50",
        "warning": "#ff9800",
        "error": "#f44336",
        "font": ("Poppins", 9),
        "heading_font": ("Poppins", 16, "medium"),
        "radius": 12,
        "shadow": "-6px -6px 12px #ffffff, 6px 6px 12px #a3b1c6"
    },
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
            raise ValueError(
                f"Theme '{theme_name}' not found. Available themes: {available}")

        theme = THEMES[theme_name]
        self.current_theme = theme_name
        self._theme_data = theme

        # Get theme properties with defaults
        blur_effect = theme.get("blur", False)
        shadow_effect = theme.get("shadow", None)
        radius = theme.get("radius", 4)

        # Helper function to convert RGBA to RGB if needed
        def get_rgb_color(color):
            if isinstance(color, str):
                if color.startswith('rgba'):
                    # Extract RGBA values and convert to hex
                    rgba = color[5:-1].split(',')
                    r, g, b = map(int, rgba[:3])
                    return f'#{r:02x}{g:02x}{b:02x}'
                elif color.startswith('rgb('):
                    # Handle rgb() format if needed
                    rgb = color[4:-1].split(',')
                    r, g, b = map(int, rgb)
                    return f'#{r:02x}{g:02x}{b:02x}'
            return color
            
        # Convert all theme colors to RGB
        theme_colors = {}
        for key, value in theme.items():
            if isinstance(value, str) and ('color' in key or 'bg' in key or 'fg' in key or 'border' in key):
                theme_colors[key] = get_rgb_color(value)
            else:
                theme_colors[key] = value
                
        # Update theme with converted colors
        theme.update(theme_colors)
            
        # Configure root window with theme background
        self.root.configure(bg=theme["bg"])

        # Apply blur effect if supported and enabled
        if blur_effect and hasattr(self.root, 'attributes'):
            try:
                # Windows-specific blur effect
                self.root.attributes('-transparentcolor', theme["bg"])
                self.root.attributes('-alpha', 0.98)
            except:
                pass  # Blur not supported on this platform

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

        # Configure layout for frames with rounded corners
        frame_layout = [
            (
                'Frame.border',
                {
                    'sticky': 'nswe',
                    'border': str(radius),
                    'children': [
                        (
                            'Frame.padding',
                            {
                                'sticky': 'nswe',
                                'children': [
                                    ('Frame.background', {'sticky': 'nswe'})
                                ]
                            }
                        )
                    ]
                }
            )
        ]
        self.style.layout('TFrame', frame_layout)

        # TFrame - Base frames
        self.style.configure("TFrame",
                             background=theme["bg"],
                             borderwidth=0,
                             relief="flat")

        # Card Frame - Elevated surface with shadow
        card_bg = theme["surface"]
        if blur_effect and 'rgba' in card_bg:
            # For glassmorphism effect
            self.style.configure("Card.TFrame",
                                 background=card_bg,
                                 relief="flat",
                                 borderwidth=0)
        else:
            # Regular card with border
            self.style.configure("Card.TFrame",
                                 background=theme["surface"],
                                 relief="flat",
                                 borderwidth=1,
                                 bordercolor=theme["border"])

        # Apply shadow effect if specified
        if shadow_effect and not blur_effect:
            self.style.configure("Card.TFrame",
                                 padding=(5, 5, 5, 5),
                                 borderwidth=0)
            # Note: Actual shadow would be implemented with a canvas or custom widget
            # This is a placeholder for the shadow effect

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
        sidebar = ttk.Frame(parent, style="Sidebar.TFrame",
                            width=width, **kwargs)
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


def create_demo(root=None):
    """
    Launch an advanced demo application showcasing all themes

    Args:
        root: Optional Tkinter root window. If None, a new window will be created.

    Returns:
        The root window containing the demo
    """
    import tkinter as tk
    from tkinter import ttk

    # Create window if not provided
    create_window = root is None
    if create_window:
        root = tk.Tk()
        root.title("TkModernThemes Demo")
        root.geometry("1000x700")

        # Center the window
        window_width = 1000
        window_height = 700
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Apply theme to root window
    theme = ThemedTk(root)
    theme.set_theme("nexus_dark")

    # Main container with scrollable content
    main_container = ttk.Frame(root)
    main_container.pack(fill=tk.BOTH, expand=True)

    # Create a canvas and scrollbar for the main content
    canvas = tk.Canvas(main_container)
    scrollbar = ttk.Scrollbar(
        main_container, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    # Configure the canvas scrolling
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    # Create a window in the canvas to contain the scrollable frame
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Pack the canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Bind mousewheel for scrolling
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    # Create demo components
    def create_demo_components():
        # Create a card for theme selection
        theme_card = theme.create_card(scrollable_frame, padding=20)
        theme_card.pack(fill=tk.X, padx=20, pady=20)

        # Theme selection header
        ttk.Label(theme_card, text="Select Theme", style="Heading.TLabel",
                  font=("", 14, "bold")).pack(anchor=tk.W, pady=(0, 15))

        # Theme selection frame
        theme_frame = ttk.Frame(theme_card)
        theme_frame.pack(fill=tk.X)

        # Create radio buttons for theme selection
        theme_var = tk.StringVar(value=theme.get_current_theme())

        # Create a frame for the theme buttons with a grid layout
        theme_grid = ttk.Frame(theme_frame)
        theme_grid.pack(fill=tk.X, pady=10)

        # Add theme selection buttons in a grid
        for i, theme_name in enumerate(theme.get_theme_list()):
            btn = ttk.Radiobutton(
                theme_grid,
                text=theme_name.replace('_', ' ').title(),
                variable=theme_var,
                value=theme_name,
                command=lambda n=theme_name: theme.set_theme(n)
            )
            btn.grid(row=i//3, column=i % 3, padx=10, pady=5, sticky=tk.W)

        # Add some sample widgets in a card
        widget_card = theme.create_card(scrollable_frame, padding=20)
        widget_card.pack(fill=tk.X, padx=20, pady=(0, 20))

        # Widget demo header
        ttk.Label(widget_card, text="Widget Showcase", style="Heading.TLabel",
                  font=("", 14, "bold")).pack(anchor=tk.W, pady=(0, 15))

        # Create a frame for the widget grid
        widget_frame = ttk.Frame(widget_card)
        widget_frame.pack(fill=tk.X)

        # Add some basic widgets
        # Entry field
        ttk.Label(widget_frame, text="Text Entry:").grid(
            row=0, column=0, sticky=tk.W, pady=5)
        entry = ttk.Entry(widget_frame)
        entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)

        # Buttons
        ttk.Button(widget_frame, text="Primary Button").grid(
            row=1, column=0, padx=5, pady=5)
        ttk.Button(widget_frame, text="Secondary Button", style="Secondary.TButton").grid(
            row=1, column=1, padx=5, pady=5)

        # Checkbuttons
        check_var1 = tk.BooleanVar()
        check_var2 = tk.BooleanVar(value=True)
        ttk.Checkbutton(widget_frame, text="Check me", variable=check_var1).grid(
            row=2, column=0, sticky=tk.W, pady=5)
        ttk.Checkbutton(widget_frame, text="Checked by default", variable=check_var2).grid(
            row=2, column=1, sticky=tk.W, pady=5)

        # Radio buttons
        radio_var = tk.StringVar(value="option1")
        ttk.Label(widget_frame, text="Options:").grid(
            row=3, column=0, sticky=tk.W, pady=5)
        ttk.Radiobutton(widget_frame, text="Option 1", variable=radio_var,
                        value="option1").grid(row=4, column=0, sticky=tk.W)
        ttk.Radiobutton(widget_frame, text="Option 2", variable=radio_var,
                        value="option2").grid(row=5, column=0, sticky=tk.W)

        # Scale
        ttk.Label(widget_frame, text="Volume:").grid(
            row=3, column=1, sticky=tk.W, pady=5)
        scale = ttk.Scale(widget_frame, from_=0, to=100, orient=tk.HORIZONTAL)
        scale.set(50)
        scale.grid(row=4, column=1, sticky=tk.EW, padx=5)

        # Progress bar
        ttk.Label(widget_frame, text="Progress:").grid(
            row=5, column=1, sticky=tk.W, pady=5)
        progress = ttk.Progressbar(widget_frame, mode='determinate', value=65)
        progress.grid(row=6, column=1, sticky=tk.EW, padx=5, pady=5)

        # Configure grid weights
        widget_frame.columnconfigure(1, weight=1)

        # Add a separator
        ttk.Separator(scrollable_frame, orient=tk.HORIZONTAL).pack(
            fill=tk.X, padx=20, pady=10)

        # Add a sample table (Treeview)
        table_card = theme.create_card(scrollable_frame, padding=20)
        table_card.pack(fill=tk.X, padx=20, pady=(0, 20))

        ttk.Label(table_card, text="Data Table", style="Heading.TLabel",
                  font=("", 14, "bold")).pack(anchor=tk.W, pady=(0, 15))

        # Create a frame for the treeview and scrollbar
        tree_frame = ttk.Frame(table_card)
        tree_frame.pack(fill=tk.BOTH, expand=True)

        # Add a scrollbar to the treeview
        tree_scroll = ttk.Scrollbar(tree_frame)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # Create the treeview
        tree = ttk.Treeview(
            tree_frame,
            columns=("Name", "Status", "Progress"),
            show="headings",
            yscrollcommand=tree_scroll.set,
            height=5
        )

        # Configure the scrollbar
        tree_scroll.config(command=tree.yview)

        # Define columns
        tree.heading("Name", text="Name")
        tree.heading("Status", text="Status")
        tree.heading("Progress", text="Progress")

        # Set column widths
        tree.column("Name", width=200)
        tree.column("Status", width=150)
        tree.column("Progress", width=100)

        # Add sample data
        sample_data = [
            ("Project Alpha", "Active", "85%"),
            ("Project Beta", "Pending", "45%"),
            ("Project Gamma", "Complete", "100%"),
            ("Project Delta", "Active", "62%"),
        ]

        for item in sample_data:
            tree.insert("", tk.END, values=item)

        # Pack the treeview
        tree.pack(fill=tk.BOTH, expand=True)

        # Add a tabbed interface example
        tab_card = theme.create_card(scrollable_frame, padding=20)
        tab_card.pack(fill=tk.X, padx=20, pady=(0, 20))

        ttk.Label(tab_card, text="Tabbed Interface", style="Heading.TLabel",
                  font=("", 14, "bold")).pack(anchor=tk.W, pady=(0, 15))

        # Create a notebook (tabbed interface)
        notebook = ttk.Notebook(tab_card)
        notebook.pack(fill=tk.BOTH, expand=True)

        # Create and add tabs
        for i in range(3):
            tab = ttk.Frame(notebook, padding=10)
            notebook.add(tab, text=f"Tab {i+1}")
            ttk.Label(
                tab, text=f"This is the content of Tab {i+1}").pack(pady=20)

    # Create all demo components
    create_demo_components()

    # Start the main loop if we created the window
    if create_window:
        root.mainloop()

    return root


# Allow running as standalone demo
if __name__ == "__main__":
    create_demo(None)
