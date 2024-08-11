# fh-frankenui

This is a wrapper of the Franken UI library.  While you can use it without FastHTML and may work well for any web-app using python to generate HTML, it is designed to be used with FastHTML and that is the focus. 

Note:  This is still under development and should be used with caution.

## Installation

```
pip install git+https://github.com/isaac-flath/fh-frankenui.git
```

## Usage Examples

### Selection of a Theme

```python
app = fast_app(hdrs=Theme.blue.headers())
```


### Compose CSS classes

```python
import fh_frankenui.core as franken

# Use a CSS Class
assert C(Text.color.red) == 'uk-text-red'

# Combine Many
assert C(Text.color.red, Text.weight.bold Text.transform.capitalize) == 'uk-text-red uk-text-small uk-text-bold'

# Combine with your own class Strings
assert C(Text.color.red, 'my-own-class', Text.transform.capitalize) == 'uk-text-red my-own-class uk-text-small'

# Use with FastHTML (Attrs first)
Div(cls=C(Text.color.red, 'my-own-class', Text.transform.capitalize))("My small red text")

# Use with FastHTML (Children first)
Div("My small red text", cls=C(Text.color.red, 'my-own-class', Text.transform.capitalize))
```


## Why?

+ Autocompletion of CSS Classes
+ Easier to Compose CSS classes and refactor with python
+ Writing lots of text strings with different CSS classes all over the place is annoying
