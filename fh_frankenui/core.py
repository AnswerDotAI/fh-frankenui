from fasthtml.common import *
from fh_frankenui.foundations import *
from enum import Enum
class Theme(Enum):
    slate = "slate"
    stone = "stone"
    gray = "gray"
    neutral = "neutral"
    red = "red"
    rose = "rose"
    orange = "orange"
    green = "green"
    blue = "blue"
    yellow = "yellow"
    violet = "violet"
    zinc = "zinc"

    def headers(self):
        js = (Script(src="https://cdn.jsdelivr.net/npm/uikit@3.21.6/dist/js/uikit.min.js"),
              Script(src="https://cdn.jsdelivr.net/npm/uikit@3.21.6/dist/js/uikit-icons.min.js"))
        _url = "https://unpkg.com/franken-wc@0.0.6/dist/css/{theme}.min.css"
        return (*js, Link(rel="stylesheet", href=_url.format(theme=self.value)))

class Button(ObjectEnum):
    default = "default"
    ghost = "ghost"
    primary = "primary"
    secondary = "secondary"
    danger = "danger"
    text = "text"
    link = "link"

    def __str__(self):
        return f"uk-button uk-button-{self.value}"
    
class Width(StyleEnum):
    full = "1-1"
    half = "1-2"
    one_third = "1-3"
    two_thirds = "2-3"
    one_fourth = "1-4"
    three_fourths = "3-4"
    one_fifth = "1-5"
    two_fifths = "2-5"
    three_fifths = "3-5"
    four_fifths = "4-5"
    one_sixth = "1-6"
    five_sixths = "5-6"

class Text(StyleEnum):
    #style
    lead = "lead"
    meta = "meta"
    italic = "italic"
    #size
    small = "small"
    default = "default"
    large = "large"
    #weight
    light = "light"
    normal = "normal"
    bold = "bold"
    lighter = "lighter"
    bolder = "bolder"
    #transform
    capitalize = "capitalize"
    uppercase = "uppercase"
    lowercase = "lowercase"
    #decoration
    decoration_none = "decoration-none"
    #color
    muted = "muted"
    primary = "primary"
    secondary = "secondary"
    success = "success"
    warning = "warning"
    danger = "danger"
    #alignment
    left = "left"
    right = "right"
    center = "center"
    justify = "justify"

class Column(StyleEnum):
    two = "1-2"
    three = "1-3"
    four = "1-4"
    five = "1-5"
    six = "1-6"


class Background(StyleEnum):
    #background
    default = "default"
    muted = "muted"
    primary = "primary"
    secondary = "secondary"
    #size
    cover = "cover"
    contain = "contain"
    width_1_1 = "width-1-1"
    height_1_1 = "height-1-1"
    #position
    top_left = "top-left"
    top_center = "top-center"
    top_right = "top-right"
    center_left = "center-left"
    center_center = "center-center"
    center_right = "center-right"
    bottom_left = "bottom-left"
    bottom_center = "bottom-center"
    bottom_right = "bottom-right"
    # repeat
    norepeat = "norepeat"
    #attachment
    fixed = "fixed"
    #responsive
    images_at_s_screen = "images@s"
    images_at_m_screen = "images@m"
    images_at_l_screen = "images@l"
    images_at_xl_screen = "images@xl"
    #blend modes
    blend_multiply = "blend-multiply"
    blend_screen = "blend-screen"
    blend_overlay = "blend-overlay"
    blend_darken = "blend-darken"
    blend_lighten = "blend-lighten"
    blend_color_dodge = "blend-color-dodge"
    blend_color_burn = "blend-color-burn"
    blend_hard_light = "blend-hard-light"
    blend_soft_light = "blend-soft-light"
    blend_difference = "blend-difference"
    blend_exclusion = "blend-exclusion"
    blend_hue = "blend-hue"
    blend_saturation = "blend-saturation"
    blend_color = "blend-color"
    blend_luminosity = "blend-luminosity"

class H(StyleEnum):
    h1 = "1"
    h2 = "2"
    h3 = "3"
    h4 = "4"
    h5 = "5"
    h6 = "6"

    def __str__(self):
        return f"uk-h{self.value}"