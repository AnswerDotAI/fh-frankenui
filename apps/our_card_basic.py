from fasthtml.common import *
from fh_frankenui.components import *
from fasthtml.svg import Svg, Path

hdrs = (Script(src="https://cdn.tailwindcss.com"),
        Script(src="https://cdn.jsdelivr.net/npm/uikit@3.21.6/dist/js/uikit.min.js"),
        Script(src="https://cdn.jsdelivr.net/npm/uikit@3.21.6/dist/js/uikit-icons.min.js"),
        Script(type="module", src="https://unpkg.com/franken-wc@0.0.6/dist/js/wc.iife.js"),
        Link(rel="stylesheet", href="https://unpkg.com/franken-wc@0.0.6/dist/css/blue.min.css") )

app = FastHTML(hdrs=hdrs,default_hdrs=False, routes = (Mount('/public', StaticFiles(directory='public')),))


GalleryCard = Card(H3(cls='uk-h3')("Inline Field Validation"),Br(),
            P(cls=TextB.muted)('A form with inline field validation on individual inputs with the submit aditionally validating the whole form.'),
                header=Img(cls='uk-img',src='public/inline_validation.gif',),
                footer=Div(cls=('uk-flex','uk-flex-between'))(
                    UkButton('App', cls=UkButtonT.primary),
                    UkButton('Info', cls=UkButtonT.default),
                    UkButton('Code', cls=UkButtonT.default)),
                # footer_cls='uk-background-muted'
                )

Left1 = Card(
            Div(cls='grid grid-cols-2 gap-6')(
                UkButton(cls=UkButtonT.default)(Span(cls="uk-margin-small-right", uk_icon="icon: github; ratio: 1"),'Github'), 
                UkButton(cls=UkButtonT.default)(Span(cls="uk-margin-small-right", uk_icon="icon: google; ratio: 1"),'Google')), 
            UkHSplit("OR CONTINUE WITH", text_cls = (TextB.xsmall, TextB.muted)),
            UkInput('Email','', 'email',placeholder='m@example.com'),
            UkInput('Password','', 'Password',placeholder='Password',type='Password'), 
            header=(H3(cls='uk-h3')('Create an account'),P(cls=f'{TextT.muted_sm}')('Enter your email below to create your account')),
            footer=UkButton(cls=(UkButtonT.primary,'w-full'))('Create Account'),
            body_cls='space-y-4 py-0'
            )
from fasthtml.svg import Rect
Card1Svg = Svg(xmlns="http://www.w3.org/2000/svg", viewBox="0 0 24 24", fill="none", stroke="currentColor", stroke_linecap="round", stroke_linejoin="round", stroke_width="2", cls="mb-3 h-6 w-6")(Rect(width="20", height="14", x="2", y="5", rx="2"),Path(d="M2 10h20"))
Card2Svg = Svg(role="img", viewBox="0 0 24 24", cls="mb-3 h-6 w-6")(Path(d="M7.076 21.337H2.47a.641.641 0 0 1-.633-.74L4.944.901C5.026.382 5.474 0 5.998 0h7.46c2.57 0 4.578.543 5.69 1.81 1.01 1.15 1.304 2.42 1.012 4.287-.023.143-.047.288-.077.437-.983 5.05-4.349 6.797-8.647 6.797h-2.19c-.524 0-.968.382-1.05.9l-1.12 7.106zm14.146-14.42a3.35 3.35 0 0 0-.607-.541c-.013.076-.026.175-.041.254-.93 4.778-4.005 7.201-9.138 7.201h-2.19a.563.563 0 0 0-.556.479l-1.187 7.527h-.506l-.24 1.516a.56.56 0 0 0 .554.647h3.882c.46 0 .85-.334.922-.788.06-.26.76-4.852.816-5.09a.932.932 0 0 1 .923-.788h.58c3.76 0 6.705-1.528 7.565-5.946.36-1.847.174-3.388-.777-4.471z", fill="currentColor")),
Card3Svg = Svg(role="img", viewBox="0 0 24 24", cls="mb-3 h-6 w-6")(Path(d="M12.152 6.896c-.948 0-2.415-1.078-3.96-1.04-2.04.027-3.91 1.183-4.961 3.014-2.117 3.675-.546 9.103 1.519 12.09 1.013 1.454 2.208 3.09 3.792 3.039 1.52-.065 2.09-.987 3.935-.987 1.831 0 2.35.987 3.96.948 1.637-.026 2.676-1.48 3.676-2.948 1.156-1.688 1.636-3.325 1.662-3.415-.039-.013-3.182-1.221-3.22-4.857-.026-3.04 2.48-4.494 2.597-4.559-1.429-2.09-3.623-2.324-4.39-2.376-2-.156-3.675 1.09-4.61 1.09zM15.53 3.83c.843-1.012 1.4-2.427 1.245-3.83-1.207.052-2.662.805-3.532 1.818-.78.896-1.454 2.338-1.273 3.714 1.338.104 2.715-.688 3.559-1.701", fill="currentColor"))

import calendar
month_opts = [Option(selected=True)(calendar.month_name[1])] + [Option(o) for o in calendar.month_name[2:]]
year_opts = [Option(selected=True)(2024)] + [Option(o) for o in range(2025,2030)]
Left2 = Card(
    Div(cls='grid grid-cols-3 gap-4')(
        UkButton(Div(cls='flex flex-col items-center justify-center')(Card1Svg,"Card"), cls='uk-button-default h-20 w-full border-2 border-primary'),
        UkButton(Div(cls='flex flex-col items-center justify-center')(Card2Svg, "Card"), cls='uk-button-default h-20 w-full'),
        UkButton(Div(cls='flex flex-col items-center justify-center')(Card3Svg, "Apple"), cls='uk-button-default h-20 w-full')),

    Div(cls=' space-y-4')(
    UkInput('Name','', 'name',placeholder='m@example.com'),
    UkInput('Card Number','', 'card_number',placeholder='m@example.com'),
    Div(cls='grid grid-cols-3 gap-4')(
        UkSelect(*month_opts,label='Expires',id='expire_month'),
        UkSelect(*year_opts,label='Year',id='expire_year'),
        UkInput('CVV','', 'cvv',placeholder='CVV'),
    )),
    header=(H3(cls='uk-h3')('Payment Method'),P(cls=f'{TextT.muted_sm}')('Add a new payment method to your account.')),
)
area_opts = ('Team','Billing','Account','Deployment','Support')
severity_opts = ('Severity 1 (Highest)', 'Severity 2', 'Severity 3', 'Severity 4 (Lowest)')
Right1 = Card(
    Div(cls='grid grid-cols-2 gap-2')(
        UkSelect(*[Option(o) for o in area_opts],label='Area',id='area'),
        UkSelect(*[Option(o) for o in severity_opts],label='Severity',id='area')),
    UkInput(label='Subject',placeholder='I need help with'),
    UkTextArea(label='Description',placeholder='Please include all information relevant to your issue'),
    UkFormLabel(label="Tags",state="danger", value="Spam,Invalid"),
    header=(H3('Report an issue'),P(cls=f'{TextT.muted_sm}')('What area are you having problems with')),
    footer = (UkButton(cls=(UkButtonT.ghost))('Cancel'),UkButton(cls=(UkButtonT.primary))('Submit')),
    # footer_cls='flex justify-between'
    )

Right2 = Card(H4(cls='uk-h4')("franken/ui"),
              P(cls=f'{TextT.muted_sm}')("HTML-first, framework-agnostic, beautifully designed components that you can truly copy and paste into your site. Accessible. Customizable. Open Source."),
              Div(cls=f'flex gap-x-4 {TextT.muted_sm}')(
                Div(cls='flex items-center')("TypeScript"),
                Div(cls='flex items-center')(Span(uk_icon='star'),"20k"),
                "Updated April 2023"
              )
              )

Right3 = Card(
    UkSwitch(label = Div(H4(cls='uk-h5')('Strictly Necessary'),P(cls=(TextT.muted_sm,'font-normal'))('These cookies are essential in order to use the website and use its features.')),
                cls='flex items-center justify-between gap-2'),
    UkSwitch(label = Div(H4(cls='uk-h5')('Functional Cookies'),P(cls=(TextT.muted_sm,'font-normal'))('These cookies allow the website to provide personalized functionality.')),
                cls='flex items-center justify-between gap-2'),
    UkSwitch(label = Div(H4(cls='uk-h5')('Performance Cookies'),P(cls=(TextT.muted_sm,'font-normal'))('These cookies help to improve the performance of the website.')),
                cls='flex items-center justify-between gap-2'),

        header=(H3(cls='uk-h4')('Cookie Settings'),P(cls=f'{TextT.muted_sm} mt-1.5')('Manage your cookie settings here.')),
        footer=UkButton(cls=(UkButtonT.default,'w-full'))('Save Preferences'),
)


team_members = [{"name": "Sofia Davis", "email": "m@example.com", "role": "Owner"},{"name": "Jackson Lee", "email": "p@example.com", "role": "Member"},]

options = ((Div('Viewer'),Div(cls=f'{TextT.muted_sm}')('Can view and comment.',)),
        (Div('Developer'),Div(cls=f'{TextT.muted_sm}')('Can view, comment and edit.',)),
        (Div('Billing'),Div(cls=f'{TextT.muted_sm}')('Can view, comment and manage billing.',)),
        (Div('Owner'),Div(cls=f'{TextT.muted_sm}')('Admin-level to all resources.')),)

body = [Div(cls='flex items-center space-x-4')(
        Span(cls='relative flex h-10 w-10 shrink-0 overflow-hidden rounded-full bg-accent')(
            Img(src='https://api.dicebear.com/8.x/lorelei/svg?seed='+member['name'], cls='aspect-square h-full w-full')
        ),
        Div(cls='flex-1')(
            P(member['name'], cls='text-sm font-medium leading-none'),
            P(member['email'], cls=f'{TextT.muted_sm}')
        ),
        UkDropdownButton(member['role'], options, 
        # btn_cls=UkButtonT.default
        ),
    ) for member in team_members]


Middle1 = Card(*body,
        header = (H4('Team Members', cls='uk-h4'),Div('Invite your team members to collaborate.', cls=f'mt-1.5 {TextT.muted_sm}')),)

team_members = [
    {"name": "Olivia Martin", "email": "m@example.com", "role": "Read and write access"},
    {"name": "Isabella Nguyen", "email": "b@example.com", "role": "Read-only access"},
    {"name": "Sofia Davis", "email": "p@example.com", "role": "Read-only access"},
]
options = ("Read and write access", "Read-only access")

body = [Div(cls='flex items-center space-x-4')(
    Span(cls='relative flex h-10 w-10 shrink-0 overflow-hidden rounded-full bg-accent')(
        Img(src='https://api.dicebear.com/8.x/lorelei/svg?seed='+member['name'], cls='aspect-square h-full w-full')
    ),
    Div(cls='flex-1')(
        P(member['name'], cls='text-sm font-medium leading-none'),
        P(member['email'], cls=f'{TextT.muted_sm}')
    ),
    UkSelect(*[Option(o,selected=(member['role']==o)) for o in options]),
) for member in team_members]

Middle2 = Card(
    Div(cls='flex gap-x-2')(
        UkInput(value='http://example.com/link/to/document',cls='flex-1'),
        UkButton(cls=UkButtonT.default)('Copy link')),
    Div(cls='uk-divider-icon my-4'),
    H4(cls='text-sm font-medium')('People with access'),
    *body,
    header = (H4('Share this document', cls='uk-h4'),Div('Anyone with the link can view this document.', cls=f'mt-1.5 {TextT.muted_sm}')),
    # body_cls=''
)

Middle3 = Card(UkButton(cls=UkButtonT.default)('Jan 20, 2024 - Feb 09, 2024'))
Middle4 = Card(
    # Refacto this
    Ul(cls="uk-nav uk-nav-secondary")
    (
        *[Li(cls='-mx-1')(A(cls="", href='#demo', uk_toggle=True)(Div(cls="flex gap-x-4")(Div(uk_icon=icon),Div(cls='flex-1')(P(name),P(cls=f"{TextT.muted_sm}")(desc)))))
            for icon, name, desc in (('bell','Everything',"Email digest, mentions & all activity."),
                                    ('user',"Available","Only mentions and comments"),
                                    ('ban',"Ignoring","Turn of all notifications"))]),
        header = (H4('Notification', cls='uk-h4'),Div('Choose what you want to be notified about.', cls=f'mt-1.5 {TextT.muted_sm}')),
        # body_cls='pt-0'
)

@app.get('/')
def home(): 
    return Title("Basic"),Div(cls=('uk-child-width-1-3@l','uk-child-width-1-2@m'), uk_grid=True)(
            Div(cls='space-y-6')(map(Div,(Left1,Left2,GalleryCard))),
            Div(cls='space-y-6')(map(Div,(Middle1,Middle2,Middle3,Middle4))),
            Div(cls='space-y-6')(map(Div,(Right1,Right2, Right3))),     
    )

serve()
