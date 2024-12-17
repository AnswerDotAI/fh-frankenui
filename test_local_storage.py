import unittest
from monsterui.core import Theme
import re

class TestLocalStoragePersistence(unittest.TestCase):
    def _clean_script(self, script_content):
        return script_content.replace('\\', '')

    def _verify_theme_script(self, script_content, theme_color, mode):
        script_content = self._clean_script(script_content)

        has_storage = (
            'localStorage.getItem' in script_content and
            'localStorage.setItem' in script_content and
            'theme-mode' in script_content
        )

        has_theme_setting = (
            'setAttribute' in script_content and
            'data-theme' in script_content and
            theme_color in script_content
        )

        has_mode_handling = (
            mode in script_content and
            ('prefers-color-scheme' in script_content if mode == 'auto' else True)
        )

        return has_storage and has_theme_setting and has_mode_handling

    def test_local_storage_script_presence(self):
        for theme_color in Theme:
            headers_light = theme_color.headers(mode='light', tw=True, daisyui=True)
            script_content = ''.join(str(header) for header in headers_light)
            self.assertTrue(
                self._verify_theme_script(script_content, theme_color.value, 'light'),
                f"Theme script missing required functionality for {theme_color.value} in light mode"
            )

            headers_dark = theme_color.headers(mode='dark', tw=True, daisyui=True)
            script_content = ''.join(str(header) for header in headers_dark)
            self.assertTrue(
                self._verify_theme_script(script_content, theme_color.value, 'dark'),
                f"Theme script missing required functionality for {theme_color.value} in dark mode"
            )

            headers_auto = theme_color.headers(mode='auto', tw=True, daisyui=True)
            script_content = ''.join(str(header) for header in headers_auto)
            self.assertTrue(
                self._verify_theme_script(script_content, theme_color.value, 'auto'),
                f"Theme script missing required functionality for {theme_color.value} in auto mode"
            )

    def test_theme_sync_across_components(self):
        for theme_color in Theme:
            headers = theme_color.headers(
                mode='auto',
                tw=True,
                hjs=True,
                frankenui=True,
                daisyui=True
            )
            script_content = self._clean_script(''.join(str(header) for header in headers))

            self.assertIn('highlight.min.js', script_content,
                         f"highlight.js missing for {theme_color.value}")
            self.assertIn('franken-ui', script_content.lower(),
                         f"FrankenUI missing for {theme_color.value}")
            self.assertIn('daisyui', script_content.lower(),
                         f"DaisyUI missing for {theme_color.value}")
            self.assertIn('tailwindcss', script_content.lower(),
                         f"Tailwind missing for {theme_color.value}")

            self.assertTrue(
                'setTheme' in script_content and
                'updateTheme' in script_content,
                f"Theme sync functions missing for {theme_color.value}"
            )

if __name__ == '__main__':
    unittest.main()
