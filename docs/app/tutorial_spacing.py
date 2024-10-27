"""A tutorial on spacing using tailwind"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../SpacingGuide.ipynb.

# %% auto 0
__all__ = ['intro_md', 'gap1_md', 'gap2_md', 'space1_md', 'space2_md', 'spacing_tutorial']

# %% ../SpacingGuide.ipynb
from fasthtml.common import *
from fh_frankenui.core import *

# %% ../SpacingGuide.ipynb
intro_md = '''
# Padding & Margin & Spacing, Oh my!

This guide will cover some essentials about how to properly space apps and what the differences are between:

- Padding
- Margin
- Spacing
- Gap

Manipulating the space between components can make a huge difference to the percieved quality of the page.  Being able to tweak the spacing can have a big impact!

> Tip: I find it works best to get everything on the page without adjusting spacing much, and adjusting spacing at the end. 

## Abreviations:

First a few abbreviations that are helpful to know with tailwind (and a convention we follow in `fh_frankenui`).

- t, b, l, r = top, bottom, left, right
- p, m = padding, margin
- x, y = horizontal, vertical

That means:

- `mt` means margin on top of the element
- `px` means padding on the x axis (both left and right)
- `space-y` means apply spacing on the y axis (both top and bottom)

## Padding vs Margin

Margin applies space to the left of the component, and padding applies space on the left inside of the component. 

Please reference the example with cards below:

- `ml-20` applies space to the left of the card (outside the card)
- `pl-20` applies space on the left inside of the card (inside the card)

This means that if you want to move the whole thing but keep the actual container unchanged, use margin.  If you want to change the container by adding space inside of it, use padding.
'''

# %% ../SpacingGuide.ipynb
gap1_md = '''
## Space vs gap

Spacing and gap are both about setting the space between components.

+ Spacing applies margin to every element except for the first element in a group.  
+ Gap creates a gap between every element in flexbox elements and grids.

>Rule of thumb: Use Gap when using grids.

Let's take a look at some grid examples.
'''
gap2_md = '''
### Grid with no gap or space

The first example has no gap or not space applied.  As expected this means the cards are flush with each other.  Often this is not what you want, because a little space between cards looks much nicer.

### Grid with gap

The second example has the same grid but with gap applied.  As youc an see, this gives constent space between all elements of the grid looks great!

### Grid with space

The third example has the same grid but with space applied.  As you can see, it's not really what we want.  However it's a really good illustration of how space works so let's notice a few things about it:

**X Axis**

- The first card is flush with the left side of the page (no margin)
- The card below it isn't flush with the left side of the page (has margin)

**Y Axis**

- The first card is flush with the heading immediately above it (no margin)
- The card top it's right isn't flush with the heading above it (has margin)

So `space` applies margin to every element except for the first element in a group!

> Tip: Use your browser developer tools to inspect the examples
'''

# %% ../SpacingGuide.ipynb
space1_md = '''
Next, let's look at a form example where `gap` isn't a good choice but `space` works beautifully!
'''

space2_md = '''
### Form with no gap or space

The top form looks a bit scrunched with defaults, but it's certainly passable.  There is a bit of a space between the label and it's associated input because of the defaults in fh_frankenui.

### Form with gap

The second form with gap is identical to the first.  Because we're not in a flex element or a grid, it doesn't do anything at all!

### Form with space

`Space-y-5` adds vertical space between each child which really spreads out the form for a nice aesthetic.  If you recall from the grid example, it does not apply this margin to the first element - but in this situation (and many others) we do not want the spacing above the top element (heading) to be the same as the spacing between the form elements.

> Tip: Use your browser developer tools to inspect the examples
'''


# %% ../SpacingGuide.ipynb
spacing_tutorial = Container(
    render_md(intro_md),
    Grid(Card(H4("A Simple Card with ml-20",style='background-color: red'), 
              cls='ml-20'),
         Card(H4("A Simple Card with pl-20", style='background-color: red'),
              cls='pl-20')),
    render_md(gap1_md),
    Div(Divider(),H4("Grid"),
        Grid(Card(H4("A Simple Card")),
             Card(H4("A Simple Card")),
             Card(H4("A Simple Card")),
             Card(H4("A Simple Card")),
             Card(H4("A Simple Card")),
             Card(H4("A Simple Card")),
             cls=''),
        Divider(),
        H4("Grid with gap"),
        Grid(Card(H4("A Simple Card")),
             Card(H4("A Simple Card")),
             Card(H4("A Simple Card")),
             Card(H4("A Simple Card")),
             Card(H4("A Simple Card")),
             Card(H4("A Simple Card")),
             cls='gap-4'),
        Divider(),H4("Grid with space"),
        Grid(Card(H4("A Simple Card")),
             Card(H4("A Simple Card")),
             Card(H4("A Simple Card")),
             Card(H4("A Simple Card")),
             Card(H4("A Simple Card")),
             Card(H4("A Simple Card")),
             cls='space-x-4 space-y-4')),
    render_md(gap2_md),
    render_md(space1_md),
    Div(Form(DivCentered(H3("My Form")),
             LabelInput("Name"),
             Grid(LabelInput("Phone"), LabelInput("Email"), cols=2)),
        Divider(),
        Form(DivCentered(H3("My Form with gap")),
             LabelInput("Name"),
             Grid(LabelInput("Phone"), LabelInput("Email"), cols=2),
             cls='gap-y-5'),
        Divider(),
        Form(DivCentered(H3("My Form with Spacing")),
             LabelInput("Name"),
             Grid(LabelInput("Phone"), LabelInput("Email"), cols=2),
             cls='space-y-5')),
    render_md(space2_md),
)