# MonsterUI Theme System

MonsterUI provides a unified theme system that synchronizes themes across multiple UI component libraries, including FrankenUI, DaisyUI, and highlight.js. This guide explains how to use the theme system effectively.

## Quick Start

```python
from monsterui.core import Theme

# Basic usage with all components
headers = Theme.blue.headers(
    mode='auto',      # 'light', 'dark', or 'auto'
    tw=True,         # Include Tailwind CSS
    hjs=True,        # Include highlight.js
    frankenui=True,  # Include FrankenUI
    daisyui=True     # Include DaisyUI
)
```

## Available Colors

MonsterUI supports 12 theme colors that work consistently across all component libraries:

- `slate`: Professional, slate theme
- `stone`: Minimalist stone theme
- `gray`: Neutral gray theme
- `neutral`: Clean, neutral theme
- `red`: Professional red theme
- `rose`: Pink/rose variation
- `orange`: Orange-based theme
- `green`: Nature-inspired theme
- `blue`: Professional blue theme
- `yellow`: Warm autumn theme
- `violet`: Rich purple theme
- `zinc`: Modern, metallic theme

## Theme Modes

The theme system supports three modes:

- `'light'`: Force light mode
- `'dark'`: Force dark mode
- `'auto'`: Automatically switch based on system preferences

## Component Options

You can selectively include UI components based on your needs:

```python
# DaisyUI only
headers = Theme.blue.headers(
    mode='auto',
    tw=True,        # Tailwind is required for DaisyUI
    daisyui=True,
    frankenui=False,
    hjs=False
)

# FrankenUI only
headers = Theme.blue.headers(
    mode='auto',
    tw=True,
    frankenui=True,
    daisyui=False,
    hjs=False
)

# With syntax highlighting
headers = Theme.blue.headers(
    mode='auto',
    tw=True,
    hjs=True,
    frankenui=True,
    daisyui=True
)
```

## Theme Synchronization

The theme system automatically synchronizes themes across all enabled components:

- DaisyUI themes are mapped to their closest equivalents
- FrankenUI themes adapt to the selected color
- highlight.js themes switch between light and dark modes
- Theme preferences are persisted in localStorage
- System theme changes are detected and applied in auto mode

## Example Usage

```python
from monsterui.core import Theme
from fastcore.foundation import HTML

def create_themed_page(color='blue', mode='auto'):
    # Get themed headers
    headers = Theme[color].headers(
        mode=mode,
        tw=True,
        hjs=True,
        frankenui=True,
        daisyui=True
    )

    # Create page content
    content = '''
    <div class="container mx-auto p-4">
        <h1 class="text-4xl font-bold mb-4">Themed Page</h1>
        <pre><code class="language-python">
        # This will be syntax highlighted
        def hello_world():
            print("Hello, themed world!")
        </code></pre>

        <!-- DaisyUI components -->
        <button class="btn btn-primary">DaisyUI Button</button>

        <!-- FrankenUI components -->
        <div class="uk-card">
            <h3>FrankenUI Card</h3>
        </div>
    </div>
    '''

    # Combine headers and content
    return HTML('\n'.join(map(str, headers)) + content)
```

This documentation provides a comprehensive guide to using MonsterUI's unified theme system for fast HTML development with synchronized themes across all UI components.
