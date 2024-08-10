# fh-frankenui

Wrapper for Franken UI to be used with fasthtml.  These are very early days, and they are not ready for general use. Contributors are welcome.  

Eventually, this will be a library and plugin; right now, I'm just trying to make useful components to determine the direction I should take.  I'm changing abstractions and API daily, so expect a lot of breaking changes.  

## What is Franken UI?

At its simplest, it is a helper for building HTML class strings used in the [Franken UI](https://getfranken.com) library.  This is done through:

+ Using enums to give autocomplete via Python
    + `style.Text.danger` = 'uk-text-danger'
    + `style.Background.primary` = 'uk-background-primary'
    + `style.Text.bold` = 'uk-text-bold'
+ Ability to add to add classes together to build a new class string
    + `s.Text.center + s.H.h2 + s.Background.primary` = `Str('uk-text-center uk-h2 uk-background-primary')`
    + `s.Text.center + s.H.h2 + s.Background.primary + 'your-own-class-string'` = `FrankenStr('uk-text-center uk-h2 uk-background-primary your-own-class-string')`
+ Theme selection
    + `s.Theme.blue.headers()`: Gives CSS and JS headers for the `blue` theme

## How do I use it?

```python
# without wrapper
P(cls='uk-text-center uk-h2 uk-background-primary')("Your Title")

# with wrapper
P(cls=Text.center + H.h2 + Background.primary)("Your Title")
```

```python
# without wrapper
P(cls='uk-text-center uk-h2 uk-background-primary my-own-class-string')("Your Title")

# with wrapper
P(cls=Text.center + H.h2 + Background.primary + 'my-own-class-string')("Your Title")
```

```python
# without wrapper
app = FastHTML(hdrs = [Script(src="https://cdn.jsdelivr.net/npm/uikit@3.21.6/dist/js/uikit.min.js"),
                        Script(src="https://cdn.jsdelivr.net/npm/uikit@3.21.6/dist/js/uikit-icons.min.js"),
                        Link(rel="stylesheet", href="https://unpkg.com/franken-wc@0.0.6/dist/css/blue.min.css")])

# with wrapper
app = FastHTML(hdrs = Theme.blue.headers())
```
