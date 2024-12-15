"""Test script for verifying theme switching functionality across all colors."""
from fastcore.all import *
from monsterui.core import Theme
from fastcore.test import test_eq
import fastcore.test as test
from pathlib import Path
import json

def test_theme_headers():
    "Test theme header generation for all colors in both light and dark modes"
    # Test with just the first theme for debugging
    theme = Theme.blue
    print(f"\nTesting theme: {theme.value}")

    # Test with all components enabled
    headers_all = theme.headers(mode='light', tw=True, hjs=True, frankenui=True, daisyui=True)
    print("\nAll components headers:")
    for header in headers_all:
        print(f"Header: {str(header)}")
    assert len(headers_all) > 0, f"No headers generated for {theme.value} with all components"
    assert any('daisyui' in str(header) for header in headers_all), f"DaisyUI not included in headers for {theme.value}"
    assert any('highlight.js' in str(header) for header in headers_all), f"highlight.js not included in headers for {theme.value}"
    assert any('frankenui' in str(header).lower() for header in headers_all), f"FrankenUI not included in headers for {theme.value}"

    # Test DaisyUI-only configuration
    headers_daisy = theme.headers(mode='light', tw=True, hjs=False, frankenui=False, daisyui=True)
    print("\nDaisyUI-only headers:")
    for header in headers_daisy:
        print(f"Header: {str(header)}")
    assert len(headers_daisy) > 0, f"No headers generated for {theme.value} with DaisyUI only"
    assert any('daisyui' in str(header) for header in headers_daisy), f"DaisyUI not included in DaisyUI-only headers"
    assert not any('highlight.js' in str(header) for header in headers_daisy), f"highlight.js included when disabled"
    assert not any('frankenui' in str(header).lower() for header in headers_daisy), f"FrankenUI included when disabled"

    # Test FrankenUI-only configuration
    headers_franken = theme.headers(mode='light', tw=True, hjs=False, frankenui=True, daisyui=False)
    print("\nFrankenUI-only headers:")
    for header in headers_franken:
        print(f"Header: {str(header)}")
    assert len(headers_franken) > 0, f"No headers generated for {theme.value} with FrankenUI only"
    assert any('frankenui' in str(header).lower() for header in headers_franken), f"FrankenUI not included in FrankenUI-only headers"
    assert not any('daisyui' in str(header) for header in headers_franken), f"DaisyUI included when disabled"
    assert not any('highlight.js' in str(header) for header in headers_franken), f"highlight.js included when disabled"

    # Test all colors in both modes
    for theme_color in Theme:
        print(f"\nTesting color: {theme_color.value}")
        # Test light mode
        headers_light = theme_color.headers(mode='light', tw=True, hjs=True, frankenui=True, daisyui=True)
        assert any('theme-mode' in str(header) for header in headers_light), f"Theme sync missing for {theme_color.value} in light mode"
        assert any('data-theme' in str(header) for header in headers_light), f"DaisyUI theme missing for {theme_color.value} in light mode"

        # Test dark mode
        headers_dark = theme_color.headers(mode='dark', tw=True, hjs=True, frankenui=True, daisyui=True)
        assert any('theme-mode' in str(header) for header in headers_dark), f"Theme sync missing for {theme_color.value} in dark mode"
        assert any('data-theme' in str(header) for header in headers_dark), f"DaisyUI theme missing for {theme_color.value} in dark mode"

        # Test auto mode
        headers_auto = theme_color.headers(mode='auto', tw=True, hjs=True, frankenui=True, daisyui=True)
        assert any('prefers-color-scheme' in str(header) for header in headers_auto), f"System preference detection missing for {theme_color.value}"

    print("\nAll theme tests passed successfully!")

if __name__ == '__main__':
    test_theme_headers()
