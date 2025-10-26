# 🎨 TkModernThemes

<div align="center">

![TkModernThemes Banner](https://img.shields.io/badge/TkModernThemes-v1.0.0-blue?style=for-the-badge)
![Python Version](https://img.shields.io/badge/python-3.6+-brightgreen?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey?style=for-the-badge)

**A modern, beautiful theme library for Python Tkinter applications featuring 6 contemporary themes following 2025 design trends**

[Installation](#-installation) • [Quick Start](#-quick-start) • [Documentation](#-documentation) • [Examples](#-examples) • [Themes](#-themes)

</div>

---

## 🌟 Why TkModernThemes?

Transform your Tkinter applications from dated to dazzling! TkModernThemes brings modern design aesthetics to Python's standard GUI library with zero external dependencies.

### ✨ Key Features

- 🎭 **6 Professional Themes** - Glassmorphism, Neomorphism, Cyberpunk, Aurora, Minimal Zen, and Dark Pro
- 🎯 **Complete Widget Coverage** - Every Tkinter/ttk widget fully themed and styled
- ⚡ **Zero Dependencies** - Only requires Python's standard library
- 🔄 **Dynamic Theme Switching** - Change themes on-the-fly without restarting
- 🎨 **Modern Design Patterns** - Card layouts, hover effects, smooth transitions
- 📱 **Responsive Components** - Adaptive layouts that work with any window size
- 🛠️ **Easy Integration** - Add modern themes with just 3 lines of code
- 🎪 **Interactive Demo** - Built-in showcase of all themes and components

---

## 📦 Installation

### Install from PyPI (Recommended)

```bash
pip install TkModernThemes
```

### Install from Source

```bash
# Clone the repository
git clone https://github.com/Dream-Pixels-Forge/TkModernThemes.git
cd TkModernThemes

# Install in development mode
pip install -e .
```

### Manual Installation

1. Download the `TkModernThemes` folder
2. Place it in your project directory
3. Import and use!

---

## 🚀 Quick Start

Get started in less than 30 seconds:

```python
import tkinter as tk
from tkinter import ttk
import TkModernThemes as TKMT

# Create your application
root = tk.Tk()
root.title("My Modern App")
root.geometry("800x600")

# Apply a modern theme (just 2 lines!)
theme = TKMT.ThemedTk(root)
theme.set_theme("glassmorphism")

# Create beautiful UI
main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill=tk.BOTH, expand=True)

ttk.Label(main_frame, text="Welcome to Modern Tkinter!", 
          style="Heading.TLabel").pack(pady=20)
ttk.Button(main_frame, text="Get Started").pack()

root.mainloop()
```

### 🎪 Try the Interactive Demo

```python
import TkModernThemes as TKMT
TKMT.create_demo()
```

Or from command line:
```bash
python -m TkModernThemes
```

---

## 🎨 Themes

TkModernThemes includes 6 professionally designed themes, each optimized for different use cases:

### 1. 🌌 Glassmorphism
<details>
<summary>Click to expand</summary>

          
<img width="453" height="587" alt="Screenshot 2025-10-26 194251" src="https://github.com/user-attachments/assets/2b38ca52-81fc-4322-bf19-eacfe8a551e7" />

**Style:** Frosted glass effect with deep purples and indigo  
**Best For:** Modern web-style applications, dashboards, creative tools  
**Vibe:** Sleek, professional, contemporary

**Colors:**
- Background: `#0f0f1e` (Deep navy)
- Accent: `#6366f1` (Indigo)
- Surface: `#1a1a2e` (Dark surface)

```python
theme.set_theme("glassmorphism")
```
</details>

### 2. 🎨 Neomorphism
<details>
<summary>Click to expand</summary>

<img width="449" height="584" alt="Screenshot 2025-10-26 194222" src="https://github.com/user-attachments/assets/625b83c5-bc5c-454a-9663-86ce11443371" />


**Style:** Soft 3D shadows and highlights for tactile feeling  
**Best For:** Elegant interfaces, design-focused apps, portfolios  
**Vibe:** Soft, tactile, refined

**Colors:**
- Background: `#e0e5ec` (Soft gray)
- Accent: `#6c5ce7` (Purple)
- Surface: `#e0e5ec` (Matching background)

```python
theme.set_theme("neomorphism")
```
</details>

### 3. ⚡ Cyberpunk
<details>
<summary>Click to expand</summary>

<img width="456" height="588" alt="Screenshot 2025-10-26 194329" src="https://github.com/user-attachments/assets/1092424e-28a7-414b-bd37-6c09df99f785" />


**Style:** High-contrast neon colors with dark backgrounds  
**Best For:** Gaming apps, tech tools, futuristic interfaces  
**Vibe:** Bold, energetic, cutting-edge

**Colors:**
- Background: `#0a0e27` (Deep black-blue)
- Accent: `#ff2a6d` (Hot pink)
- Secondary: `#05d9e8` (Cyan)
- Text: `#00ff9f` (Neon green)

```python
theme.set_theme("cyberpunk")
```
</details>

### 4. 🌠 Aurora
<details>
<summary>Click to expand</summary>


<img width="456" height="586" alt="Screenshot 2025-10-26 194408" src="https://github.com/user-attachments/assets/1678845c-49d6-43cd-89b5-8bcca7c364a3" />

**Style:** Inspired by northern lights with vibrant gradients  
**Best For:** Creative applications, media tools, portfolios  
**Vibe:** Vibrant, artistic, dynamic

**Colors:**
- Background: `#0f1419` (Deep charcoal)
- Accent: `#ff6b9d` (Pink)
- Secondary: `#c38fff` (Purple)
- Border: `#7ee787` (Green)

```python
theme.set_theme("aurora")
```
</details>

### 5. 🧘 Minimal Zen
<details>
<summary>Click to expand</summary>


<img width="457" height="586" alt="Screenshot 2025-10-26 194501" src="https://github.com/user-attachments/assets/07a1880f-6f45-401b-a64f-eb8606a656f3" />


**Style:** Clean, minimal design with teal accents  
**Best For:** Productivity tools, note-taking apps, minimalist interfaces  
**Vibe:** Clean, calm, focused

**Colors:**
- Background: `#fafafa` (Off-white)
- Accent: `#2dd4bf` (Teal)
- Surface: `#ffffff` (Pure white)
- Text: `#1a1a1a` (Near black)

```python
theme.set_theme("minimal_zen")
```
</details>

### 6. 💻 Dark Pro
<details>
<summary>Click to expand</summary>

<img width="455" height="587" alt="Screenshot 2025-10-26 194534" src="https://github.com/user-attachments/assets/2ede4e20-0406-4759-b650-d8525e41e315" />


**Style:** Professional dark theme similar to VS Code  
**Best For:** Code editors, development tools, terminal apps  
**Vibe:** Professional, focused, developer-friendly

**Colors:**
- Background: `#1e1e1e` (VS Code dark)
- Accent: `#007acc` (Blue)
- Surface: `#252526` (Slightly lighter)
- Text: `#d4d4d4` (Light gray)

```python
theme.set_theme("dark_pro")
```
</details>

---

## 📚 Documentation

### Core Classes and Functions

#### `ThemedTk(root)`
Main theme manager class.

```python
theme = TKMT.ThemedTk(root)
```

**Parameters:**
- `root` - Your Tkinter root window or Toplevel widget

**Methods:**
- `set_theme(theme_name)` - Apply a theme
- `get_theme_list()` - Get list of available themes
- `get_current_theme()` - Get name of current theme
- `get_theme_colors(theme_name=None)` - Get color dictionary
- `create_card(parent, **kwargs)` - Create a styled card component

---

### Methods Reference

#### `set_theme(theme_name)`
Apply a theme to your application.

```python
theme.set_theme("glassmorphism")
```

**Parameters:**
- `theme_name` (str) - Name of theme: `"glassmorphism"`, `"neomorphism"`, `"cyberpunk"`, `"aurora"`, `"minimal_zen"`, or `"dark_pro"`

**Raises:**
- `ValueError` - If theme name is invalid

**Example:**
```python
# Apply different themes
theme.set_theme("cyberpunk")      # Neon cyberpunk style
theme.set_theme("minimal_zen")    # Clean minimal style
theme.set_theme("dark_pro")       # Professional dark theme
```

---

#### `get_theme_list()`
Get all available theme names.

```python
themes = theme.get_theme_list()
print(themes)  # ['glassmorphism', 'neomorphism', 'cyberpunk', ...]
```

**Returns:**
- `list` - List of theme name strings

**Example:**
```python
# Create a theme selector dropdown
theme_var = tk.StringVar()
theme_selector = ttk.Combobox(
    frame,
    textvariable=theme_var,
    values=theme.get_theme_list(),
    state="readonly"
)
```

---

#### `get_current_theme()`
Get the name of currently active theme.

```python
current = theme.get_current_theme()
print(f"Current theme: {current}")  # "glassmorphism"
```

**Returns:**
- `str` or `None` - Current theme name, or None if no theme applied

---

#### `get_theme_colors(theme_name=None)`
Get color dictionary for a theme.

```python
# Get current theme colors
colors = theme.get_theme_colors()
print(colors['accent'])  # '#6366f1'

# Get specific theme colors
cyber_colors = theme.get_theme_colors('cyberpunk')
print(cyber_colors['bg'])  # '#0a0e27'
```

**Parameters:**
- `theme_name` (str, optional) - Theme name. Uses current theme if None.

**Returns:**
- `dict` - Dictionary containing: `bg`, `fg`, `accent`, `secondary`, `surface`, `border`, `hover`, `font`, `heading_font`

---

#### `create_card(parent, **kwargs)`
Create a styled card frame component.

```python
card = theme.create_card(parent_frame, padding=20)
card.pack(fill=tk.X, pady=10)
```

**Parameters:**
- `parent` - Parent widget
- `**kwargs` - Additional ttk.Frame arguments (padding, width, etc.)

**Returns:**
- `ttk.Frame` - Styled frame with Card.TFrame style

**Example:**
```python
# Create multiple cards
for i in range(3):
    card = theme.create_card(main_frame, padding=20)
    card.pack(fill=tk.X, pady=10)
    ttk.Label(card, text=f"Card {i+1}").pack()
```

---

### Widget Styles

TkModernThemes provides pre-configured styles for all ttk widgets:

#### Labels
```python
# Regular label
ttk.Label(frame, text="Regular text")

# Heading label (larger, accent color)
ttk.Label(frame, text="Section Title", style="Heading.TLabel")

# Card label (for use inside cards)
ttk.Label(card, text="Card content", style="Card.TLabel")
```

#### Buttons
```python
# Primary button (accent color)
ttk.Button(frame, text="Primary Action")

# Secondary button (outlined style)
ttk.Button(frame, text="Secondary", style="Secondary.TButton")
```

#### Input Fields
```python
# Entry field
email_entry = ttk.Entry(frame, width=30)

# Password entry
password_entry = ttk.Entry(frame, width=30, show="*")

# Combobox (dropdown)
options = ttk.Combobox(frame, values=["Option 1", "Option 2"], state="readonly")
```

#### Selection Widgets
```python
# Checkbox
ttk.Checkbutton(frame, text="Remember me")

# Radio button
gender_var = tk.StringVar()
ttk.Radiobutton(frame, text="Male", variable=gender_var, value="male")
ttk.Radiobutton(frame, text="Female", variable=gender_var, value="female")
```

#### Progress & Controls
```python
# Progress bar
progress = ttk.Progressbar(frame, length=300, mode='determinate', value=50)

# Slider/Scale
volume = ttk.Scale(frame, from_=0, to=100, orient=tk.HORIZONTAL)
```

#### Containers
```python
# Frame
content_frame = ttk.Frame(root, padding=20)

# Card frame (elevated, styled)
card = theme.create_card(root, padding=20)

# Notebook (tabs)
notebook = ttk.Notebook(frame)
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Tab 1")
```

---

## 💡 Examples

### Example 1: Modern Login Form

```python
import tkinter as tk
from tkinter import ttk
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
theme.set_theme("glassmorphism")

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
```

---

### Example 2: Dashboard with Stats Cards

```python
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
```

---

### Example 3: Settings Panel

```python
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

ttk.Label(appearance_card, text="Theme", style="Card.TLabel").pack(anchor=tk.W, pady=(5, 5))
theme_choice = ttk.Combobox(appearance_card, values=theme.get_theme_list(), 
                            state="readonly", width=30)
theme_choice.set(theme.get_current_theme())
theme_choice.pack(anchor=tk.W, pady=(0, 10))
theme_choice.bind("<<ComboboxSelected>>", 
                 lambda e: theme.set_theme(theme_choice.get()))

ttk.Checkbutton(appearance_card, text="Use system theme").pack(anchor=tk.W, pady=5)
ttk.Checkbutton(appearance_card, text="Show animations").pack(anchor=tk.W, pady=5)

# Notifications Section
notif_card = theme.create_card(main, padding=20)
notif_card.pack(fill=tk.X, pady=(0, 15))

ttk.Label(notif_card, text="Notifications", 
          font=("", 12, "bold"), style="Card.TLabel").pack(anchor=tk.W, pady=(0, 10))

ttk.Checkbutton(notif_card, text="Enable desktop notifications").pack(anchor=tk.W, pady=5)
ttk.Checkbutton(notif_card, text="Enable email notifications").pack(anchor=tk.W, pady=5)
ttk.Checkbutton(notif_card, text="Enable sound alerts").pack(anchor=tk.W, pady=5)

# Volume control
volume_frame = ttk.Frame(notif_card)
volume_frame.pack(fill=tk.X, pady=10)
ttk.Label(volume_frame, text="Volume", style="Card.TLabel").pack(side=tk.LEFT, padx=(0, 10))
ttk.Scale(volume_frame, from_=0, to=100, orient=tk.HORIZONTAL, 
         length=300).pack(side=tk.LEFT)

# Action buttons
button_frame = ttk.Frame(main)
button_frame.pack(fill=tk.X, pady=20)

ttk.Button(button_frame, text="Save Changes").pack(side=tk.RIGHT, padx=5)
ttk.Button(button_frame, text="Cancel", 
          style="Secondary.TButton").pack(side=tk.RIGHT)

root.mainloop()
```

---

### Example 4: File Manager UI

```python
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

ttk.Label(sidebar, text="📁 Folders", style="Heading.TLabel").pack(pady=20, padx=10)

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
```

---

### Example 5: Theme Switcher App

```python
import tkinter as tk
from tkinter import ttk
import TkModernThemes as TKMT

class ThemeSwitcherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Theme Switcher Demo")
        self.root.geometry("800x600")
        
        # Initialize theme
        self.theme = TKMT.ThemedTk(root)
        self.theme.set_theme("glassmorphism")
        
        self.create_ui()
    
    def create_ui(self):
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        main = ttk.Frame(self.root, padding=30)
        main.pack(fill=tk.BOTH, expand=True)
        
        # Header with theme selector
        header = ttk.Frame(main)
        header.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Label(header, text="🎨 Theme Switcher", 
                 style="Heading.TLabel").pack(side=tk.LEFT)
        
        theme_var = tk.StringVar(value=self.theme.get_current_theme())
        theme_combo = ttk.Combobox(
            header,
            textvariable=theme_var,
            values=self.theme.get_theme_list(),
            state="readonly",
            width=15
        )
        theme_combo.pack(side=tk.RIGHT)
        theme_combo.bind("<<ComboboxSelected>>", self.change_theme)
        
        # Demo components
        self.create_demo_components(main)
    
    def change_theme(self, event):
        theme_name = event.widget.get()
        self.theme.set_theme(theme_name)
        self.create_ui()  # Recreate UI to apply theme
    
    def create_demo_components(self, parent):
        # Buttons card
        card1 = self.theme.create_card(parent, padding=20)
        card1.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Label(card1, text="Buttons", style="Card.TLabel", 
                 font=("", 12, "bold")).pack(anchor=tk.W, pady=(0, 10))
        
        btn_frame = ttk.Frame(card1)
        btn_frame.pack(fill=tk.X)
        ttk.Button(btn_frame, text="Primary").pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(btn_frame, text="Secondary", 
                  style="Secondary.TButton").pack(side=tk.LEFT)
        
        # Form card
        card2 = self.theme.create_card(parent, padding=20)
        card2.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Label(card2, text="Form Elements", style="Card.TLabel",
                 font=("", 12, "bold")).pack(anchor=tk.W, pady=(0, 10))
        
        ttk.Entry(card2, width=40).pack(fill=tk.X, pady=5)
        ttk.Combobox(card2, values=["Option 1", "Option 2"], 
                    state="readonly", width=38).pack(fill=tk.X, pady=5)
        
        # Controls card
        card3 = self.theme.create_card(parent, padding=20)
        card3.pack(fill=tk.X)
        
        ttk.Label(card3, text="Controls", style="Card.TLabel",
                 font=("", 12, "bold")).pack(anchor=tk.W, pady=(0, 10))
        
        ttk.Checkbutton(card3, text="Enable feature").pack(anchor=tk.W)
        ttk.Progressbar(card3, length=300, value=70).pack(pady=10, anchor=tk.W)

if __name__ == "__main__":
    root = tk.Tk()
    app = ThemeSwitcherApp(root)
    root.mainloop()
```

---

## 🎯 Use Cases

TkModernThemes is perfect for:

- 📊 **Data Visualization Tools** - Dashboards, analytics platforms
- 🎮 **Gaming Utilities** - Launchers, mod managers, game tools
- 💼 **Business Applications** - CRM, inventory systems, admin panels
- 🎨 **Creative Tools** - Image editors, design utilities, media players
- 📝 **Productivity Apps** - Note-taking, task managers, editors
- 🔧 **System Utilities** - File managers, system monitors, config tools
- 🎓 **Educational Software** - Learning platforms, quiz apps, tutorials
- 💻 **Developer Tools** - Code editors, API testers, database clients

---

## 🔧 Advanced Usage

### Custom Color Schemes

```python
import TkModernThemes as TKMT

# Access and modify theme colors
TKMT.THEMES['glassmorphism']['accent'] = '#ff0000'  # Change accent to red
TKMT.THEMES['glassmorphism']['bg'] = '#000000'  # Change background to black

# Apply modified theme
theme = TKMT.ThemedTk(root)
theme.set_theme('glassmorphism')
```

### Creating Your Own Theme

```python
import TkModernThemes as TKMT

# Add a custom theme
TKMT.THEMES['my_theme'] = {
    "name": "My Custom Theme",
    "bg": "#1a1a1a",
    "fg": "#ffffff",
    "accent": "#00ff00",
    "secondary": "#00cc00",
    "surface": "#2a2a2a",
    "border": "#3a3a3a",
    "hover": "#4a4a4a",
    "font": ("Arial", 10),
    "heading_font": ("Arial", 14, "bold")
}

# Use your custom theme
theme = TKMT.ThemedTk(root)
theme.set_theme('my_theme')
```

### Dynamic Theme Switching

```python
def create_theme_menu(menubar, theme_manager):
    """Create a menu for theme switching"""
    theme_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Themes", menu=theme_menu)
    
    for theme_name in theme_manager.get_theme_list():
        theme_menu.add_command(
            label=theme_name.replace('_', ' ').title(),
            command=lambda t=theme_name: theme_manager.set_theme(t)
        )
```

###
