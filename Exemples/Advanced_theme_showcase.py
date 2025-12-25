"""
Advanced Theme Showcase for TkModernThemes

This example demonstrates all 13 themes with various UI components
to showcase the full capabilities of TkModernThemes.
"""

import tkinter as tk
from tkinter import ttk
import TkModernThemes as TKMT


class AdvancedThemeShowcase:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Advanced Theme Showcase - TkModernThemes")
        self.root.geometry("1200x800")
        
        # Initialize theme manager
        self.theme = TKMT.ThemedTk(self.root)
        
        # Create main layout
        self.create_layout()
        
        # Show the first theme
        self.show_theme("glassmorphism")
    
    def create_layout(self):
        """Create the main application layout"""
        # Main container
        main_container = ttk.Frame(self.root)
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create top bar with theme selector
        top_bar = ttk.Frame(main_container)
        top_bar.pack(fill=tk.X, pady=(0, 20))
        
        # Title
        title_label = ttk.Label(
            top_bar, 
            text="TkModernThemes Advanced Showcase", 
            style="Heading.TLabel"
        )
        title_label.pack(side=tk.LEFT)
        
        # Theme selector
        theme_label = ttk.Label(top_bar, text="Select Theme:", style="Card.TLabel")
        theme_label.pack(side=tk.RIGHT, padx=(10, 0))
        
        self.theme_var = tk.StringVar()
        theme_selector = ttk.Combobox(
            top_bar,
            textvariable=self.theme_var,
            values=self.theme.get_theme_list(),
            state="readonly",
            width=20
        )
        theme_selector.pack(side=tk.RIGHT, padx=(0, 10))
        theme_selector.bind("<<ComboboxSelected>>", self.on_theme_change)
        
        # Create notebook for different sections
        self.notebook = ttk.Notebook(main_container)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create different tabs
        self.create_widgets_tab()
        self.create_cards_tab()
        self.create_layout_tab()
        self.create_theme_info_tab()
    
    def create_widgets_tab(self):
        """Create tab with various widgets"""
        tab = ttk.Frame(self.notebook, padding=20)
        self.notebook.add(tab, text="Widgets")
        
        # Create a card for widgets
        card = self.theme.create_card(tab, padding=20)
        card.pack(fill=tk.BOTH, expand=True)
        
        # Title
        ttk.Label(card, text="Widget Showcase", style="Heading.TLabel").pack(anchor=tk.W, pady=(0, 20))
        
        # Create a frame for organizing widgets
        widget_frame = ttk.Frame(card)
        widget_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left column - Basic widgets
        left_frame = ttk.Frame(widget_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Labels and Entry
        ttk.Label(left_frame, text="Text Input:", style="Card.TLabel").pack(anchor=tk.W)
        ttk.Entry(left_frame).pack(fill=tk.X, pady=(0, 15))
        
        # Buttons
        ttk.Label(left_frame, text="Buttons:", style="Card.TLabel").pack(anchor=tk.W)
        btn_frame = ttk.Frame(left_frame)
        btn_frame.pack(fill=tk.X, pady=(0, 15))
        ttk.Button(btn_frame, text="Primary").pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(btn_frame, text="Secondary", style="Secondary.TButton").pack(side=tk.LEFT)
        
        # Checkboxes and Radiobuttons
        ttk.Label(left_frame, text="Checkboxes:", style="Card.TLabel").pack(anchor=tk.W, pady=(10, 0))
        ttk.Checkbutton(left_frame, text="Option 1").pack(anchor=tk.W, pady=2)
        ttk.Checkbutton(left_frame, text="Option 2").pack(anchor=tk.W, pady=2)
        
        ttk.Label(left_frame, text="Radio Buttons:", style="Card.TLabel").pack(anchor=tk.W, pady=(10, 0))
        radio_var = tk.StringVar(value="option1")
        ttk.Radiobutton(left_frame, text="Option 1", variable=radio_var, value="option1").pack(anchor=tk.W, pady=2)
        ttk.Radiobutton(left_frame, text="Option 2", variable=radio_var, value="option2").pack(anchor=tk.W, pady=2)
        
        # Right column - Advanced widgets
        right_frame = ttk.Frame(widget_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        # Combobox
        ttk.Label(right_frame, text="Dropdown:", style="Card.TLabel").pack(anchor=tk.W)
        ttk.Combobox(right_frame, values=["Item 1", "Item 2", "Item 3"], state="readonly").pack(fill=tk.X, pady=(0, 15))
        
        # Scale and Progress
        ttk.Label(right_frame, text="Slider:", style="Card.TLabel").pack(anchor=tk.W)
        scale = ttk.Scale(right_frame, from_=0, to=100, orient=tk.HORIZONTAL)
        scale.pack(fill=tk.X, pady=(0, 15))
        scale.set(50)
        
        ttk.Label(right_frame, text="Progress:", style="Card.TLabel").pack(anchor=tk.W)
        progress = ttk.Progressbar(right_frame, mode='determinate', value=65)
        progress.pack(fill=tk.X, pady=(0, 15))
        
        # Treeview
        ttk.Label(right_frame, text="Data Table:", style="Card.TLabel").pack(anchor=tk.W)
        tree_frame = ttk.Frame(right_frame)
        tree_frame.pack(fill=tk.BOTH, expand=True)
        
        tree = ttk.Treeview(tree_frame, columns=("Name", "Value"), show="headings", height=4)
        tree.heading("Name", text="Name")
        tree.heading("Value", text="Value")
        tree.column("Name", width=100)
        tree.column("Value", width=100)
        
        for i in range(5):
            tree.insert("", "end", values=(f"Item {i+1}", f"Value {i+1}"))
        
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Add scrollbar to treeview
        tree_scroll = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=tree.yview)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        tree.config(yscrollcommand=tree_scroll.set)
    
    def create_cards_tab(self):
        """Create tab with different card layouts"""
        tab = ttk.Frame(self.notebook, padding=20)
        self.notebook.add(tab, text="Cards")
        
        # Title
        ttk.Label(tab, text="Card Components Showcase", style="Heading.TLabel").pack(anchor=tk.W, pady=(0, 20))
        
        # Create multiple cards in a grid
        card_grid = ttk.Frame(tab)
        card_grid.pack(fill=tk.BOTH, expand=True)
        
        # Create 3 cards in a row
        for i in range(3):
            card = self.theme.create_card(card_grid, padding=15)
            card.grid(row=0, column=i, padx=10, sticky="nsew")
            card_grid.columnconfigure(i, weight=1)
            
            ttk.Label(card, text=f"Card {i+1}", style="Heading.TLabel").pack(anchor=tk.W)
            ttk.Label(card, text=f"This is card number {i+1}", style="Card.TLabel").pack(anchor=tk.W, pady=5)
            ttk.Button(card, text=f"Action {i+1}").pack(pady=10)
    
    def create_layout_tab(self):
        """Create tab with different layout components"""
        tab = ttk.Frame(self.notebook, padding=20)
        self.notebook.add(tab, text="Layout")
        
        # Title
        ttk.Label(tab, text="Layout Components", style="Heading.TLabel").pack(anchor=tk.W, pady=(0, 20))
        
        # Create sidebar layout
        layout_frame = ttk.Frame(tab)
        layout_frame.pack(fill=tk.BOTH, expand=True)
        
        # Sidebar
        sidebar = self.theme.create_card(layout_frame, padding=15)
        sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        
        ttk.Label(sidebar, text="Navigation", style="Heading.TLabel").pack(anchor=tk.W)
        ttk.Button(sidebar, text="Dashboard").pack(fill=tk.X, pady=2)
        ttk.Button(sidebar, text="Settings").pack(fill=tk.X, pady=2)
        ttk.Button(sidebar, text="Profile").pack(fill=tk.X, pady=2)
        
        # Main content area
        main_content = self.theme.create_card(layout_frame, padding=20)
        main_content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        ttk.Label(main_content, text="Main Content Area", style="Heading.TLabel").pack(anchor=tk.W)
        ttk.Label(main_content, text="This area uses the main theme styling", style="Card.TLabel").pack(anchor=tk.W, pady=10)
        
        # Add some content to the main area
        content_card = self.theme.create_card(main_content, padding=15)
        content_card.pack(fill=tk.X, pady=10)
        
        ttk.Label(content_card, text="Content Card", style="Card.TLabel").pack(anchor=tk.W)
        ttk.Label(content_card, text="This is a nested card inside the main content", style="Card.TLabel").pack(anchor=tk.W, pady=5)
    
    def create_theme_info_tab(self):
        """Create tab with theme information"""
        tab = ttk.Frame(self.notebook, padding=20)
        self.notebook.add(tab, text="Theme Info")
        
        # Title
        ttk.Label(tab, text="Current Theme Information", style="Heading.TLabel").pack(anchor=tk.W, pady=(0, 20))
        
        # Theme info card
        info_card = self.theme.create_card(tab, padding=20)
        info_card.pack(fill=tk.BOTH, expand=True)
        
        # Theme details
        self.theme_info_text = tk.Text(info_card, height=20, wrap=tk.WORD, bg=self.theme._theme_data["surface"], 
                                      fg=self.theme._theme_data["fg"], relief="flat", borderwidth=0)
        self.theme_info_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Scrollbar for text widget
        text_scroll = ttk.Scrollbar(info_card, orient=tk.VERTICAL, command=self.theme_info_text.yview)
        text_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.theme_info_text.config(yscrollcommand=text_scroll.set)
        
        self.update_theme_info()
    
    def update_theme_info(self):
        """Update the theme info display"""
        if hasattr(self, 'theme_info_text'):
            self.theme_info_text.delete(1.0, tk.END)
            theme_data = self.theme._theme_data
            
            info = f"Theme Name: {theme_data['name']}\n\n"
            info += f"Background: {theme_data['bg']}\n"
            info += f"Foreground: {theme_data['fg']}\n"
            info += f"Accent: {theme_data['accent']}\n"
            info += f"Secondary: {theme_data['secondary']}\n"
            info += f"Surface: {theme_data['surface']}\n"
            info += f"Surface Variant: {theme_data['surface_variant']}\n"
            info += f"Border: {theme_data['border']}\n"
            info += f"Hover: {theme_data['hover']}\n"
            info += f"Success: {theme_data['success']}\n"
            info += f"Warning: {theme_data['warning']}\n"
            info += f"Error: {theme_data['error']}\n\n"
            info += f"Font: {theme_data['font']}\n"
            info += f"Heading Font: {theme_data['heading_font']}\n"
            info += f"Radius: {theme_data['radius']}\n"
            
            # Add special properties if they exist
            if 'blur' in theme_data:
                info += f"Blur: {theme_data['blur']}\n"
            if 'shadow' in theme_data:
                info += f"Shadow: {theme_data['shadow']}\n"
            
            self.theme_info_text.insert(tk.END, info)
    
    def on_theme_change(self, event=None):
        """Handle theme change event"""
        theme_name = self.theme_var.get()
        if theme_name:
            self.show_theme(theme_name)
    
    def show_theme(self, theme_name):
        """Apply and display a specific theme"""
        self.theme.set_theme(theme_name)
        
        # Update the theme info tab
        if hasattr(self, 'theme_info_text'):
            self.update_theme_info()
    
    def run(self):
        """Run the application"""
        self.root.mainloop()


if __name__ == "__main__":
    app = AdvancedThemeShowcase()
    app.run()