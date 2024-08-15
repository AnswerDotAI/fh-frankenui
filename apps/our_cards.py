from fasthtml.common import *
from fh_frankenui.components import *
from fasthtml.components import Uk_select


hdrs = (Script(src="https://cdn.tailwindcss.com"),
        Script(src="https://cdn.jsdelivr.net/npm/uikit@3.21.6/dist/js/uikit.min.js"),
        Script(src="https://cdn.jsdelivr.net/npm/uikit@3.21.6/dist/js/uikit-icons.min.js"),
        Link(rel="stylesheet", href="https://unpkg.com/franken-wc@0.0.6/dist/css/blue.min.css") 
)
app = FastHTML(hdrs=hdrs,default_hdrs=False, routes = (Mount('/public', StaticFiles(directory='public')),))


GalleryCard = Card(H3(cls='uk-h3')("Inline Field Validation"),Br(),
            P(cls='uk-text-muted')('A form with inline field validation on individual inputs with the submit aditionally validating the whole form.'),
                header=Img(cls='uk-img',src='public/inline_validation.gif',),
                footer=Div(cls=('uk-flex','uk-flex-between'))(
                    UkButton('App', cls=UkButtonT.primary),
                    UkButton('Info', cls=UkButtonT.default),
                    UkButton('Code', cls=UkButtonT.default)),
                footer_cls='uk-background-muted',
             )

Left1 = Card(
            Div(cls='grid grid-cols-2 gap-6')(
                # https://getuikit.com/docs/icon#library
                UkButton(cls=UkButtonT.default)(Span(cls="uk-margin-small-right", uk_icon="icon: github; ratio: 1"),'Github'), 
                UkButton(cls=UkButtonT.default)(Span(cls="uk-margin-small-right", uk_icon="icon: google; ratio: 1"),'Google')), 
            UkHSplit("or continue with", text_cls = "text-xs uppercase uk-text-muted"),
            UkInput('Email','', 'email',placeholder='m@example.com'),
            UkInput('Password','', 'Password',placeholder='Password',type='Password'), 
            header=(H3(cls='uk-h3')('Create an account'),P(cls='text-sm uk-text-muted')('Enter your email below to create your account')),
            footer=UkButton(cls=(UkButtonT.primary,'w-full'))('Create Account'),
            body_cls='space-y-4 py-0')

box2svg = Svg(role="img", viewBox="0 0 24 24", cls="mb-3 h-6 w-6")(Path(d="M7.076 21.337H2.47a.641.641 0 0 1-.633-.74L4.944.901C5.026.382 5.474 0 5.998 0h7.46c2.57 0 4.578.543 5.69 1.81 1.01 1.15 1.304 2.42 1.012 4.287-.023.143-.047.288-.077.437-.983 5.05-4.349 6.797-8.647 6.797h-2.19c-.524 0-.968.382-1.05.9l-1.12 7.106zm14.146-14.42a3.35 3.35 0 0 0-.607-.541c-.013.076-.026.175-.041.254-.93 4.778-4.005 7.201-9.138 7.201h-2.19a.563.563 0 0 0-.556.479l-1.187 7.527h-.506l-.24 1.516a.56.56 0 0 0 .554.647h3.882c.46 0 .85-.334.922-.788.06-.26.76-4.852.816-5.09a.932.932 0 0 1 .923-.788h.58c3.76 0 6.705-1.528 7.565-5.946.36-1.847.174-3.388-.777-4.471z", fill="currentColor")),

import calendar

Left2 = Card(
    Div(cls='grid grid-cols-3 gap-4')(
        UkButton(Div(cls='flex flex-col items-center justify-center')(Span(uk_icon='credit-card'),"Card"), cls='uk-button-default h-20 w-full border-2 border-primary'),
        UkButton(box2svg,cls='uk-button-default h-20 w-full')("Card"),
        UkButton(Span(uk_icon='apple'),"Apple",cls='uk-button-default h-20 w-full')),
    
    Div(cls=' space-y-4')(
    UkInput('Name','', 'name',placeholder='m@example.com'),
    UkInput('Card Number','', 'card_number',placeholder='m@example.com'),
    Div(cls='grid grid-cols-3 gap-4')(
        UkDropdownButton('Month', calendar.month_name, btn_cls=UkButtonT.default),
        UkDropdownButton('Year', range(2024,2030), btn_cls=UkButtonT.default),
        UkInput('','', 'cvv',placeholder='CVV'),
    )),
    header=(H3(cls='uk-h3')('Payment Method'),P(cls='text-sm uk-text-muted')('Add a new payment method to your account.')),
)

Right1 = Card(
    Div(cls="uk-drop uk-dropdown", uk_dropdown=True)(
            Ul(cls="uk-dropdown-nav uk-nav")(
                Li(cls="uk-active")(A(href="#")('Active')),
                Li(A(href="#")('Item')),
                Li(cls="uk-nav-header")('Header'),
                Li(A(href="#")('Item')),
                Li(A(href="#")('Item')),
                Li(cls="uk-nav-divider"),
                Li(A(href="#")('Item')))),
    header=(H3('Report an issue'),P(cls='text-sm uk-text-muted')('What area are you having problems with')),
    footer = (UkButton(cls=(UkButtonT.ghost))('Cancel'),UkButton(cls=(UkButtonT.primary))('Submit')),
    footer_cls='flex justify-between')

Right2 = Card(H4(cls='uk-h4')("franken/ui"),
              P(cls='text-sm text-muted-foreground')("HTML-first, framework-agnostic, beautifully designed components that you can truly copy and paste into your site. Accessible. Customizable. Open Source."),
              Div(cls='flex space-x-4 text-sm text-muted-foreground')(
              Div(cls='flex items-center')("TypeScript"),
              Div(cls='flex items-center')(Span(uk_icon='star'),"20k"),
              "Updated April 2023"
              )
              )

Right3 = Card(
    UkInput(label = Div(H4(cls='uk-h5')('Strictly Necessary'),P(cls='font-normal leading-snug text-muted-foreground')('These cookies are essential in order to use the website and use its features.')),
                inp_cls='uk-toggle-switch uk-toggle-switch-primary flex-none',
                cls='flex items-center justify-between gap-2'),
    UkInput(label = Div(H4(cls='uk-h5')('Functional Cookies'),P(cls='font-normal leading-snug text-muted-foreground')('These cookies allow the website to provide personalized functionality.')),
                inp_cls='uk-toggle-switch uk-toggle-switch-primary flex-none',
                cls='flex items-center justify-between gap-2'),
    UkInput(label = Div(H4(cls='uk-h5')('Performance Cookies'),P(cls='font-normal leading-snug text-muted-foreground')('These cookies help to improve the performance of the website.')),
                inp_cls='uk-toggle-switch uk-toggle-switch-primary flex-none',
                cls='flex items-center justify-between gap-2'),

        header=(H3(cls='font-semibold leading-none tracking-tight')('Cookie Settings'),P(cls='text-sm uk-text-muted')('Manage your cookie settings here.')),
        body_cls='space-y-6 py-0',
        footer=UkButton(cls=(UkButtonT.default,'w-full'))('Save Preferences'),
)


team_members = [{"name": "Sofia Davis", "email": "m@example.com", "role": "Owner"},{"name": "Jackson Lee", "email": "p@example.com", "role": "Member"},]

options = ((Div('Viewer'),Div(cls='text-sm text-muted-foreground')('Can view and comment.',)),
        (Div('Developer'),Div(cls='text-sm text-muted-foreground')('Can view, comment and edit.',)),
        (Div('Billing'),Div(cls='text-sm text-muted-foreground')('Can view, comment and manage billing.',)),
        (Div('Owner'),Div(cls='text-sm text-muted-foreground')('Admin-level to all resources.')),)

body = [Div(cls='flex items-center space-x-4')(
        Span(cls='relative flex h-10 w-10 shrink-0 overflow-hidden rounded-full bg-accent')(
            Img(src='https://api.dicebear.com/8.x/lorelei/svg?seed='+member['name'], cls='aspect-square h-full w-full')
        ),
        Div(cls='flex-1')(
            P(member['name'], cls='text-sm font-medium leading-none'),
            P(member['email'], cls='text-sm text-muted-foreground')
        ),
        UkDropdownButton(member['role'], options, btn_cls=UkButtonT.default),
    ) for member in team_members]


Middle1 = (Card(*body,
    body_cls='space-y-6',
    header = (H4('Team Members', cls='uk-h4'),Div('Invite your team members to collaborate.', cls='mt-1.5 text-sm text-muted-foreground'))
))

team_members = [
    {"name": "Olivia Martin", "email": "m@example.com", "role": "Member"},
    {"name": "Isabella Nguyen", "email": "b@example.com", "role": "Viewer"},
    {"name": "Sofia Davis", "email": "p@example.com", "role": "Viewer"},
]

options = (
    (Div('Viewer'), Div(cls='text-sm text-muted-foreground')('Can view and comment.')),
    (Div('Developer'), Div(cls='text-sm text-muted-foreground')('Can view, comment and edit.')),
    (Div('Billing'), Div(cls='text-sm text-muted-foreground')('Can view, comment and manage billing.')),
    (Div('Owner'), Div(cls='text-sm text-muted-foreground')('Admin-level to all resources.')),
)

body = [Div(cls='flex items-center space-x-4')(
    Span(cls='relative flex h-10 w-10 shrink-0 overflow-hidden rounded-full bg-accent')(
        Img(src='https://api.dicebear.com/8.x/lorelei/svg?seed='+member['name'], cls='aspect-square h-full w-full')
    ),
    Div(cls='flex-1')(
        P(member['name'], cls='text-sm font-medium leading-none'),
        P(member['email'], cls='text-sm text-muted-foreground')
    ),
    UkDropdownButton(member['role'], options, btn_cls=UkButtonT.default),
) for member in team_members]

Middle2 = Card(
    Div(cls='flex gap-x-2')(
        UkInput(value='http://example.com/link/to/document',cls='flex-1'),
        UkButton(cls=UkButtonT.default)('Copy link')),
    Div(cls='uk-divider-icon my-4'),
    H4(cls='text-sm font-medium')('People with access'),
    *body,
    body_cls='space-y-6',
    header = (H4('Share this document', cls='uk-h4'),Div('Anyone with the link can view this document.', cls='mt-1.5 text-sm text-muted-foreground'))
)

Middle3 = Card()
Middle4 = Card(
        header = (H4('Notification', cls='uk-h4'),Div('Choose what you want to be notified about.', cls='mt-1.5 text-sm text-muted-foreground'))

)
# Ul(cls='uk-nav uk-nav-secondary')(
#     Li(cls='-mx-1')(A(href='#demo', uk_toggle='', role='button', cls='')(
#             Div(cls='flex gap-x-4')(
#                 Div(cls='flex-1')(P('Everything'),P('Email digest, mentions & all activity.', cls='text-sm text-muted-foreground'))))),
#     Li(cls='uk-active -mx-1')(
#         A(href='#demo', uk_toggle='', role='button', cls='')(
#             Div(cls='flex gap-x-4')(
#                 Div(cls='flex-1')(
#                     P('Available'),
#                     P('Only mentions and comments.', cls='text-sm text-muted-foreground')
#                 )
#             )
#         )
#     ),
#     Li(cls='-mx-1')(
#         A(href='#demo', uk_toggle='', role='button', cls='')(
#             Div(cls='flex gap-x-4')(Div(cls='flex-1')(P('Ignoring'),P('Turn off all notifications.', cls='text-sm text-muted-foreground')
#                 )
#             )
#         )
#     )
# )


@app.get('/')
def home(): 


    

    return Div(cls=('uk-child-width-1-3@l','uk-child-width-1-2@m'), uk_grid=True)(
            Div(cls='space-y-6')(map(Div,(Left1,Left2))),
            Div(cls='space-y-6')(map(Div,(Middle1,Middle2,Middle3,Middle4))),
            Div(cls='space-y-6')(map(Div,(Right1,Right2, Right3))),        

            GalleryCard

            
    )

serve()
