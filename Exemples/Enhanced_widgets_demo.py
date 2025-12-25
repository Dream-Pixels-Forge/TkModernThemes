"""
Enhanced Widgets Demo for TkModernThemes

This example demonstrates the enhanced styling for various ttk widgets
including new button types, progress bars, and treeview customizations.
"""

import tkinter as tk
from tkinter import ttk
import TkModernThemes as TKMT


class EnhancedWidgetsDemo:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Enhanced Widgets Demo - TkModernThemes")
        self.root.geometry("1100x800")
        
        # Initialize theme manager
        self.theme = TKMT.ThemedTk(self.root)
        self.theme.set_theme("nexus_dark")
        
        # Create the UI
        self.create_ui()
    
    def create_ui(self):
        """Create the user interface"""
        # Main container
        main_container = ttk.Frame(self.root)
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title = ttk.Label(main_container, text="Enhanced Widgets Demo", style="Heading.TLabel")
        title.pack(pady=(0, 20))
        
        # Create notebook for different widget categories
        notebook = ttk.Notebook(main_container)
        notebook.pack(fill=tk.BOTH, expand=True)
        
        # Buttons tab
        self.create_buttons_tab(notebook)
        
        # Progress bars tab
        self.create_progress_tab(notebook)
        
        # Treeview tab
        self.create_treeview_tab(notebook)
        
        # Sliders tab
        self.create_sliders_tab(notebook)
    
    def create_buttons_tab(self, parent):
        """Create tab with enhanced button styles"""
        tab = ttk.Frame(parent, padding=20)
        parent.add(tab, text="Buttons")
        
        # Title
        ttk.Label(tab, text="Enhanced Button Types", style="Heading.TLabel").pack(anchor=tk.W, pady=(0, 20))
        
        # Create cards for different button types
        button_card = self.theme.create_card(tab, padding=20)
        button_card.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Label(button_card, text="Button Variants", style="Heading.TLabel").pack(anchor=tk.W)
        
        # Primary button
        btn_frame1 = ttk.Frame(button_card)
        btn_frame1.pack(fill=tk.X, pady=5)
        ttk.Label(btn_frame1, text="Primary:", style="Card.TLabel").pack(side=tk.LEFT)
        ttk.Button(btn_frame1, text="Primary Button").pack(side=tk.RIGHT)
        
        # Secondary button
        btn_frame2 = ttk.Frame(button_card)
        btn_frame2.pack(fill=tk.X, pady=5)
        ttk.Label(btn_frame2, text="Secondary:", style="Card.TLabel").pack(side=tk.LEFT)
        ttk.Button(btn_frame2, text="Secondary Button", style="Secondary.TButton").pack(side=tk.RIGHT)
        
        # Success button
        btn_frame3 = ttk.Frame(button_card)
        btn_frame3.pack(fill=tk.X, pady=5)
        ttk.Label(btn_frame3, text="Success:", style="Card.TLabel").pack(side=tk.LEFT)
        ttk.Button(btn_frame3, text="Success Button", style="Success.TButton").pack(side=tk.RIGHT)
        
        # Warning button
        btn_frame4 = ttk.Frame(button_card)
        btn_frame4.pack(fill=tk.X, pady=5)
        ttk.Label(btn_frame4, text="Warning:", style="Card.TLabel").pack(side=tk.LEFT)
        ttk.Button(btn_frame4, text="Warning Button", style="Warning.TButton").pack(side=tk.RIGHT)
        
        # Error button
        btn_frame5 = ttk.Frame(button_card)
        btn_frame5.pack(fill=tk.X, pady=5)
        ttk.Label(btn_frame5, text="Error:", style="Card.TLabel").pack(side=tk.LEFT)
        ttk.Button(btn_frame5, text="Error Button", style="Error.TButton").pack(side=tk.RIGHT)
        
        # Accent button
        btn_frame6 = ttk.Frame(button_card)
        btn_frame6.pack(fill=tk.X, pady=5)
        ttk.Label(btn_frame6, text="Accent:", style="Card.TLabel").pack(side=tk.LEFT)
        ttk.Button(btn_frame6, text="Accent Button", style="Accent.TButton").pack(side=tk.RIGHT)
    
    def create_progress_tab(self, parent):
        """Create tab with enhanced progress bar styles"""
        tab = ttk.Frame(parent, padding=20)
        parent.add(tab, text="Progress Bars")
        
        # Title
        ttk.Label(tab, text="Enhanced Progress Bars", style="Heading.TLabel").pack(anchor=tk.W, pady=(0, 20))
        
        # Create card for progress bars
        progress_card = self.theme.create_card(tab, padding=20)
        progress_card.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Label(progress_card, text="Progress Bar Variants", style="Heading.TLabel").pack(anchor=tk.W)
        
        # Standard progress bar
        prog_frame1 = ttk.Frame(progress_card)
        prog_frame1.pack(fill=tk.X, pady=10)
        ttk.Label(prog_frame1, text="Standard:", style="Card.TLabel").pack(side=tk.LEFT)
        standard_pb = ttk.Progressbar(prog_frame1, mode='determinate', value=75)
        standard_pb.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(10, 0))
        
        # Success progress bar
        prog_frame2 = ttk.Frame(progress_card)
        prog_frame2.pack(fill=tk.X, pady=10)
        ttk.Label(prog_frame2, text="Success:", style="Card.TLabel").pack(side=tk.LEFT)
        success_pb = ttk.Progressbar(prog_frame2, mode='determinate', value=50, style="Success.TProgressbar")
        success_pb.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(10, 0))
        
        # Warning progress bar
        prog_frame3 = ttk.Frame(progress_card)
        prog_frame3.pack(fill=tk.X, pady=10)
        ttk.Label(prog_frame3, text="Warning:", style="Card.TLabel").pack(side=tk.LEFT)
        warning_pb = ttk.Progressbar(prog_frame3, mode='determinate', value=30, style="Warning.TProgressbar")
        warning_pb.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(10, 0))
        
        # Error progress bar
        prog_frame4 = ttk.Frame(progress_card)
        prog_frame4.pack(fill=tk.X, pady=10)
        ttk.Label(prog_frame4, text="Error:", style="Card.TLabel").pack(side=tk.LEFT)
        error_pb = ttk.Progressbar(prog_frame4, mode='determinate', value=90, style="Error.TProgressbar")
        error_pb.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(10, 0))
    
    def create_treeview_tab(self, parent):
        """Create tab with enhanced treeview"""
        tab = ttk.Frame(parent, padding=20)
        parent.add(tab, text="Treeview")
        
        # Title
        ttk.Label(tab, text="Enhanced Treeview", style="Heading.TLabel").pack(anchor=tk.W, pady=(0, 20))
        
        # Create card for treeview
        tree_card = self.theme.create_card(tab, padding=20)
        tree_card.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(tree_card, text="Data Table with Enhanced Styling", style="Heading.TLabel").pack(anchor=tk.W)
        
        # Create treeview with scrollbars
        tree_frame = ttk.Frame(tree_card)
        tree_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        # Create treeview
        tree = ttk.Treeview(tree_frame, columns=("Type", "Status", "Progress"), show="headings", height=8)
        
        # Define headings
        tree.heading("Type", text="Type")
        tree.heading("Status", text="Status")
        tree.heading("Progress", text="Progress")
        
        # Define column widths
        tree.column("Type", width=150)
        tree.column("Status", width=150)
        tree.column("Progress", width=150)
        
        # Add sample data
        sample_data = [
            ("Project Alpha", "Active", 85),
            ("Project Beta", "Pending", 45),
            ("Project Gamma", "Complete", 100),
            ("Project Delta", "Active", 62),
            ("Project Epsilon", "On Hold", 20),
            ("Project Zeta", "Planning", 10),
            ("Project Eta", "Active", 78),
            ("Project Theta", "Complete", 100),
        ]
        
        for item in sample_data:
            tree.insert("", "end", values=(item[0], item[1], f"{item[2]}%"))
        
        # Add scrollbars
        v_scroll = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=tree.yview)
        h_scroll = ttk.Scrollbar(tree_frame, orient=tk.HORIZONTAL, command=tree.xview)
        tree.config(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)
        
        # Pack treeview and scrollbars
        tree.grid(row=0, column=0, sticky="nsew")
        v_scroll.grid(row=0, column=1, sticky="ns")
        h_scroll.grid(row=1, column=0, sticky="ew")
        
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)
    
    def create_sliders_tab(self, parent):
        """Create tab with enhanced sliders"""
        tab = ttk.Frame(parent, padding=20)
        parent.add(tab, text="Sliders")
        
        # Title
        ttk.Label(tab, text="Enhanced Sliders", style="Heading.TLabel").pack(anchor=tk.W, pady=(0, 20))
        
        # Create card for sliders
        slider_card = self.theme.create_card(tab, padding=20)
        slider_card.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(slider_card, text="Slider Controls", style="Heading.TLabel").pack(anchor=tk.W)
        
        # Horizontal sliders
        h_slider_frame = ttk.Frame(slider_card)
        h_slider_frame.pack(fill=tk.X, pady=15)
        
        ttk.Label(h_slider_frame, text="Horizontal Sliders:", style="Card.TLabel").pack(anchor=tk.W, pady=(0, 10))
        
        # Standard horizontal slider
        ttk.Label(h_slider_frame, text="Standard:", style="Card.TLabel").pack(anchor=tk.W)
        h_slider1 = ttk.Scale(h_slider_frame, from_=0, to=100, orient=tk.HORIZONTAL, value=50)
        h_slider1.pack(fill=tk.X, pady=(5, 15))
        
        # Vertical sliders
        v_slider_frame = ttk.Frame(slider_card)
        v_slider_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(v_slider_frame, text="Vertical Sliders:", style="Card.TLabel").pack(anchor=tk.W, pady=(0, 10))
        
        # Pack vertical sliders horizontally
        v_sliders_container = ttk.Frame(v_slider_frame)
        v_sliders_container.pack(fill=tk.X)
        
        for i in range(5):
            slider_frame = ttk.Frame(v_sliders_container)
            slider_frame.pack(side=tk.LEFT, fill=tk.Y, expand=True, padx=10)
            
            ttk.Label(slider_frame, text=f"Slider {i+1}", style="Card.TLabel").pack()
            v_slider = ttk.Scale(slider_frame, from_=0, to=100, orient=tk.VERTICAL, value=20*i)
            v_slider.pack(fill=tk.Y, expand=True)
    
    def run(self):
        """Run the application"""
        self.root.mainloop()


if __name__ == "__main__":
    app = EnhancedWidgetsDemo()
    app.run()