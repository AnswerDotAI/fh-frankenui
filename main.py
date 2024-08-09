from fasthtml.common import *
import fh_frankenui.core as fui

app = FastHTML(hdrs=fui.Theme.blue.headers())

def get_header(text):
    return Div(Br(),P(cls=fui.Text.center + fui.H.h2 + fui.Background.primary + 'my-class')(text),Br())

@app.get("/")
async def index():
    return Div(
        get_header("Text"),
        Div(cls=fui.Column.six)( *[P(cls=e)(e.name) for e in fui.Text],),

        get_header("Button"),
        Strong('A: '),*[A(cls=e)(e.name) for e in fui.Button],
        Br(),
        Strong('Button: '),*[Button(cls=e)(e.name) for e in fui.Button],

        get_header("Width"),
        *[Button(cls=fui.Button.default + e)(e.name) for e in fui.Width],
        
        get_header("Text"),
        Div(cls=fui.Column.six)( *[P(cls=e)(e.name) for e in fui.Text],),

        get_header("Column"),
        Div(cls=fui.Column.two)(*[P(cls=fui.Background.muted)("two")]*2),Br(),
        Div(cls=fui.Column.three)(*[P(cls=fui.Background.muted)("three")]*3),Br(),
        Div(cls=fui.Column.four)(*[P(cls=fui.Background.muted)("four")]*4),Br(),
        Div(cls=fui.Column.five)(*[P(cls=fui.Background.muted)("five")]*5),Br(),
        Div(cls=fui.Column.six)(*[P(cls=fui.Background.muted)("six")]*6),Br(),
        
        get_header('Background'),
        Div(uk_grid='', cls='uk-child-width-1-3@s uk-grid-small uk-child-width-1-2')(
            Div(Div(style='background-image: url(https://avatars.githubusercontent.com/u/6256508?v=4); height: 500px;',
                    cls=fui.Background.primary + (fui.Background.cover + fui.Background.blend_overlay),
                    )(P(cls=fui.Text.bold + 'uk-h3')('blend_overlay'))),

            Div(Div(style='background-image: url(https://avatars.githubusercontent.com/u/6256508?v=4); height: 500px;',
                    cls=fui.Background.primary + (fui.Background.cover + fui.Background.blend_color),
                    )(P(cls=fui.Text.bold + 'uk-h3')('blend_color'))),

            Div(Div(style='background-image: url(https://avatars.githubusercontent.com/u/6256508?v=4); height: 500px;',
                    cls=fui.Background.primary + (fui.Background.cover + fui.Background.blend_lighten),
                    )(P(cls=fui.Text.bold + 'uk-h3')('blend_lighten'))),
    ))

serve(app)