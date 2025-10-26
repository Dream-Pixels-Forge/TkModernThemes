from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="TkModernThemes",
    version="2.0.0",  # Updated version
    author="Your Name",  # Replace with your name
    author_email="your.email@example.com",  # Replace with your email
    description="Modern Tkinter Theme Library inspired by PySide6 and Nexus UI with 8 contemporary themes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/TkModernThemes",  # Replace with your repo URL
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/TkModernThemes/issues",
        "Documentation": "https://github.com/yourusername/TkModernThemes#readme",
        "Source Code": "https://github.com/yourusername/TkModernThemes",
        "Demo": "https://github.com/yourusername/TkModernThemes#demo",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",  # Updated status
        "Intended Audience :: Developers",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Desktop Environment",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Environment :: X11 Applications",
        "Environment :: Win32 (MS Windows)",
        "Environment :: MacOS X",
        "Framework :: tkinter",
    ],
    python_requires=">=3.6",
    keywords=[
        "tkinter",
        "themes",
        "gui",
        "ui",
        "modern",
        "design",
        "pyside6",
        "nexus",
        "material",
        "fluent",
        "nord",
        "dark-theme",
        "light-theme",
        "widgets",
        "styling",
        "ttk",
        "desktop",
        "cross-platform"
    ],
    install_requires=[
        # TkModernThemes has no external dependencies
        # tkinter comes with Python standard library
    ],
    extras_require={
        "dev": [
            "twine>=4.0.0",
            "wheel>=0.37.0",
            "setuptools>=60.0.0",
            "build>=0.7.0",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'tkmodernthemes-demo=TkModernThemes:create_demo',
        ],
    },
)