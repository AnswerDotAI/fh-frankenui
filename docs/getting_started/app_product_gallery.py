from fasthtml.common import *
# fh_frankenui shadows fasthtml components with the same name
from fh_frankenui.core import *
# If you don't want shadowing behavior, you use import frankenui.core as ... style instead

# Get frankenui and tailwind headers via CDN using Theme.blue.headers()
hdrs = Theme.blue.headers()

# fast_app defaults to no Pico, and body classes needed for frankenui theme styling
app, rt = fast_app(hdrs=Theme.blue.headers())

#  Examples Product Data to render in the gallery and detail pages
products = [
    {"name": "Laptop", "price": "$999", "img": "https://picsum.photos/200/100?random=1"},
    {"name": "Smartphone", "price": "$599", "img": "https://picsum.photos/200/100?random=2"},
    {"name": "Headphones", "price": "$199", "img": "https://picsum.photos/200/100?random=3"},
    {"name": "Smartwatch", "price": "$299", "img": "https://picsum.photos/200/100?random=4"},
    {"name": "Tablet", "price": "$449", "img": "https://picsum.photos/200/100?random=5"},
    {"name": "Camera", "price": "$799", "img": "https://picsum.photos/200/100?random=6"},]

def ProductCard(p):
    # Card does lots of boilerplate classes so you can just pass in the content
    return Card( 
        Img(src=p["img"], alt=p["name"], style="width:100%; height:100px; object-fit:cover;"),
        # All components can take a cls argument to add additional styling, see spacing tutorial for what `mt-2` does!
        H4(p["name"], cls="mt-2"),
        # There are helpful Enums, such as TextFont, ButtonT, ContainerT, etc that allow for easy discoverability of class options
        P(p["price"], cls=TextFont.bold_sm),
        Button("Click me!", cls=(ButtonT.primary, "mt-2"), 
               # HTMX can be used as normal on any component
               hx_get=product_detail.to(product_name=p['name']),
               hx_push_url='true',
               hx_target='body'))

@rt
def index():
    # Titled using a H1 title, sets the page title, and wraps contents in Main(Container(...)) using frankenui styles
    return Titled("Example Store Front!",
        Grid(map(ProductCard,products), cols_lg=3))

example_product_description = """\n
This is a sample detailed description of the {product_name}.  You can see when clicking on the card from the gallery you can:

+ Have a detailed description of the product on the page
+ Have an order form to fill out and submit
+ Anything else you want!
"""

@rt
def product_detail(product_name:str):
    return Titled("Product Detail",
        # Grid lays out its children in a responsive grid
        Grid( 
            Div(
                H1(product_name),
                # render_md is a helper that renders markdown into HTML using frankenui styles
                render_md(example_product_description.format(product_name=product_name))),
            Div(
                H3("Order Form"),
                # Form automatically has a class of 'space-y-3' for a margin between each child
                Form( 
                    # LabelInput is a convience wrapper for a label and input that links them
                    LabelInput("Name", id='name'), 
                    LabelInput("Email", id='email'),
                    LabelInput("Quantity", id='quantity'),
                    Button("Submit", cls=ButtonT.primary))
        ),
        # Grid has defaults and args for cols at different breakpoints, but you can pass in your own to customize responsiveness
        cols_lg=2)) 

serve()
