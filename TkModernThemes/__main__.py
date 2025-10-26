"""
TkModernThemes Demo Application

Run with: python -m TkModernThemes
Or install and use: tkmodernthemes-demo
"""

def main():
    """Launch the theme demo application."""
    import tkinter as tk
    from TkModernThemes import create_demo
    
    # Just call create_demo without creating a root window first
    # It will handle window creation and mainloop internally
    create_demo()

if __name__ == "__main__":
    main()
