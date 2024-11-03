"""FrankenUI Cards Example"""

from fasthtml.common import *
import fasthtml.common as fh
from fasthtml.components import Uk_input_tag
from fasthtml.svg import *
from fh_frankenui import *
from fh_frankenui.core import *
 
import calendar

CreateAccount = Card(Grid(Button(UkIcon('github',cls='uk-margin-small-right'),'Github'),
                  Button(UkIcon('google',cls='uk-margin-small-right'),'Google'),
                  cols=2,cls='gap-6'),
            DividerSplit("OR CONTINUE WITH", text_cls = (TextT.small, TextT.muted)),
            LabelInput('Email',    id='email',   placeholder='m@example.com'),
            LabelInput('Password', id='password',placeholder='Password', type='Password'),
            header=(H3('Create an account'),P(cls=TextFont.muted_sm)('Enter your email below to create your account')),
            footer=Button(cls=(ButtonT.primary,'w-full'))('Create Account'),
            body_cls='space-y-4 py-0')

Card1Svg = Svg(viewBox="0 0 24 24", fill="none", stroke="currentColor", stroke_linecap="round", stroke_linejoin="round", stroke_width="2", cls="h-6 w-6 mr-1")(Rect(width="20", height="14", x="2", y="5", rx="2"),Path(d="M2 10h20"))
Card2Svg = Svg(role="img", viewBox="0 0 24 24", cls="h-6 w-6 mr-1")(Path(d="M7.076 21.337H2.47a.641.641 0 0 1-.633-.74L4.944.901C5.026.382 5.474 0 5.998 0h7.46c2.57 0 4.578.543 5.69 1.81 1.01 1.15 1.304 2.42 1.012 4.287-.023.143-.047.288-.077.437-.983 5.05-4.349 6.797-8.647 6.797h-2.19c-.524 0-.968.382-1.05.9l-1.12 7.106zm14.146-14.42a3.35 3.35 0 0 0-.607-.541c-.013.076-.026.175-.041.254-.93 4.778-4.005 7.201-9.138 7.201h-2.19a.563.563 0 0 0-.556.479l-1.187 7.527h-.506l-.24 1.516a.56.56 0 0 0 .554.647h3.882c.46 0 .85-.334.922-.788.06-.26.76-4.852.816-5.09a.932.932 0 0 1 .923-.788h.58c3.76 0 6.705-1.528 7.565-5.946.36-1.847.174-3.388-.777-4.471z", fill="currentColor")),
AppleSvg = Svg(role="img", viewBox="0 0 24 24", cls="h-6 w-6 mr-1")(Path(d="M12.152 6.896c-.948 0-2.415-1.078-3.96-1.04-2.04.027-3.91 1.183-4.961 3.014-2.117 3.675-.546 9.103 1.519 12.09 1.013 1.454 2.208 3.09 3.792 3.039 1.52-.065 2.09-.987 3.935-.987 1.831 0 2.35.987 3.96.948 1.637-.026 2.676-1.48 3.676-2.948 1.156-1.688 1.636-3.325 1.662-3.415-.039-.013-3.182-1.221-3.22-4.857-.026-3.04 2.48-4.494 2.597-4.559-1.429-2.09-3.623-2.324-4.39-2.376-2-.156-3.675 1.09-4.61 1.09zM15.53 3.83c.843-1.012 1.4-2.427 1.245-3.83-1.207.052-2.662.805-3.532 1.818-.78.896-1.454 2.338-1.273 3.714 1.338.104 2.715-.688 3.559-1.701", fill="currentColor"))

PaymentMethod = Card(
    Grid(
        Button(DivCentered(Card1Svg, "Card"),  cls='h-20 w-full border-2 border-primary'),
        Button(DivCentered(Card2Svg, "Card"),  cls='h-20 w-full'),
        Button(DivCentered(AppleSvg, "Apple"), cls='h-20 w-full'),
        cols=3,cls='gap-6'),
    Div(cls='space-y-4')(
        LabelInput('Name',        id='name',        placeholder='John Doe'),
        LabelInput('Card Number', id='card_number', placeholder='m@example.com'),
        Grid(LabelUkSelect(*Options(*calendar.month_name[1:],selected_idx=0),label='Expires',id='expire_month'),
             LabelUkSelect(*Options(*range(2024,2030),selected_idx=0),       label='Year',   id='expire_year'),
             LabelInput('CVV', id='cvv',placeholder='CVV'),
             cols=3,cls='gap-4')),
    header=(H3('Payment Method'),P(cls=TextFont.muted_sm)('Add a new payment method to your account.')))

area_opts = ('Team','Billing','Account','Deployment','Support')
severity_opts = ('Severity 1 (Highest)', 'Severity 2', 'Severity 3', 'Severity 4 (Lowest)')
ReportIssue = Card(
    Grid(Div(LabelUkSelect(*Options(*area_opts),    label='Area',    id='area')),
         Div(LabelUkSelect(*Options(*severity_opts),label='Severity',id='area')),
         cols=2),
    LabelInput(    label='Subject',    placeholder='I need help with', id='subject'),
    LabelTextArea( label='Description',placeholder='Please include all information relevant to your issue', id='description'),
    Div(FormLabel('Tags', fr='#tags'),
        Uk_input_tag(name="Tags",state="danger", value="Spam,Invalid", uk_cloak=True, id='tags')),
    header=(H3('Report an issue'),P(cls=TextFont.muted_sm)('What area are you having problems with')),
    footer = DivFullySpaced(Button(cls=ButtonT.ghost  )('Cancel'),
                            Button(cls=ButtonT.primary)('Submit')))


FlexBlockCentered = (FlexT.block,FlexT.center)

franken_desc ="HTML-first, framework-agnostic, beautifully designed components that you can truly copy and paste into your site. Accessible. Customizable. Open Source."
FrankenUI = Card(H4("franken/ui"),
              P(cls=TextFont.muted_sm)(franken_desc),
              Div(cls=('flex','gap-x-4',TextFont.muted_sm))(
                Div(cls=FlexBlockCentered)("TypeScript"),
                Div(cls=FlexBlockCentered)(UkIcon('star'),"20k"),"Updated April 2023"))

CookieSettings = Card(
    Div(H5('Strictly Necessary'),
        P(cls=(TextFont.muted_sm,TextT.normal))('These cookies are essential in order to use the website and use its features.'),
        Switch(),
        cls=(*FlexBlockCentered, FlexT.between, 'gap-2')),
    Div(H5('Functional Cookies'),
        P(cls=(TextFont.muted_sm,TextT.normal))('These cookies allow the website to provide personalized functionality.'),
        Switch(),
        cls=(*FlexBlockCentered, FlexT.between, 'gap-2')),
    Div(H5('Performance Cookies'),
        P(cls=(TextFont.muted_sm,TextT.normal))('These cookies help to improve the performance of the website.'),
        Switch(),
        cls=(*FlexBlockCentered, FlexT.between, 'gap-2')),
    header=(H4('Cookie Settings'),P(cls=(TextFont.muted_sm, 'mt-1.5'))('Manage your cookie settings here.')),
    footer=Button(cls=(ButtonT.primary, 'w-full'))('Save Preferences'),)

team_members = [("Sofia Davis", "m@example.com", "Owner"),("Jackson Lee", "p@example.com", "Member"),]

body = [Div(cls=(*FlexBlockCentered, 'space-x-4'))(
        DiceBearAvatar(n, 10,10),
        Div(cls='flex-1')(
            P(n, cls='text-sm font-medium leading-none'),
            P(e, cls=TextFont.muted_sm)),
        Button(r),
        DropDownNavContainer(map(NavCloseLi, [
            A(Div('Viewer',    NavSubtitle('Can view and comment.'))),
            A(Div('Developer', NavSubtitle('Can view, comment and edit.'))),
            A(Div('Billing',   NavSubtitle('Can view, comment and manage billing.'))),
            A(Div('Owner',     NavSubtitle('Admin-level access to all resources.')))]
                 )),
    ) for n,e,r in team_members]

TeamMembers = Card(*body,
        header = (H4('Team Members'),Div('Invite your team members to collaborate.', cls=('mt-1.5', TextFont.muted_sm))),)

access_roles = ("Read and write access", "Read-only access")
team_members = [("Olivia Martin", "m@example.com", "Read and write access"),
                ("Isabella Nguyen", "b@example.com", "Read-only access"),
                ("Sofia Davis", "p@example.com", "Read-only access")]

ShareDocument = Card(
    Div(cls='flex gap-x-2')(
        Input(value='http://example.com/link/to/document',cls='flex-1'),
        Button('Copy link')),
    Div(cls='uk-divider-icon my-4'),
    H4(cls=TextFont.bold_sm)('People with access'),
    *[DivLAligned(
        DiceBearAvatar(n, 10,10),
        Div(cls='flex-1')(
            P(n, cls='text-sm font-medium leading-none'),
            P(e, cls=TextFont.muted_sm)),
        UkSelect(*Options(*access_roles, selected_idx=access_roles.index(r))), cls='gap-4') for n,e,r in team_members],
    header = (H4('Share this document'),Div('Anyone with the link can view this document.', cls=('mt-1.5',TextFont.muted_sm))))

DateCard = Card(Button('Jan 20, 2024 - Feb 09, 2024'))

section_content =(('bell','Everything',"Email digest, mentions & all activity."), 
                  ('user',"Available","Only mentions and comments"),
                  ('ban',"Ignoring","Turn of all notifications"))

Notifications = Card(
    NavContainer(
    *[Li(cls='-mx-1')(A(Div(cls="flex gap-x-4")(UkIcon(icon),Div(cls='flex-1')(P(name),P(cls=TextFont.muted_sm)(desc)))))
            for icon, name, desc in section_content],
        cls=NavT.secondary),
    header = (H4('Notification'),Div('Choose what you want to be notified about.', cls=('mt-1.5', TextFont.muted_sm))),
    body_cls='pt-0')

def page():
    return Title("Custom"),Grid(
            *map(lambda x: Div(x, cls='space-y-4'),(
                      (PaymentMethod,CreateAccount),
                      (TeamMembers, ShareDocument,DateCard,Notifications),
                      (ReportIssue,FrankenUI,CookieSettings))),
         cols_lg=3,
       )

cards_homepage = page()
