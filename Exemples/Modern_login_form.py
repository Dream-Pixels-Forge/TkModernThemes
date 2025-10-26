import tkinter as tk
from tkinter import ttk
import sys
import os

# Add the parent directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TkModernThemes as TKMT

def login():
    username = username_entry.get()
    password = password_entry.get()
    print(f"Login attempt: {username}")

root = tk.Tk()
root.title("Modern Login")
root.geometry("450x550")
root.resizable(False, False)

# Apply theme
theme = TKMT.ThemedTk(root)
theme.set_theme("nexus_dark")  # Choose from available themes

# Main container
main_frame = ttk.Frame(root, padding=40)
main_frame.pack(fill=tk.BOTH, expand=True)

# Login card
card = theme.create_card(main_frame, padding=40)
card.pack(fill=tk.BOTH, expand=True)

# Header
ttk.Label(card, text="Welcome Back", 
          style="Heading.TLabel").pack(pady=(0, 10))
ttk.Label(card, text="Sign in to continue", 
          style="Card.TLabel").pack(pady=(0, 30))

# Username field
ttk.Label(card, text="Username", style="Card.TLabel").pack(anchor=tk.W, pady=(0, 5))
username_entry = ttk.Entry(card, width=35)
username_entry.pack(fill=tk.X, pady=(0, 15))

# Password field
ttk.Label(card, text="Password", style="Card.TLabel").pack(anchor=tk.W, pady=(0, 5))
password_entry = ttk.Entry(card, width=35, show="●")
password_entry.pack(fill=tk.X, pady=(0, 10))

# Remember me
ttk.Checkbutton(card, text="Remember me").pack(anchor=tk.W, pady=(0, 20))

# Buttons
ttk.Button(card, text="Sign In", command=login).pack(fill=tk.X, pady=(0, 10))
ttk.Button(card, text="Create Account", 
          style="Secondary.TButton").pack(fill=tk.X)

# Footer
ttk.Label(card, text="Forgot password?", 
          style="Card.TLabel").pack(pady=(20, 0))

root.mainloop()