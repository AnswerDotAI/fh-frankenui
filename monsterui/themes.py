"""Theme definitions and mappings for MonsterUI.

This module provides theme variables and mappings between FrankenUI and DaisyUI themes,
enabling synchronized theming across different UI component libraries.
"""

DAISYUI_THEMES = {
    'light': {
        '--border': '215 28% 17%',
        '--input': '215 28% 17%',
        '--ring': '215 28% 17%',
        '--background': '0 0% 100%',
        '--foreground': '215 28% 17%',
        '--primary': '222 47% 11%',
        '--primary-foreground': '210 40% 98%',
        '--secondary': '210 40% 96%',
        '--secondary-foreground': '222 47% 11%',
        '--destructive': '0 84% 60%',
        '--destructive-foreground': '210 40% 98%',
        '--muted': '210 40% 96%',
        '--muted-foreground': '215 28% 17%',
        '--accent': '210 40% 96%',
        '--accent-foreground': '222 47% 11%',
        '--popover': '0 0% 100%',
        '--popover-foreground': '215 28% 17%',
        '--card': '0 0% 100%',
        '--card-foreground': '215 28% 17%',
        '--radius': '0.5rem'
    },
    'dark': {
        '--border': '220 13% 69%',
        '--input': '220 13% 69%',
        '--ring': '220 13% 69%',
        '--background': '224 71% 4%',
        '--foreground': '220 13% 69%',
        '--primary': '210 40% 98%',
        '--primary-foreground': '222 47% 11%',
        '--secondary': '222 47% 11%',
        '--secondary-foreground': '210 40% 98%',
        '--destructive': '0 63% 31%',
        '--destructive-foreground': '210 40% 98%',
        '--muted': '223 47% 11%',
        '--muted-foreground': '220 13% 69%',
        '--accent': '222 47% 11%',
        '--accent-foreground': '210 40% 98%',
        '--popover': '224 71% 4%',
        '--popover-foreground': '220 13% 69%',
        '--card': '224 71% 4%',
        '--card-foreground': '220 13% 69%',
        '--radius': '0.5rem'
    }
}

# Map FrankenUI themes to their closest DaisyUI equivalents
THEME_MAPPINGS = {
    'blue': 'corporate',    # Professional blue theme
    'slate': 'business',    # Clean, modern look
    'stone': 'lofi',        # Minimalist design
    'gray': 'business',     # Professional grayscale
    'neutral': 'wireframe', # Clean, minimal design
    'red': 'valentine',     # Warm, red-based theme
    'rose': 'valentine',    # Pink/rose variation
    'orange': 'halloween',  # Orange-based theme
    'green': 'forest',      # Nature-inspired theme
    'yellow': 'retro',      # Warm, vintage feel
    'violet': 'dracula',    # Dark, purple-based theme
    'zinc': 'luxury'        # Modern, metallic theme
}
