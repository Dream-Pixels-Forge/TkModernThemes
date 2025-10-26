"""
TkModernThemes Demo Application

Run with: python -m TkModernThemes
Or install and use: tkmodernthemes-demo
"""

def main():
    """Launch the theme demo application."""
    import tkinter as tk
    from . import create_demo
    
    root = tk.Tk()
    root.title("TkModernThemes Demo")
    root.geometry("1000x700")
    
    # Create and run the demo
    demo = create_demo()
    
    # Center the window
    window_width = 1000
    window_height = 700
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    root.mainloop()

if __name__ == "__main__":
    main()
