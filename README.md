# 📦 Publishing TkModernThemes to PyPI

Complete step-by-step guide to publish your library to PyPI so anyone can install it with `pip install TkModernThemes`

## 📋 Prerequisites

1. **Python 3.6+** installed
2. **PyPI Account** - Create free accounts at:
   - [PyPI](https://pypi.org/account/register/) (production)
   - [TestPyPI](https://test.pypi.org/account/register/) (for testing)

## 🗂️ Project Structure

Ensure your project looks like this:

```
TkModernThemes/
├── TkModernThemes/
│   ├── __init__.py       # Your main library code
├── README.md             # Documentation
├── LICENSE               # MIT License
├── setup.py              # Package configuration
└── .gitignore            # (optional) Git ignore file
```

## 🚀 Step-by-Step Publishing Guide

### Step 1: Install Required Tools

```bash
# Install/upgrade packaging tools
pip install --upgrade pip setuptools wheel twine
```

### Step 2: Prepare Your Files

#### Update setup.py
Edit the `setup.py` file and replace:
- `"Your Name"` → Your actual name
- `"your.email@example.com"` → Your email
- `"https://github.com/yourusername/TkModernThemes"` → Your GitHub repo URL (if you have one)

#### Create .gitignore (Optional but Recommended)
```bash
# Create .gitignore file
cat > .gitignore << EOF
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
EOF
```

### Step 3: Build Your Package

```bash
# Navigate to your project root (where setup.py is)
cd TkModernThemes

# Build distribution packages
python setup.py sdist bdist_wheel
```

This creates two files in the `dist/` folder:
- `TkModernThemes-1.0.0.tar.gz` (source distribution)
- `TkModernThemes-1.0.0-py3-none-any.whl` (wheel distribution)

### Step 4: Test on TestPyPI First (Recommended)

**Why?** TestPyPI lets you practice without affecting the real PyPI.

#### Upload to TestPyPI:
```bash
# Upload to TestPyPI
twine upload --repository testpypi dist/*
```

You'll be prompted for:
- **Username**: Your TestPyPI username
- **Password**: Your TestPyPI password

#### Test Installation from TestPyPI:
```bash
# Test install from TestPyPI
pip install --index-url https://test.pypi.org/simple/