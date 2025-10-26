"""
ModernThemes - A modern theme manager for CustomTkinter
Inspired by PySide6 and Nexus UI design
"""

import customtkinter as ctk
from typing import Dict, List, Optional, Union, Any, Tuple

__version__ = "3.0.0"
__author__ = "TkModernThemes"
__all__ = ["ModernThemes", "THEMES", "create_card", "create_sidebar"]

# Theme definitions with modern color schemes
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
        "font": ("Segoe UI", 12),
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
        "font": ("Segoe UI", 12),
        "heading_font": ("Segoe UI", 16, "bold"),
        "radius": 8
    },
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
        "font": ("Courier New", 12, "bold"),
        "heading_font": ("Arial Black", 16, "bold"),
        "radius": 6
    }
}

class ModernThemes:
    """
    Modern theme manager for CustomTkinter applications
    """
    
    def __init__(self, root: ctk.CTk):
        """
        Initialize the theme manager
        
        Args:
            root: CustomTkinter root window
        """
        self.root = root
        self.current_theme = None
        self._theme_data = None
    
    def set_theme(self, theme_name: str) -> None:
        """
        Apply a theme to the application
        
        Args:
            theme_name: Name of the theme to apply
            
        Raises:
            ValueError: If theme name is not found
        """
        if theme_name not in THEMES:
            available = ", ".join(THEMES.keys())
            raise ValueError(
                f"Theme '{theme_name}' not found. Available themes: {available}"
            )
        
        theme = THEMES[theme_name]
        self.current_theme = theme_name
        self._theme_data = theme
        
        # Set appearance mode based on theme name
        appearance_mode = "dark" if "dark" in theme_name.lower() else "light"
        ctk.set_appearance_mode(appearance_mode)
        
        # Set default color theme
        ctk.set_default_color_theme("blue")  # Using default blue theme as base
        
        # Apply custom colors
        self._apply_theme_styles()
    
    def _apply_theme_styles(self) -> None:
        """Apply custom styles based on the current theme"""
        theme = self._theme_data
        
        # Configure button styles
        ctk.set_widget_scaling(1.0)  # Reset to default scaling
        
        # Custom button style
        self.root.option_add('*TButton*font', theme["font"])
        self.root.option_add('*TButton*borderWidth', '0')
        self.root.option_add('*TButton*cornerRadius', theme["radius"])
        
        # Frame style
        self.root.option_add('*TFrame*background', theme["bg"])
        
        # Label style
        self.root.option_add('*TLabel*font', theme["font"])
        self.root.option_add('*TLabel*textColor', theme["fg"])
        self.root.option_add('*TLabel*background', theme["bg"])
        
        # Entry style
        self.root.option_add('*TEntry*font', theme["font"])
        self.root.option_add('*TEntry*fieldBackground', theme["surface"])
        self.root.option_add('*TEntry*foreground', theme["fg"])
        self.root.option_add('*TEntry*borderColor', theme["border"])
        self.root.option_add('*TEntry*insertColor', theme["accent"])
        
        # Configure CTk widgets
        ctk.CTkButton.appearance = {
            "corner_radius": theme["radius"],
            "border_width": 1,
            "fg_color": theme["accent"],
            "hover_color": self._adjust_color(theme["accent"], -20),
            "border_color": theme["border"],
            "text_color": "white",
            "font": theme["font"]
        }
        
        ctk.CTkFrame.appearance = {
            "corner_radius": theme["radius"],
            "border_width": 1,
            "fg_color": theme["surface"],
            "border_color": theme["border"]
        }
        
        ctk.CTkLabel.appearance = {
            "font": theme["font"],
            "text_color": theme["fg"],
            "fg_color": "transparent"
        }
        
        ctk.CTkEntry.appearance = {
            "corner_radius": theme["radius"],
            "border_width": 1,
            "fg_color": theme["surface"],
            "border_color": theme["border"],
            "text_color": theme["fg"],
            "placeholder_text_color": theme["border"],
            "font": theme["font"]
        }
    
    def _adjust_color(self, color: str, amount: int) -> str:
        """Adjust color brightness by amount (-255 to 255)"""
        import colorsys
        
        # Convert hex to RGB
        color = color.lstrip('#')
        r, g, b = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
        
        # Convert to HSV
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        
        # Adjust value (brightness)
        v = max(0, min(1, v + amount/255))
        
        # Convert back to RGB
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        
        # Convert to hex
        return f'#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}'
    
    def get_theme_list(self) -> List[str]:
        """Return list of available theme names"""
        return list(THEMES.keys())
    
    def get_current_theme(self) -> str:
        """Return current theme name"""
        return self.current_theme
    
    def get_theme_colors(self, theme_name: str = None) -> Dict[str, Any]:
        """
        Get color dictionary for a theme
        
        Args:
            theme_name: Name of theme (uses current theme if None)
            
        Returns:
            Dictionary of theme colors
        """
        if theme_name is None:
            return self._theme_data.copy()
        return THEMES.get(theme_name, {})
    
    def create_card(self, parent: ctk.CTk, **kwargs) -> ctk.CTkFrame:
        """
        Create a styled card frame
        
        Args:
            parent: Parent widget
            **kwargs: Additional arguments passed to CTkFrame
            
        Returns:
            CTkFrame with Card style
        """
        theme = self._theme_data
        return ctk.CTkFrame(
            parent,
            corner_radius=theme["radius"],
            fg_color=theme["surface"],
            border_color=theme["border"],
            border_width=1,
            **kwargs
        )
    
    def create_sidebar(self, parent: ctk.CTk, **kwargs) -> ctk.CTkFrame:
        """
        Create a styled sidebar
        
        Args:
            parent: Parent widget
            **kwargs: Additional arguments
            
        Returns:
            CTkFrame with Sidebar style
        """
        theme = self._theme_data
        return ctk.CTkFrame(
            parent,
            corner_radius=0,
            fg_color=theme["surface_variant"],
            **kwargs
        )


def create_card(parent: ctk.CTk, **kwargs) -> ctk.CTkFrame:
    """
    Utility function to create a styled card frame
    
    Args:
        parent: Parent widget
        **kwargs: Additional arguments passed to CTkFrame
        
    Returns:
        CTkFrame with Card style
    """
    return ctk.CTkFrame(
        parent,
        corner_radius=8,
        fg_color=("gray90", "gray16"),
        **kwargs
    )


def create_sidebar(parent: ctk.CTk, **kwargs) -> ctk.CTkFrame:
    """
    Utility function to create a styled sidebar
    
    Args:
        parent: Parent widget
        **kwargs: Additional arguments
        
    Returns:
        CTkFrame with Sidebar style
    """
    return ctk.CTkFrame(
        parent,
        corner_radius=0,
        fg_color=("gray85", "gray20"),
        **kwargs
    )


# Example usage
if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Modern Themes Demo")
    app.geometry("1000x700")
    
    # Initialize theme manager
    themes = ModernThemes(app)
    
    # Set initial theme
    themes.set_theme("nexus_dark")
    
    # Create main layout
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(1, weight=1)
    
    # Create sidebar
    sidebar = themes.create_sidebar(app, width=200)
    sidebar.grid(row=0, column=0, sticky="nsew")
    
    # Add theme selector
    theme_label = ctk.CTkLabel(sidebar, text="Select Theme:")
    theme_label.pack(padx=20, pady=(20, 10), anchor="w")
    
    theme_var = ctk.StringVar(value=themes.get_current_theme())
    theme_menu = ctk.CTkOptionMenu(
        sidebar,
        values=themes.get_theme_list(),
        command=lambda x: themes.set_theme(x),
        variable=theme_var
    )
    theme_menu.pack(padx=20, pady=(0, 20), fill="x")
    
    # Create main content
    main_frame = ctk.CTkFrame(app)
    main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
    main_frame.grid_columnconfigure(0, weight=1)
    
    # Add sample content
    title = ctk.CTkLabel(
        main_frame,
        text="ModernThemes for CustomTkinter",
        font=ctk.CTkFont(size=24, weight="bold")
    )
    title.pack(pady=(20, 10))
    
    card = themes.create_card(main_frame)
    card.pack(pady=10, padx=20, fill="both", expand=True)
    
    # Add some sample widgets
    button = ctk.CTkButton(card, text="Click Me!")
    button.pack(pady=20)
    
    entry = ctk.CTkEntry(card, placeholder_text="Type something...")
    entry.pack(pady=10, padx=20, fill="x")
    
    app.mainloop()
