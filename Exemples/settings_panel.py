import tkinter as tk
from tkinter import ttk
import TkModernThemes as TKMT

root = tk.Tk()
root.title("Settings")
root.geometry("700x600")

theme = TKMT.ThemedTk(root)
theme.set_theme("minimal_zen")

main = ttk.Frame(root, padding=30)
main.pack(fill=tk.BOTH, expand=True)

# Title
ttk.Label(main, text="⚙️ Settings", style="Heading.TLabel").pack(pady=(0, 20))

# Appearance Section
appearance_card = theme.create_card(main, padding=20)
appearance_card.pack(fill=tk.X, pady=(0, 15))

ttk.Label(appearance_card, text="Appearance",
          font=("", 12, "bold"), style="Card.TLabel").pack(anchor=tk.W, pady=(0, 10))

ttk.Label(appearance_card, text="Theme", style="Card.TLabel").pack(
    anchor=tk.W, pady=(5, 5))
theme_choice = ttk.Combobox(appearance_card, values=theme.get_theme_list(),
                            state="readonly", width=30)
theme_choice.set(theme.get_current_theme())
theme_choice.pack(anchor=tk.W, pady=(0, 10))
theme_choice.bind("<<ComboboxSelected>>",
                  lambda e: theme.set_theme(theme_choice.get()))

ttk.Checkbutton(appearance_card, text="Use system theme").pack(
    anchor=tk.W, pady=5)
ttk.Checkbutton(appearance_card, text="Show animations").pack(
    anchor=tk.W, pady=5)

# Notifications Section
notif_card = theme.create_card(main, padding=20)
notif_card.pack(fill=tk.X, pady=(0, 15))

ttk.Label(notif_card, text="Notifications",
          font=("", 12, "bold"), style="Card.TLabel").pack(anchor=tk.W, pady=(0, 10))

ttk.Checkbutton(notif_card, text="Enable desktop notifications").pack(
    anchor=tk.W, pady=5)
ttk.Checkbutton(notif_card, text="Enable email notifications").pack(
    anchor=tk.W, pady=5)
ttk.Checkbutton(notif_card, text="Enable sound alerts").pack(
    anchor=tk.W, pady=5)

# Volume control
volume_frame = ttk.Frame(notif_card)
volume_frame.pack(fill=tk.X, pady=10)
ttk.Label(volume_frame, text="Volume", style="Card.TLabel").pack(
    side=tk.LEFT, padx=(0, 10))
ttk.Scale(volume_frame, from_=0, to=100, orient=tk.HORIZONTAL,
          length=300).pack(side=tk.LEFT)

# Action buttons
button_frame = ttk.Frame(main)
button_frame.pack(fill=tk.X, pady=20)

ttk.Button(button_frame, text="Save Changes").pack(side=tk.RIGHT, padx=5)
ttk.Button(button_frame, text="Cancel",
           style="Secondary.TButton").pack(side=tk.RIGHT)

root.mainloop()
