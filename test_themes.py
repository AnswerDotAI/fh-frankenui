"""Test script for verifying theme switching functionality across all colors."""
from fastcore.all import *
from monsterui.core import Theme
from fastcore.test import test_eq
import fastcore.test as test
from pathlib import Path
import json

def test_theme_headers():
    "Test theme header generation for all colors in both light and dark modes"
    for theme in Theme:
        # Test light mode
        headers_light = theme.headers(mode='light', tw=True, hjs=True, frankenui=True, daisyui=True)
        assert len(headers_light) > 0, f"No headers generated for {theme.value} in light mode"

        # Test dark mode
        headers_dark = theme.headers(mode='dark', tw=True, hjs=True, frankenui=True, daisyui=True)
        assert len(headers_dark) > 0, f"No headers generated for {theme.value} in dark mode"

        # Test auto mode
        headers_auto = theme.headers(mode='auto', tw=True, hjs=True, frankenui=True, daisyui=True)
        assert len(headers_auto) > 0, f"No headers generated for {theme.value} in auto mode"

        # Verify DaisyUI inclusion
        daisyui_included = any('daisyui' in str(header) for header in headers_light)
        assert daisyui_included, f"DaisyUI not included in headers for {theme.value}"

        # Verify highlight.js inclusion
        hljs_included = any('highlight.js' in str(header) for header in headers_light)
        assert hljs_included, f"highlight.js not included in headers for {theme.value}"

if __name__ == '__main__':
    test_theme_headers()
    print("All theme tests passed successfully!")
