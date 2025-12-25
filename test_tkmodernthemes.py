"""
Comprehensive Test Suite for TkModernThemes

This test suite validates the functionality of the TkModernThemes library.
"""

import tkinter as tk
from tkinter import ttk
import unittest
import TkModernThemes as TKMT


class TestTkModernThemes(unittest.TestCase):
    """Test suite for TkModernThemes library"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the window during testing
        self.theme_manager = TKMT.ThemedTk(self.root)
    
    def tearDown(self):
        """Clean up after tests"""
        self.root.destroy()
    
    def test_theme_initialization(self):
        """Test that theme manager initializes correctly"""
        self.assertIsNotNone(self.theme_manager)
        self.assertIsNotNone(self.theme_manager.style)
        self.assertIsNone(self.theme_manager.current_theme)
    
    def test_get_theme_list(self):
        """Test that get_theme_list returns a list of themes"""
        themes = self.theme_manager.get_theme_list()
        self.assertIsInstance(themes, list)
        self.assertGreater(len(themes), 0)
        self.assertIn("glassmorphism", themes)
        self.assertIn("neomorphism", themes)
        self.assertIn("cyberpunk", themes)
        self.assertIn("minimal_zen", themes)
        self.assertIn("dark_pro", themes)
        self.assertIn("nexus_dark", themes)
        self.assertIn("nexus_light", themes)
    
    def test_set_theme_valid(self):
        """Test setting a valid theme"""
        self.theme_manager.set_theme("glassmorphism")
        self.assertEqual(self.theme_manager.current_theme, "glassmorphism")
        self.assertIsNotNone(self.theme_manager._theme_data)
    
    def test_set_theme_invalid(self):
        """Test setting an invalid theme raises ValueError"""
        with self.assertRaises(ValueError):
            self.theme_manager.set_theme("invalid_theme_name")
    
    def test_get_current_theme(self):
        """Test getting the current theme"""
        self.theme_manager.set_theme("cyberpunk")
        current = self.theme_manager.get_current_theme()
        self.assertEqual(current, "cyberpunk")
    
    def test_get_theme_colors(self):
        """Test getting theme colors"""
        self.theme_manager.set_theme("minimal_zen")
        colors = self.theme_manager.get_theme_colors()
        self.assertIsNotNone(colors)
        self.assertIn("bg", colors)
        self.assertIn("fg", colors)
        self.assertIn("accent", colors)
        
        # Test getting specific theme colors without setting it
        cyber_colors = self.theme_manager.get_theme_colors("cyberpunk")
        self.assertIsNotNone(cyber_colors)
        self.assertEqual(cyber_colors["name"], "Cyberpunk")
    
    def test_create_card(self):
        """Test creating a card widget"""
        self.theme_manager.set_theme("dark_pro")
        card = self.theme_manager.create_card(self.root)
        self.assertIsInstance(card, ttk.Frame)
        self.assertEqual(card.winfo_class(), "TFrame")
    
    def test_create_sidebar(self):
        """Test creating a sidebar widget"""
        self.theme_manager.set_theme("nexus_light")
        sidebar = self.theme_manager.create_sidebar(self.root)
        self.assertIsInstance(sidebar, ttk.Frame)
        self.assertEqual(sidebar.winfo_class(), "TFrame")
    
    def test_create_toolbar(self):
        """Test creating a toolbar widget"""
        self.theme_manager.set_theme("material_deep")
        toolbar = self.theme_manager.create_toolbar(self.root)
        self.assertIsInstance(toolbar, ttk.Frame)
        self.assertEqual(toolbar.winfo_class(), "TFrame")
    
    def test_theme_consistency(self):
        """Test that all themes can be applied without errors"""
        themes = self.theme_manager.get_theme_list()
        for theme_name in themes:
            with self.subTest(theme=theme_name):
                self.theme_manager.set_theme(theme_name)
                self.assertEqual(self.theme_manager.current_theme, theme_name)
                colors = self.theme_manager.get_theme_colors()
                self.assertIn("bg", colors)
                self.assertIn("fg", colors)
                self.assertIn("accent", colors)
    
    def test_update_theme_colors(self):
        """Test updating theme colors"""
        self.theme_manager.set_theme("glassmorphism")
        original_bg = self.theme_manager._theme_data["bg"]
        
        # Update a color
        self.theme_manager.update_theme_colors(bg="#ff0000")
        
        # Check that the color was updated
        new_colors = self.theme_manager.get_theme_colors()
        self.assertEqual(new_colors["bg"], "#ff0000")
        
        # Reset to original
        self.theme_manager.update_theme_colors(bg=original_bg)
        reset_colors = self.theme_manager.get_theme_colors()
        self.assertEqual(reset_colors["bg"], original_bg)


class TestWidgetStyling(unittest.TestCase):
    """Test that widgets are properly styled"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the window during testing
        self.theme_manager = TKMT.ThemedTk(self.root)
        self.theme_manager.set_theme("nexus_dark")
    
    def tearDown(self):
        """Clean up after tests"""
        self.root.destroy()
    
    def test_button_styling(self):
        """Test that buttons are styled correctly"""
        button = ttk.Button(self.root, text="Test Button")
        # Check that the button was created successfully
        self.assertIsInstance(button, ttk.Button)
        
        # Apply theme and check that it works
        self.theme_manager.set_theme("cyberpunk")
        button2 = ttk.Button(self.root, text="Themed Button")
        self.assertIsInstance(button2, ttk.Button)
    
    def test_label_styling(self):
        """Test that labels are styled correctly"""
        label = ttk.Label(self.root, text="Test Label")
        self.assertIsInstance(label, ttk.Label)
    
    def test_frame_styling(self):
        """Test that frames are styled correctly"""
        frame = self.theme_manager.create_card(self.root)
        self.assertIsInstance(frame, ttk.Frame)
    
    def test_entry_styling(self):
        """Test that entries are styled correctly"""
        entry = ttk.Entry(self.root)
        self.assertIsInstance(entry, ttk.Entry)


def run_tests():
    """Run all tests"""
    # Create a test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(__import__('__main__', fromlist=['TestTkModernThemes']))
    
    # Create additional suite for widget tests
    widget_suite = loader.loadTestsFromModule(__import__('__main__', fromlist=['TestWidgetStyling']))
    
    # Combine suites
    all_tests = unittest.TestSuite([suite, widget_suite])
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(all_tests)
    
    return result


if __name__ == "__main__":
    print("Running TkModernThemes Test Suite...")
    print("=" * 50)
    
    # Run the tests
    result = run_tests()
    
    print("=" * 50)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.2f}%")
    
    if result.failures:
        print("\nFailures:")
        for test, traceback in result.failures:
            print(f"  {test}: {traceback}")
    
    if result.errors:
        print("\nErrors:")
        for test, traceback in result.errors:
            print(f"  {test}: {traceback}")
    
    if not result.failures and not result.errors:
        print("\nAll tests passed! ✓")