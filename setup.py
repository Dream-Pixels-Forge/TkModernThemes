from setuptools import setup, find_packages
import os

# Read the long description from README.md
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="TkModernThemes",
    version="2.1.0",  # Bumped version for new themes
    packages=find_packages(),
    install_requires=[
        'ttkthemes>=3.2.2',
        'pillow>=8.0.0',  # For image processing in themes
    ],
    python_requires='>=3.7',
    author="Dream-Pixels-Forge",
    author_email="contact@dreampixelsforge.com",
    description="Modern Tkinter Theme Library with 10+ beautiful themes including Cyberpunk, Glassmorphism, and Neomorphism",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dream-Pixels-Forge/TkModernThemes",
    project_urls={
        'Documentation': 'https://github.com/Dream-Pixels-Forge/TkModernThemes/wiki',
        'Source': 'https://github.com/Dream-Pixels-Forge/TkModernThemes',
        'Bug Reports': 'https://github.com/Dream-Pixels-Forge/TkModernThemes/issues',
    },
    keywords=['tkinter', 'themes', 'gui', 'cyberpunk', 'glassmorphism', 'neomorphism', 'modern-ui'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Desktop Environment :: Window Managers",
    ],
    include_package_data=True,
    package_data={
        'TkModernThemes': ['assets/*.png', 'assets/*.ttf'],
    },
    entry_points={
        'console_scripts': [
            'tkmodernthemes-demo=TkModernThemes.__main__:main',
        ],
    },
)
