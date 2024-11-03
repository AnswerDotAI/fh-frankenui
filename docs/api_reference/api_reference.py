"""Reference to all FrankenUI Components"""

from fasthtml.common import *
from fh_frankenui.core import *
from nbdev.showdoc import *
import inspect

from enum import EnumType
from collections.abc import Callable

'''
Any variable starting with docs_ is a function that generates a section of the API reference.

These are automatically added to the docs sidebar so you don't have to do anything other than add the function using create_doc_section.


'''


def enum_to_html_table(enum_class):
    headers = ["Option", "Value"]
    rows = [[name, value.value] for name, value in enum_class.__members__.items()]
    return Div(
        Hr(cls='uk-divider-icon my-4'),
        H3(enum_class.__name__,cls='my-4'),
        P(I(enum_class.__doc__)),
        TableFromLists(headers, rows, cls=(TableT.hover, 'uk-table-small')),)

def render_content(c):
    "Renders content by type"
    if isinstance(c, str):        return render_md(c) # Strings are rendered as markdown
    elif isinstance(c, EnumType): return enum_to_html_table(c) # Enums are rendered as tables
    elif isinstance(c, FT):       return c # FastHTML tags are rendered as themselves
    elif isinstance(c, tuple): # Tuples are rendered as cards with source and output that are flippable
        _id = 'f'+str(unqid())
        _card = Card(
            Button(
                DivFullySpaced(UkIcon('corner-down-right', 20, 20, 3),"See Source"), 
                uk_toggle=f"target: #{_id}", id=_id, cls=ButtonT.primary),
            Button(
                DivFullySpaced(UkIcon('corner-down-right', 20, 20, 3),"See Output"), 
                uk_toggle=f"target: #{_id}", id=_id, cls=ButtonT.primary, hidden=True),
            Div(c[0], id=_id),
            Div(Pre(Code(c[1])), id=_id, hidden=True, cls="mockup-code"),
            cls='my-8')
        if len(tuple(c)) == 3: return Div(_card, cls=c[2]) # If there is a third element, it is a class to apply to the card
        else: return _card        
    elif isinstance(c, Callable): # Callables are rendered as documentation via show_doc
        _html = show_doc(c, renderer=BasicHtmlRenderer)._repr_html_()
        return NotStr(apply_classes(_html, class_map_mods={"table":'uk-table uk-table-hover uk-table-small'}))
    else: return c    

def create_doc_section(*content, title):
    return lambda: Titled(H1(title,cls='mb-10'), *map(render_content, content))

def string2code_string(code: str) -> tuple: return eval(code), code

def extract_function_body(func):
    source = inspect.getsource(func)
    body_start = source.index(':') + 1
    body = source[body_start:]
    lines = body.split('\n')
    # Remove empty lines at the start
    while lines and not lines[0].strip():
        lines.pop(0)
    # Remove first 4 spaces from each line
    body = '\n'.join(line[4:] if line.startswith('    ') else line for line in lines)
    return body.replace('return ', '', 1)

def fn2code_string(fn: Callable) -> tuple: return fn(), extract_function_body(fn)

def ex_buttons(): 
    return Div(
        Button("Default",   cls=ButtonT.default),
        Button("Primary",   cls=ButtonT.primary),
        Button("Secondary", cls=ButtonT.secondary),
        Button("Danger",    cls=ButtonT.danger),
        Button("Text",      cls=ButtonT.text),
        Button("Link",      cls=ButtonT.link),
        Button("Ghost",     cls=ButtonT.ghost),
        )

def ex_links(): 
    return Div(cls='space-x-4')(
        A('Default Link'),
        A('Muted Link', cls=AT.muted),
        A('Text Link',  cls=AT.text),
        A('Reset Link', cls=AT.reset))

docs_button_link = create_doc_section(
    Button, 
    fn2code_string(ex_buttons),
    ButtonT, 
    A,
    AT,
    fn2code_string(ex_links),
    title="Buttons & Links")

def ex_headings():
    return Div(
        Titled("Titled"),
        H1("Level 1 Heading (H1)"), 
        H2("Level 2 Heading (H2)"), 
        H3("Level 3 Heading (H3)"), 
        H4("Level 4 Heading (H4)")
        )

docs_heading = create_doc_section(
                       fn2code_string(ex_headings),
                        H1, H2, H3, H4, Titled,
                        title="Headings")

def ex_theme_switcher():
    from fasthtml.components import Uk_theme_switcher
    return Uk_theme_switcher()

docs_theme_headers = create_doc_section( 
   "To get headers with a default theme use `hdrs=Theme.<color>.headers()`.  For example for the blue theme you would use `hdrs=Theme.blue.headers()`.  Theme options are:",
    "> Note: Tailwind is included in the headers for convenience",
    Card(Grid(map(P,Theme)),cls='mb-8'),
    H3("Theme Picker"),
    fn2code_string(ex_theme_switcher),
    "Themes are controlled with `bg-background text-foreground` classes on the `Body` tag.  `fast_app` and `FastHTML` will do this for you automatically so you typically do not have to do anything",
    fast_app,
    FastHTML,
    title="Headers")

def ex_textfont():
    return Div(
    P('muted_sm', cls=TextFont.muted_sm),
    P('muted_lg', cls=TextFont.muted_lg), 
    P('bold_sm', cls=TextFont.bold_sm),
    )

def ex_textt():
    return Grid(
        P('lead',           cls=TextT.lead),
        P('meta',           cls=TextT.meta),
        P('italic',         cls=TextT.italic),
        P('small',          cls=TextT.small),
        P('default',        cls=TextT.default),
        P('large',          cls=TextT.large),
        P('light',          cls=TextT.light),
        P('normal',         cls=TextT.normal),
        P('bold',           cls=TextT.bold),
        P('lighter',        cls=TextT.lighter),
        P('bolder',         cls=TextT.bolder),
        P('capitalize',     cls=TextT.capitalize),
        P('uppercase',      cls=TextT.uppercase),
        P('lowercase',      cls=TextT.lowercase),
        P('decoration_none',cls=TextT.decoration_none),
        P('muted',          cls=TextT.muted),
        P('primary',        cls=TextT.primary),
        P('secondary',      cls=TextT.secondary),
        P('success',        cls=TextT.success),
        P('warning',        cls=TextT.warning),
        P('danger',         cls=TextT.danger),
        P('left',           cls=TextT.left),
        P('right',          cls=TextT.right),
        P('center',         cls=TextT.center),
        P('justify',        cls=TextT.justify),
        P('top',            cls=TextT.top),
        P('middle',         cls=TextT.middle),
        P('bottom',         cls=TextT.bottom),
        P('baseline',       cls=TextT.baseline),
        P('truncate',       cls=TextT.truncate),
        P('break_',         cls=TextT.break_),
        P('nowrap',         cls=TextT.nowrap),
        )

docs_text = create_doc_section( 
   "Styling text is possibly the most common style thing to do, so we have a couple of helpers for discoverability inside python.  `TextFont` is intended to be combinations are are widely applicable and used often, where `TextT` is intended to be more flexible options for you to combine together yourself.",
    fn2code_string(ex_textfont),
    TextFont,
    fn2code_string(ex_textt),
    TextT,

    title="Text Style")

def ex_articles():
    return Article(
        ArticleTitle("Sample Article Title"), 
        ArticleMeta("By: John Doe"),
        P('lorem ipsum dolor sit amet consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'))

def ex_containers():
    return Container(
        "This is a sample container with custom styling.",
        cls=ContainerT.xsmall,
        style="background-color: #FFA500; color: #000000")

docs_containers = create_doc_section(
    ArticleMeta,
    ArticleTitle,
    Article,
    fn2code_string(ex_articles),
    Container,
    ContainerT,
    fn2code_string(ex_containers),
    Section,
    SectionT,
    title="Articles, Containers & Sections"
)

def ex_card():
    return Card(
        Form(LabelInput("Input"),
             LabelRange("Range")),
        header=Div(
            CardTitle("Header"),
            P("A card with header and footer",cls=TextFont.muted_sm)),
        footer=DivLAligned(Button("Footer Submit Button")))

def Tags(cats): return Div(cls='space-x-2')(map(Label, cats))

def ex_card2_wide():
    def Tags(cats): return Div(cls='space-x-2')(map(Label, cats))

    return Card(
        DivLAligned(
            A(Img(src="https://picsum.photos/200/200?random=12", style="width:200px"),href="#"),
            Div(cls='space-y-3 uk-width-expand')(
                H4("Creating Custom FastHTML Tags for Markdown Rendering"),
                P("A step by step tutorial to rendering markdown in FastHTML using zero-md inside of DaisyUI chat bubbles"),
                DivFullySpaced(map(Span, ["Isaac Flath", "20-October-2024"]), cls=TextFont.muted_sm),
                DivFullySpaced(
                    Tags(["FastHTML", "HTMX", "Web Apps"]),
                    Button("Read", cls=(ButtonT.primary,'h-6'))))))


def ex_card2_tall():
    def Tags(cats): return Div(cls='space-x-2')(map(Label, cats))

    return Card(
        Div(
            A(Img(src="https://picsum.photos/200/200?random=14"),href="#"),
            Div(cls='space-y-3 uk-width-expand')(
                H4("Creating Custom FastHTML Tags for Markdown Rendering"),
                P("A step by step tutorial to rendering markdown in FastHTML using zero-md inside of DaisyUI chat bubbles"),
                DivFullySpaced(map(Span, ["Isaac Flath", "20-October-2024"]), cls=TextFont.muted_sm),
                DivFullySpaced(
                    Tags(["FastHTML", "HTMX", "Web Apps"]),
                    Button("Read", cls=(ButtonT.primary,'h-6'))))))



docs_cards = create_doc_section(
    Card,
    H3("Example Usage"),
    fn2code_string(ex_card),
    (*fn2code_string(ex_card2_wide),'uk-visible@s'),
    (*fn2code_string(ex_card2_tall),'uk-hidden@s'),
    CardTitle,
    CardT,
    "The remainder of these are only needed if you're doing something really special.  They are used in the `Card` function to generate the boilerplate for you.",
    CardContainer,
    CardHeader,
    CardBody,
    CardFooter,
    title="Cards"
)

def ex_lists():
    list_options = [(style,str(cls)) for style,cls in ListT.__members__.items()]
    lists = [Div(H4(f"{style} List:"), List(Li("Item 1"), Li("Item 2"), cls=cls)) for style, cls in list_options]
    return Grid(*lists)

docs_lists = create_doc_section(
    List,
    fn2code_string(ex_lists),
    ListT,
    title="Lists")

def ex_md(): 
    return render_md('''# Test MD

+ A list with **bold** and *italics*
+ And a link to [answer.ai](https://answer.ai)''')

def ex_applyclasses():
    return apply_classes('<h1>Hello, World!</h1><p>This is a paragraph</p>')
        
        
docs_markdown = create_doc_section(render_md, 
                             fn2code_string(ex_md), 
                             P("This uses the `apply_classes` function, which can be used to apply classes to html strings"),
                             apply_classes,
                             fn2code_string(ex_applyclasses),
                             title="Markdown")

def ex_formlabel(): 
    return FormLabel("Form Label")

def ex_input(): 
    return Div(
        Input(placeholder="Enter text"), 
        LabelInput(label="Input", id='myid'))

def ex_checkbox(): 
    return Div(
        CheckboxX(), 
        LabelCheckboxX(label="Checkbox", id='checkbox1'))
def ex_range(): 
    return Div(
        Range(), 
        LabelRange(label="Range", id='range1'))
def ex_switch(): 
    return Div(
        Switch(id="switch"), 
        LabelSwitch(label="Switch", id='switch'))

def ex_textarea(): 
    return Div(
        TextArea(placeholder="Enter multiple lines of text"), 
        LabelTextArea(label="TextArea", id='myid'))

def ex_radio(): 
    return Div(
        Radio(name="radio-group", id="radio1"), 
        LabelRadio(label="Radio", id='radio1',cls='flex items-center space-x-4'))

def ex_ukselect(): 
    return Div(
        UkSelect(map(Option, ["Option 1", "Option 2", "Option 3"])),
        LabelUkSelect(map(Option, ["Option 1", "Option 2", "Option 3"]), label="UkSelect", id='myid'))

def ex_select(): 
    return Div(
        Select(map(Option, ["Option 1", "Option 2", "Option 3"])),
        LabelSelect(map(Option, ["Option 1", "Option 2", "Option 3"]), label="Select", id='myid'))

def ex_progress(): 
    return Progress(value=20, max=100)

def ex_form():
    relationship = ["Parent",'Sibling', "Friend", "Spouse", "Significant Other", "Relative", "Child", "Other"]
    return Div(cls='space-y-4')(
        DivCentered(
            H3("Emergency Contact Form"),
            P("Please fill out the form completely", cls=TextFont.muted_sm)),
        Form(cls='space-y-4')(
            Grid(LabelInput("First Name",id='fn'), LabelInput("Last Name",id='ln')),
            Grid(LabelInput("Email",     id='em'), LabelInput("Phone",    id='ph')),
            H3("Relationship to patient"),
            Grid(*[LabelCheckboxX(o) for o in relationship], cols=4, cls='space-y-3'),
            LabelInput("Address",        id='ad'),
            LabelInput("Address Line 2", id='ad2'),
            Grid(LabelInput("City",      id='ct'), LabelInput("State",    id='st')),
            LabelInput("Zip",            id='zp'),
            DivCentered(Button("Submit Form", cls=ButtonT.primary))))

docs_forms = create_doc_section(
    H3("Example Form"),
    P(f"This form was live coded in a 5 minute video ",
          A("here",href="https://www.loom.com/share/0916e8a95d524c43a4d100ee85157624?start_and_pause=1", 
            cls=AT.muted), cls=TextFont.muted_sm),
    fn2code_string(ex_form),
    FormLabel,
    fn2code_string(ex_formlabel),
    Input,
    fn2code_string(ex_input),
    Progress,
    fn2code_string(ex_progress),
    Radio,
    fn2code_string(ex_radio),
    CheckboxX,
    fn2code_string(ex_checkbox),
    Range,
    fn2code_string(ex_range),
    Switch,
    fn2code_string(ex_switch),
    TextArea,
    fn2code_string(ex_textarea),
    Select,
    fn2code_string(ex_select),
    UkSelect,
    fn2code_string(ex_ukselect),
    Legend,
    Fieldset,
    title="Forms")

def ex_modal():
    return Div(
        Button("Open Modal",uk_toggle="target: #my-modal" ),
        Modal(ModalTitle("Simple Test Modal"), 
              P("With some somewhat brief content to show that it works!", cls=TextFont.muted_sm),
              footer=ModalCloseButton("Close", cls=ButtonT.primary),id='my-modal'))

docs_modals = create_doc_section(
    H3("Example Modal"),
    fn2code_string(ex_modal),
    Modal,
    ModalCloseButton,
    P("The remainder of the Modal functions below are used internally by the `Modal` function for you.  You shouldn't need to use them unless you're doing something really special."),
    ModalTitle,
    ModalFooter,
    ModalBody,
    ModalHeader,
    ModalDialog,
    ModalContainer,
    title="Modals")

def ex_grid():
    return Grid(
        Div(
            P("Column 1 Item 1"), 
            P("Column 1 Item 2"), 
            P("Column 1 Item 3")),
        Div(
            P("Column 2 Item 1"), 
            P("Column 2 Item 2"), 
            P("Column 2 Item 3")),
        Div(
            P("Column 3 Item 1"), 
            P("Column 3 Item 2"), 
            P("Column 3 Item 3")))

def ex_product_grid():
    products = [
        {"name": "Laptop", "price": "$999", "img": "https://picsum.photos/200/100?random=1"},
        {"name": "Smartphone", "price": "$599", "img": "https://picsum.photos/200/100?random=2"},
        {"name": "Headphones", "price": "$199", "img": "https://picsum.photos/200/100?random=3"},
        {"name": "Smartwatch", "price": "$299", "img": "https://picsum.photos/200/100?random=4"},
        {"name": "Tablet", "price": "$449", "img": "https://picsum.photos/200/100?random=5"},
        {"name": "Camera", "price": "$799", "img": "https://picsum.photos/200/100?random=6"},
    ]
    
    product_cards = [
        Card(
            Img(src=p["img"], alt=p["name"], style="width:100%; height:100px; object-fit:cover;"),
            H4(p["name"], cls="mt-2"),
            P(p["price"], cls=TextFont.bold_sm),
            Button("Add to Cart", cls=(ButtonT.primary, "mt-2"))
        ) for p in products
    ]
    
    return Grid(*product_cards, cols_lg=3)


def ex_fully_spaced_div():
    return DivFullySpaced(
        Button("Left", cls=ButtonT.primary),
        Button("Center", cls=ButtonT.secondary),
        Button("Right", cls=ButtonT.danger)
    )

def ex_centered_div():
    return DivCentered(
        H3("Centered Title"),
        P("This content is centered both horizontally and vertically.")
    )

def ex_l_aligned_div():
    return DivLAligned(
        Img(src="https://picsum.photos/100/100?random=1", style="max-width: 100px;"),
        H4("Left Aligned Title"),
        P("Some text that's left-aligned with the title and image.")
    )

def ex_r_aligned_div():
    return DivRAligned(
        Button("Action", cls=ButtonT.primary),
        P("Right-aligned text"),
        Img(src="https://picsum.photos/100/100?random=3", style="max-width: 100px;")
    )

def ex_v_stacked_div():
    return DivVStacked(
        H2("Vertical Stack"),
        P("First paragraph in the stack"),
        P("Second paragraph in the stack"),
        Button("Action Button", cls=ButtonT.secondary)
    )

def ex_h_stacked_div():
    return DivHStacked(
        Div(H4("Column 1"), P("Content for column 1")),
        Div(H4("Column 2"), P("Content for column 2")),
        Div(H4("Column 3"), P("Content for column 3"))
    )

docs_layout = create_doc_section(
    P("This page covers `Grid`s, which are often used for general structure, `Flex` which is often used for layout of components that are not grid based, padding and positioning that can help you make your layout look good, and dividers that can help break up the page", cls=TextFont.muted_sm),
    H2("Grid"),
    fn2code_string(ex_grid),
    Grid,
    H4("Practical Grid Example"),
    fn2code_string(ex_product_grid),
    H2("Flex"),
    P("Play ", 
      A("Flex Box Froggy", href="https://flexboxfroggy.com/", cls=AT.muted), 
      " to get an understanding of flex box.",
      cls=TextFont.muted_sm),
    DivFullySpaced,
    fn2code_string(ex_fully_spaced_div),
    DivCentered,
    fn2code_string(ex_centered_div),
    DivLAligned,
    fn2code_string(ex_l_aligned_div),
    DivRAligned,
    fn2code_string(ex_r_aligned_div),
    DivVStacked,
    fn2code_string(ex_v_stacked_div),
    DivHStacked,
    fn2code_string(ex_h_stacked_div),
    FlexT,

    H2("Padding and Positioning"),
    PaddingT,
    PositionT,
    title="Layout")

def ex_dividers():
    return Div(
        P("Small Divider"),
        Divider(cls=DividerT.small),
        DivCentered(
            P("Vertical Divider"),
            Divider(cls=DividerT.vertical)),
        DivCentered("Icon Divider"),
        Divider(cls=DividerT.icon))

def ex_dividersplit():
    return DividerSplit(P("Or continue with", cls=TextFont.muted_sm))
def ex_dividerline():
    return DividerLine()

docs_dividers = create_doc_section(
    Divider,
    DividerT,
    fn2code_string(ex_dividers),
    DividerSplit,
    fn2code_string(ex_dividersplit),
    DividerLine,
    fn2code_string(ex_dividerline),
    title="Dividers")

def ex_nav1():
    mbrs1 = [Li(A('Option 1'), cls='uk-active'), Li(A('Option 2')), Li(A('Option 3'))]
    return NavContainer(*mbrs1)

def ex_nav2():
    mbrs1 = [Li(A('Option 1'), cls='uk-active'), Li(A('Option 2')), Li(A('Option 3'))]
    mbrs2 = [Li(A('Child 1')), Li(A('Child 2')),Li(A('Child 3'))]

    return NavContainer(
        NavHeaderLi("NavHeaderLi"),
        *mbrs1,
        Li(A(href='')(Div("Subtitle Ex",NavSubtitle("NavSubtitle text to be shown")))),
        NavDividerLi(),
        NavParentLi(
            A('Parent Name'),
            NavContainer(*mbrs2,parent=False),
             ),
    )

def ex_navbar():
    mbrs1 = [Li(A('Option 1'), cls='uk-active'), Li(A('Option 2')), Li(A('Option 3'))]
    mbrs2 = [Li(A('Child 1')), Li(A('Child 2')),Li(A('Child 3'))]

    lnav = NavBarNav(Li(cls='uk-active')(A("Active",href='')),
        Li(A("Parent",href=''),
          NavBarNavContainer(
              Li(cls='uk-active')(A("Active",href='')),
              Li(A("Item",href='')),
              Li(A("Item",href='')))),
        Li(A("Item",href='')))

    rnav = NavBarNav(
        Li(cls='uk-active')(A(NavBarSubtitle("Title","Subtitle"),href='')),
        Li(A("DropDown",NavBarParentIcon(),href=''),
            NavBarNavContainer(
                NavHeaderLi("NavHeaderLi"),
                *mbrs1,
                Li(A(href='')(Div("Subtitle Ex",NavSubtitle("NavSubtitle text to be shown")))),
                NavDividerLi(),
                NavParentLi(
                    A('Parent Name'),
                    NavContainer(*mbrs2,parent=False)))),
        Li(A(NavBarSubtitle("Title","Subtitle"),href='')))
    
    return NavBarContainer(
        NavBarLSide(lnav),
        NavBarRSide(rnav))

def ex_navdrop():
    return Div(
        Button("Open DropDown"),
        DropDownNavContainer(Li(A("Item 1",href=''),Li(A("Item 2",href='')))))

def ex_tabs1():
    return Container(
        TabContainer(
            Li(A("Active",href='#', cls='uk-active')),
            Li(A("Item",href='#')),
            Li(A("Item",href='#')),
            Li(A("Disabled",href='#', cls='uk-disabled')),
            uk_switcher='connect: #component-nav; animation: uk-animation-fade',
            alt=True),
         Ul(id="component-nav", cls="uk-switcher")(
            Li(H1("Tab 1")),
            Li(H1("Tab 2")),
            Li(H1("Tab 3"))))


def ex_tabs2():
    return Container(
        TabContainer(
            Li(A("Active",href='javascript:void(0);', cls='uk-active')),
            Li(A("Item",href='javascript:void(0);')),
            Li(A("Item",href='javascript:void(0);')),
            Li(A("Disabled", cls='uk-disabled'))))

docs_navigation = create_doc_section(
    H1("Nav, NavBar, DowDownNav, and Tab examples"),
    Divider(),
    H2("Nav"),
    fn2code_string(ex_nav1),
    fn2code_string(ex_nav2),
    H2("Navbars"),
    fn2code_string(ex_navbar),
    H2("Drop Down Navs"),
    fn2code_string(ex_navdrop),
    H2("Tabs"),
    fn2code_string(ex_tabs2),
    P("A tabs can use any method of navigation (htmx, or href).  However, often these are use in conjunction with switchers do to this client side", cls=TextFont.muted_sm),
    fn2code_string(ex_tabs1),
    H1("API Docs"),
    Nav,
    NavT,
    NavContainer,
    NavCloseLi,
    NavSubtitle,
    NavHeaderLi,
    NavDividerLi,
    NavParentLi,
    NavBarCenter,
    NavBarRSide,
    NavBarLSide,
    NavBarContainer,
    NavBarNav,
    NavBarSubtitle,
    NavBarNavContainer,
    NavBarParentIcon,
    DropDownNavContainer,
    TabContainer,
    title="Navigation")


def ex_tables0():
    return Table(
        Thead(Tr(Th('Name'),    Th('Age'), Th('City'))),
        Tbody(Tr(Td('Alice'),   Td('25'),  Td('New York')),
              Tr(Td('Bob'),     Td('30'),  Td('San Francisco')),
              Tr(Td('Charlie'), Td('35'),  Td('London'))),
        Tfoot(Tr(Td('Total'),   Td('90'))))

def ex_tables1():
    header =  ['Name',    'Age', 'City']
    body   = [['Alice',   '25',  'New York'],
              ['Bob',     '30',  'San Francisco'],
              ['Charlie', '35',  'London']]
    footer =  ['Total',   '90']
    return TableFromLists(header, body, footer)

def ex_tables2():
    def body_render(k, v):
        match k.lower():
            case 'name': return Td(v, cls='font-bold')
            case 'age':  return Td(f"{v} years")
            case _:      return Td(v)

    header_data = ['Name',          'Age',     'City']
    body_data   =[{'Name': 'Alice', 'Age': 30, 'City': 'New York'},
                  {'Name': 'Bob',   'Age': 25, 'City': 'London'}]

    return TableFromDicts(header_data, body_data, 
        header_cell_render=lambda v: Th(v.upper()), 
        body_cell_render=body_render)

docs_tables = create_doc_section(
    fn2code_string(ex_tables0),
    fn2code_string(ex_tables1),
    fn2code_string(ex_tables2),
    Table,
    TableFromLists,
    TableFromDicts,
    TableT,
    Tbody,
    Th,
    Td,
    Tfoot,
    Thead,
    Tr,    
    title="Tables")

def ex_dicebear():
    return DivLAligned(
        DiceBearAvatar('Isaac Flath',10,10),
        DiceBearAvatar('Aaliyah',10,10),
        DiceBearAvatar('Alyssa',10,10))

def ex_icon():
    return Grid(
        UkIcon('chevrons-right', height=15, width=15),
        UkIcon('bug',            height=15, width=15),
        UkIcon('phone-call',     height=15, width=15),
        UkIcon('maximize-2',     height=15, width=15),
        UkIcon('thumbs-up',      height=15, width=15),)        

def ex_iconlink():
    return DivLAligned(
        UkIconLink('chevrons-right'),
        UkIconLink('chevrons-right', button=True, cls=ButtonT.primary))

docs_icons = create_doc_section(
    H1("Avatars"),
    fn2code_string(ex_dicebear),
    DiceBearAvatar,
    H1("Icons"),
    P("Icons use Lucide icons - you can find a full list of icons in their docs.", cls=TextFont.muted_sm),
    fn2code_string(ex_icon),
    UkIcon,
    fn2code_string(ex_iconlink),
    UkIconLink,
    title="Icons")

def ex_markdown():
    md = '''# Example Markdown

+ With **bold** and *italics*
+ With a [link](https://github.com)

### And a subheading

> This is a blockquote
'''
    return render_md(md)

docs_markdown = create_doc_section(
    fn2code_string(ex_markdown),
    render_md,
    apply_classes,
    title="Markdown + HTML Frankification")
