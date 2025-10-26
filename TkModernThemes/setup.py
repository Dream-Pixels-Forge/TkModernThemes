from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="TkModernThemes",
    version="1.0.0",
    author="Dimona Patrick",
    author_email="dream.pixels.forge@gmail.com",
    description="Modern Tkinter Theme Library with 6 contemporary themes following 2025 design trends",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dream-Pixels-Forge/TkModernThemes",
    project_urls={
        "Bug Tracker": "https://github.com/Dream-Pixels-Forge/TkModernThemes/issues",
        "Documentation": "https://github.com/Dream-Pixels-Forge/TkModernThemes#readme",
        "Source Code": "https://github.com/Dream-Pixels-Forge/TkModernThemes",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Software Development :: Libraries :: Python Modules",
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
    ],
    python_requires=">=3.6",
    keywords="tkinter, themes, gui, ui, modern, design, glassmorphism, neomorphism, cyberpunk, dark-theme",
    install_requires=[
        # TkModernThemes has no external dependencies
        # tkinter comes with Python standard library
    ],
    extras_require={
        "dev": [
            "twine>=4.0.0",
            "wheel>=0.37.0",
            "setuptools>=60.0.0",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
