"""
Animation Demo for TkModernThemes

This example demonstrates the animation capabilities
that can be used with TkModernThemes.
"""

import tkinter as tk
from tkinter import ttk
import TkModernThemes as TKMT


class AnimationDemo:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Animation Demo - TkModernThemes")
        self.root.geometry("900x700")
        
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
        title = ttk.Label(main_container, text="Animation Demo", style="Heading.TLabel")
        title.pack(pady=(0, 20))
        
        # Create a card for controls
        control_card = self.theme.create_card(main_container, padding=20)
        control_card.pack(fill=tk.X, pady=(0, 20))
        
        # Theme transition controls
        ttk.Label(control_card, text="Theme Transitions:", style="Heading.TLabel").pack(anchor=tk.W)
        
        transition_frame = ttk.Frame(control_card)
        transition_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(transition_frame, text="Select Theme:", style="Card.TLabel").pack(side=tk.LEFT)
        self.theme_var = tk.StringVar(value="nexus_dark")
        theme_selector = ttk.Combobox(
            transition_frame,
            textvariable=self.theme_var,
            values=self.theme.get_theme_list(),
            state="readonly",
            width=20
        )
        theme_selector.pack(side=tk.LEFT, padx=(10, 10))
        
        ttk.Button(transition_frame, text="Change Theme", 
                  command=self.change_theme).pack(side=tk.LEFT)
        
        # Animation controls
        ttk.Label(control_card, text="Widget Animations:", style="Heading.TLabel").pack(anchor=tk.W, pady=(20, 10))
        
        animate_frame = ttk.Frame(control_card)
        animate_frame.pack(fill=tk.X)
        
        # Button to demonstrate animation
        self.demo_button = ttk.Button(animate_frame, text="Animate Me!", 
                                     command=self.animate_button)
        self.demo_button.pack(side=tk.LEFT, padx=(0, 10))
        
        # Card animation button
        self.card_button = ttk.Button(animate_frame, text="Animate Card", 
                                     command=self.animate_card)
        self.card_button.pack(side=tk.LEFT)
        
        # Create a card to animate
        self.demo_card = self.theme.create_card(main_container, padding=20)
        self.demo_card.pack(fill=tk.X, pady=10)
        
        ttk.Label(self.demo_card, text="Animated Card", style="Heading.TLabel").pack(anchor=tk.W)
        ttk.Label(self.demo_card, text="This card will change color when animated", 
                 style="Card.TLabel").pack(anchor=tk.W, pady=10)
    
    def change_theme(self):
        """Change theme with animation"""
        new_theme = self.theme_var.get()
        # For now, just switch the theme (animation would be implemented in a more advanced version)
        self.theme.set_theme(new_theme)
    
    def animate_button(self):
        """Animate the demo button"""
        # This is a simple example of how animations could work
        # For a real animation, we'd use the animate_widget function
        original_text = self.demo_button.cget('text')
        self.demo_button.configure(text="Animating...")
        
        # After a short delay, restore the original text
        self.root.after(1000, lambda: self.demo_button.configure(text=original_text))
    
    def animate_card(self):
        """Animate the demo card"""
        # Get the current theme colors
        theme_colors = self.theme.get_theme_colors()
        
        # Change the card's background temporarily to show animation
        original_bg = self.demo_card.cget('style')
        
        # This is a basic animation - in a real implementation we'd smoothly transition colors
        self.demo_card.configure(style="Card.TFrame")
        
        # Example of using the animation utility (simplified)
        # For a real animation, we'd use color interpolation
        self.root.after(500, lambda: self.demo_card.configure(style="Card.TFrame"))
    
    def run(self):
        """Run the application"""
        self.root.mainloop()


if __name__ == "__main__":
    app = AnimationDemo()
    app.run()