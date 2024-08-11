from fasthtml.common import *
import fh_frankenui.core as fui
from fh_frankenui.foundations import C
from enum import EnumType

app = FastHTML(hdrs=fui.Theme.blue.headers())

def get_header(text):
    return Div(Br(),P(cls=C(fui.Text.align.center, fui.H.h2, fui.Background.primary, 'my-class'))(text),Br())

def get_explanation(text):
    return Div(P(cls=C(fui.Text.size.small, fui.Text.color.muted))(text),Br())


def get_all_options(nested_enum):
    result = []
    for e in nested_enum:
        n = nested_enum.__name__
        if isinstance(e.value, EnumType):
            n += f".{e.name}"
            for sub_e in e.value:
                result.append((sub_e.C(),f"{n}.{sub_e.name}"))
        else:
            result.append((e.C(),f"{n}.{e.name}"))
    return result


@app.get("/")
async def index():
    return Div(
        # Themes
        get_header("Themes"),
        get_explanation("Franken UI has a variety of themes that can be used.  To get a CDN with the JS and CSS needed use the `Theme` enum.  For example `Theme.blue.headers()`"),
        # Buttons
        get_header("Button"),
        get_explanation("Button styling apply to both the A and Button tags.  Example: `A(cls=C(Button.base, Button.style.primary))`"),
        Strong('A: '),*[A(cls=C(fui.Button.base, c))(p) for c,p in get_all_options(fui.Button)],
        Br(),
        Strong('Button: '),*[Button(cls=C(fui.Button.base, c))(p) for c,p in get_all_options(fui.Button)],
        # Text
        get_header("Text"),
        get_explanation("Text styling apply toanything with text.  Example: `P(C(Text.style.lead))`"),
        Div(cls=fui.Column.four)(*[P(cls=C(c))(p) for c,p in get_all_options(fui.Text)]),
            
    )

serve()