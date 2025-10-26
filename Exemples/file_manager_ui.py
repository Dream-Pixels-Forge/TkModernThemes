import tkinter as tk
from tkinter import ttk
import TkModernThemes as TKMT

root = tk.Tk()
root.title("File Manager")
root.geometry("900x600")

theme = TKMT.ThemedTk(root)
theme.set_theme("aurora")

# Main container with sidebar
main = ttk.Frame(root)
main.pack(fill=tk.BOTH, expand=True)

# Sidebar
sidebar = ttk.Frame(main, width=200)
sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 1))

ttk.Label(sidebar, text="📁 Folders",
          style="Heading.TLabel").pack(pady=20, padx=10)

folders = ["Documents", "Downloads", "Pictures", "Music", "Videos"]
for folder in folders:
    ttk.Button(sidebar, text=f"  📂 {folder}",
               style="Secondary.TButton").pack(fill=tk.X, padx=10, pady=2)

# Main content area
content = ttk.Frame(main, padding=20)
content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Toolbar
toolbar = ttk.Frame(content)
toolbar.pack(fill=tk.X, pady=(0, 20))

ttk.Button(toolbar, text="➕ New Folder").pack(side=tk.LEFT, padx=5)
ttk.Button(toolbar, text="📤 Upload",
           style="Secondary.TButton").pack(side=tk.LEFT, padx=5)

search_entry = ttk.Entry(toolbar, width=30)
search_entry.pack(side=tk.RIGHT)
ttk.Label(toolbar, text="🔍").pack(side=tk.RIGHT, padx=5)

# File grid
file_frame = ttk.Frame(content)
file_frame.pack(fill=tk.BOTH, expand=True)

files = [
    ("Document.pdf", "2.4 MB", "PDF"),
    ("Image.png", "1.8 MB", "PNG"),
    ("Video.mp4", "45.2 MB", "MP4"),
    ("Spreadsheet.xlsx", "156 KB", "XLSX"),
]

for i, (name, size, type_) in enumerate(files):
    row, col = i // 3, i % 3

    file_card = theme.create_card(file_frame, padding=15)
    file_card.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
    file_frame.columnconfigure(col, weight=1)

    icon = {"PDF": "📄", "PNG": "🖼️", "MP4": "🎬", "XLSX": "📊"}.get(type_, "📄")
    ttk.Label(file_card, text=icon, font=("", 32)).pack(pady=10)
    ttk.Label(file_card, text=name, style="Card.TLabel",
              font=("", 10, "bold")).pack()
    ttk.Label(file_card, text=f"{size} • {type_}",
              style="Card.TLabel").pack(pady=5)

root.mainloop()
