import tkinter as tk
from tkinter import ttk
import TkModernThemes as TKMT

root = tk.Tk()
root.title("Analytics Dashboard")
root.geometry("1100x700")

# Apply dark pro theme
theme = TKMT.ThemedTk(root)
theme.set_theme("dark_pro")

# Main container
main = ttk.Frame(root, padding=30)
main.pack(fill=tk.BOTH, expand=True)

# Header
header_frame = ttk.Frame(main)
header_frame.pack(fill=tk.X, pady=(0, 30))

ttk.Label(header_frame, text="Dashboard", 
          style="Heading.TLabel").pack(side=tk.LEFT)

theme_selector = ttk.Combobox(
    header_frame,
    values=theme.get_theme_list(),
    state="readonly",
    width=15
)
theme_selector.set(theme.get_current_theme())
theme_selector.pack(side=tk.RIGHT)
theme_selector.bind("<<ComboboxSelected>>", 
                   lambda e: theme.set_theme(theme_selector.get()))

# Stats cards
stats_frame = ttk.Frame(main)
stats_frame.pack(fill=tk.X, pady=(0, 20))

stats = [
    ("Total Users", "24,567", "+12.5%"),
    ("Revenue", "$145,890", "+8.2%"),
    ("Active Sessions", "1,234", "+23.1%"),
    ("Conversion Rate", "3.24%", "+0.8%")
]

for i, (title, value, change) in enumerate(stats):
    card = theme.create_card(stats_frame, padding=20)
    card.grid(row=0, column=i, padx=10, sticky="ew")
    stats_frame.columnconfigure(i, weight=1)
    
    ttk.Label(card, text=title, style="Card.TLabel").pack(anchor=tk.W)
    ttk.Label(card, text=value, style="Heading.TLabel").pack(anchor=tk.W, pady=5)
    ttk.Label(card, text=change, style="Card.TLabel").pack(anchor=tk.W)

# Chart placeholder
chart_card = theme.create_card(main, padding=20)
chart_card.pack(fill=tk.BOTH, expand=True)

ttk.Label(chart_card, text="Revenue Chart", 
          style="Heading.TLabel").pack(anchor=tk.W, pady=(0, 10))

# Progress bars as simple chart
for month in ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]:
    month_frame = ttk.Frame(chart_card)
    month_frame.pack(fill=tk.X, pady=5)
    
    ttk.Label(month_frame, text=month, width=5).pack(side=tk.LEFT)
    ttk.Progressbar(month_frame, length=400, mode='determinate', 
                   value=50 + (hash(month) % 40)).pack(side=tk.LEFT, padx=10)

root.mainloop()