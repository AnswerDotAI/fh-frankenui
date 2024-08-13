# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_core.ipynb.

# %% auto 0
__all__ = ['Theme', 'Card', 'UkInput', 'UkButton']

# %% ../nbs/01_core.ipynb 2
from .foundations import *
from fasthtml.common import *
from enum import Enum

# %% ../nbs/01_core.ipynb 3
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


# %% ../nbs/01_core.ipynb 4
def Card(*c, header=None, footer=None, **kwargs):
    res = []
    if header: res += [Div(cls='uk-card-header')(header),]
    res += [Div(cls='uk-card-body')(*c),]
    if footer: res += [Div(cls='uk-card-footer')(footer),]
    return Div(cls='uk-card', **kwargs)(*res)

# %% ../nbs/01_core.ipynb 5
def UkInput(label=(), cls=(), id="", **kwargs):
    if label: 
        label = Label(label, cls='uk-form-label')
        if id: label.fr = id
    res = Input(cls=f'uk-input', **kwargs)
    if id: res.id = id
    return Div(cls=cls)(label, res)


UkInput(label="Name", id="name")

# %% ../nbs/01_core.ipynb 6
def UkButton(*c, typ="", **kwargs):
    if typ: typ = f'uk-button-{typ}'
    return Button(cls=f'uk-button {typ}', **kwargs)(*c)

UkButton("name")
