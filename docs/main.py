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
        # Text
        get_header("Text"),
        Div(cls=fui.Column.four)(*[P(cls=C(c))(p) for c,p in get_all_options(fui.Text)]),            
        # Themes
        get_header("Themes"),
        get_explanation("Franken UI has a variety of themes that can be used.  To get a CDN with the JS and CSS needed use the `Theme` enum.  For example `Theme.blue.headers()`"),
        # Buttons
        get_header("Button"),
        Strong('A: '),*[A(cls=C(fui.Button.base, c))(p) for c,p in get_all_options(fui.Button)],
        Br(),
        Strong('Button: '),*[Button(cls=C(fui.Button.base, c))(p) for c,p in get_all_options(fui.Button)],
        # Width
        get_header("Width"),
        *[Div(cls=C(fui.Background.primary, c))(P(p)) for c,p in get_all_options(fui.Width)],
        # Column
        get_header("Column"),
        *[Div(cls=fui.Column[label])(*[P(cls=fui.Background.secondary)(f'Column.{label}')]*n) for label, n in (('two',2),('three',3),('four',4),('five',5),('six',6))],
        # H
        get_header("H"),
        Div(cls=fui.Column.three)(
            *[Div(cls=C(c))(p) for c,p in get_all_options(fui.H)]
        ),
        # Card
        get_header("Card"),

        Div(cls="uk-child-width-1-2@m uk-grid-small uk-grid-match", uk_grid=True)(

        Div(cls=C(fui.Card.base, fui.Card.section.body, fui.Card.style.default))(
            H3(cls=fui.Card.section.title)("Card.style.default"),
            P(cls='uk-margin')("These cards are styled with margins in a grid, and have a Card.section.title and Card.section.body")),

        Div(cls=C(fui.Card.base, fui.Card.section.body, fui.Card.style.secondary))(
            H3(cls=fui.Card.section.title)("Card.style.secondary"),
            P(cls='uk-margin')("These cards are styled with margins in a grid, and have a Card.section.title and Card.section.body")),

        Div(cls=C(fui.Card.base, fui.Card.section.body, fui.Card.style.danger))(
            H3(cls=fui.Card.section.title)("Card.style.danger"),
            P(cls='uk-margin')("These cards are styled with margins in a grid, and have a Card.section.title and Card.section.body")),

        Div(cls=C(fui.Card.base, fui.Card.section.body, fui.Card.style.primary))(
            H3(cls=fui.Card.section.title)("Card.style.primary"),
            P(cls='uk-margin')("These cards are styled with margins in a grid, and have a Card.section.title and Card.section.body")),





    )
    )
serve()