from fasthtml.common import *
import fh_frankenui.core as fui

app = FastHTML(hdrs=fui.Theme.blue.headers())

def get_header(text):
    return Div(Br(),P(cls=fui.Text.center + fui.H.h2 + fui.Background.primary + 'my-class')(text),Br())

def get_explanation(text):
    return Div(P(cls=fui.Text.small + fui.Text.muted)(text),Br())


@app.get("/")
async def index():
    return Div(
        get_header("Text"),
        get_explanation("Text is used to style text. It is a nested enum that allows you to style text in a variety of ways."),
        Div(cls=fui.Column.six)( *[P(cls=e)(e.name) for e in fui.Text],),

        get_header("Button"),
        Strong('A: '),*[A(cls=e)(e.name) for e in fui.Button],
        Br(),
        Strong('Button: '),*[Button(cls=e)(e.name) for e in fui.Button],

        get_header("Width"),
        *[Button(cls=fui.Button.default + e)(e.name) for e in fui.Width],

        get_header("Column"),
        Div(cls=fui.Column.two)(*[P(cls=fui.Background.muted)("two")]*2),Br(),
        Div(cls=fui.Column.three)(*[P(cls=fui.Background.muted)("three")]*3),Br(),
        Div(cls=fui.Column.four)(*[P(cls=fui.Background.muted)("four")]*4),Br(),
        Div(cls=fui.Column.five)(*[P(cls=fui.Background.muted)("five")]*5),Br(),
        Div(cls=fui.Column.six)(*[P(cls=fui.Background.muted)("six")]*6),Br(),
        
        get_header('Background'),
        Div(uk_grid='', cls='uk-child-width-1-3@s uk-grid-small uk-child-width-1-2')(
            *[show_background(e) for e in fui.Background],),

        get_header("Cards"),
        Div(uk_grid='', cls='uk-child-width-1-2@m uk-grid-small uk-grid-match')(
            *[basic_card(e) for e in fui.Card if e in [fui.Card.default, fui.Card.primary, fui.Card.secondary, fui.Card.danger]],

        # advanced_card(),
            
        )
    )


def show_background(e: fui.Background):
    return Div(
        P(cls=fui.Text.bold + fui.H.h3)(e.name),
        Div(cls=fui.Background.primary + fui.Background.cover + e,
                   style='background-image: url(https://avatars.githubusercontent.com/u/6256508?v=4); height: 500px;')(
        ))

def basic_card(e: fui.Card):
    return Div(Div(cls=fui.Card.base + fui.Card.body + e)(
        H3(cls=fui.Card.title)(e.name),
        P(cls='uk-margin')('Lorem ipsum dolor sit amet, consectetur adipisicing elit.')
    ))
# def advanced_card():
#     return Div(cls='uk-width-1-2@m uk-card')(
#     Div(cls=fui.Card.header)(
#         H3('Create project', cls=fui.Card.title),
#         P('Deploy your new project in one-click.', cls=fui.Text.small + 'uk-margin-small-top' +  'text-muted-foreground')
#     ),
#     Div(cls=fui.Card.body + 'uk-padding-remove-top uk-padding-remove-bottom')(
#         Div(cls='')(
#             Label('Name', fr='name', cls='uk-form-label'),
#             Input(id='name', type='text', aria_describedby='name-help-block', placeholder='Name', cls='uk-input uk-margin-small-top'),
#             Div('The name of your project.', id='name-help-block', cls='uk-form-help uk-margin-small-top')
#         ),
#         Div(cls='uk-margin')(
#             Label('Framework', fr='framework', cls='uk-form-label'),
#             Select(name='framework', id='framework', cls='uk-select uk-margin-small-top')(
#                 Option('Sveltekit', value='sveltekit'),
#                 Option('Astro', value='astro')
#             )
#         )
#     ),
#     Div(cls=fui.Card.footer + 'uk-flex uk-flex-between')(
#         Button('Cancel', cls=fui.Button.default),
#         Button('Deploy', cls=fui.Button.primary)
#     )
# )

serve()