"""FrankenUI Music Example"""

from fasthtml.common import *
from fh_frankenui.core import *
 
def SpacedPP(left, right=None): return DivFullySpaced(NavP(left),NavP(right) if right else '')

def SpacedPPs(*c): return [SpacedPP(*tuplify(o)) for o in c]

def NavP(*c, cls=TextFont.muted_sm): return P(cls=cls)(*c)

def LAlignedTxtIcon(txt, icon, width=None, height=None, stroke_width=None, cls='space-x-2', icon_right=True, txt_cls=None):
    # Good for navbards
    c = (txt if isinstance(txt, FT) else NavP(txt,cls=ifnone(txt_cls,TextFont.muted_sm)),UkIcon(icon=icon, height=height, width=width, stroke_width=stroke_width))
    if not icon_right: c = reversed(c)
    return DivLAligned(*c, cls=cls)

def MusicLi(t,hk=''): return Li(A(DivFullySpaced(t,P(hk,cls=TextFont.muted_sm))))

music_items = [("About Music", ""),("Preferences", "⌘"),("Hide Music", "⌘H"),("Hide Others", "⇧⌘H"),("Quit Music", "⌘Q")]

file_dd_items = [("New", ""),("Open Stream URL", "⌘U"),("Close Window", "⌘W"),("Library", ""),("Import", "⌘O"),
    ("Burn Playlist to Disc", ""),("Show in Finder", "⇧⌘R"),("Convert", ""),("Page Setup", "Print")]

edit_actions = [("Undo", "⌘Z"),("Redo", "⇧⌘Z"),("Cut", "⌘X"),("Copy", "⌘C"),
    ("Paste", "⌘V"),("Select All", "⌘A"),("Deselect All", "⇧⌘A")]

view_dd_data = ["Show Playing Next", "Show Lyrics", "Show Status Bar", "Hide Sidebar", "Enter Full Screen"]

account_dd_data = [Span("Switch Account", cls="ml-6"), [SpacedPP("Andy"), LAlignedTxtIcon("Benoit", 'plus-circle', 0.5, icon_right=False), SpacedPP("Luis")],
                   SpacedPPs("Manage Family"), SpacedPPs("Add Account")]

music_headers =NavBarContainer(
    NavBarLSide(
        NavBarNav(
            Li(A("Music"),NavBarNavContainer(map(lambda x: MusicLi(*x), music_items))),
            Li(A("File"),NavBarNavContainer(map(lambda x: MusicLi(*x), file_dd_items))),
            Li(A("Edit")),
                NavBarNavContainer(
                    *map(lambda x: MusicLi(*x), edit_actions),
                    Li(A(DivFullySpaced("Smart Dictation",UkIcon("mic")))),
                    Li(A(DivFullySpaced("Emojis & Symbols",UkIcon("globe"))))),
            Li(A("View"),
               NavBarNavContainer(map(lambda x: MusicLi(x), view_dd_data))),
            Li(A("Account"),
                NavBarNavContainer(
                    NavHeaderLi("Switch Account"),
                    MusicLi("Andy"),
                    MusicLi("Benoit"),
                    MusicLi("Luis"),
                    MusicLi("Manage Family"),
                    MusicLi("Add Account"))),
        cls='space-x-4')))

def AlbumImg(url):
    return Div(cls="overflow-hidden rounded-md")(Img(cls="transition-transform duration-200 hover:scale-105", src=url))

def AlbumFooter(title, artist):
    return Div(cls='space-y-1')(P(title,cls=TextT.bold),P(artist,cls=TextT.muted))

def Album(url,title,artist):
    return Div(AlbumImg(url),AlbumFooter(title,artist))

listen_now_albums = (("Roar", "Catty Perry"), ("Feline on a Prayer", "Cat Jovi"),("Fur Elise", "Ludwig van Beethovpurr"),("Purrple Rain", "Prince's Cat"))

made_for_you_albums = [("Like a Feline", "Catdonna"),("Livin' La Vida Purrda", "Ricky Catin"),("Meow Meow Rocket", "Elton Cat"),
        ("Rolling in the Purr", "Catdelle",),("Purrs of Silence", "Cat Garfunkel"),("Meow Me Maybe", "Carly Rae Purrsen"),]
    

def create_album_grid(albums, cols=4):  
    return Grid(*[Div(cls="uk-grid-small")(
                Div(cls="overflow-hidden rounded-md")(
                    Img(cls="transition-transform duration-200 hover:scale-105", src=img_url, alt="")),
                Div(cls="space-y-1 text-sm")(
                    H3(album['title'], cls="font-medium leading-none"),
                    P(album['artist'], cls="text-xs text-muted-foreground"))) for album in albums],
                cols,gap=4)

_album = lambda t,a: Album('https://ucarecdn.com/e5607eaf-2b2a-43b9-ada9-330824b6afd7/music1.webp',t,a)

music_content = (Div(H3("Listen Now"), cls="mt-6 space-y-1"),
                    P("Top picks for you. Updated daily.",cls=TextFont.muted_sm),
                    DividerLine(),
                    Grid(*[_album(t,a) for t,a in listen_now_albums], cols=4, cols_lg=4,cls='gap-8'),
                    Div(H3("Made for You"), cls="mt-6 space-y-1"),
                    P("Your personal playlists. Updated daily.", cls=TextFont.muted_sm),
                    DividerLine(),
                    Grid(*[_album(t,a) for t,a in made_for_you_albums], cols=6))

tabs = TabContainer(
    Li(A('Music', href='#'),cls='uk-active'),
    Li(A('Podcasts', href='#')),
    Li(A('Live', cls='opacity-50'), cls='uk-disabled'),
    uk_switcher='connect: #component-nav; animation: uk-animation-fade',
    alt=True)

def podcast_tab():
    return Div(
        Div(cls="space-y-3")(
            H3("New Episodes"),
            P("Your favorite podcasts. Updated daily.", cls=TextFont.muted_sm)),
        Div(cls="my-4 h-[1px] w-full bg-border"),
        Div(cls="uk-placeholder flex h-[450px] items-center justify-center rounded-md",uk_placeholder=True)(
            Div(cls="text-center space-y-6")(
                UkIcon("microphone", 3),
                H4("No episodes added"),
                P("You have not added any podcasts. Add one below.", cls=TextFont.muted_sm),
                Button("Add Podcast", cls=ButtonT.primary))))

def LAlignedIconTxts(ns, icns): return [Li(A(LAlignedIconTxt(n,i))) for n,i in zip(ns,icns)]

discoved_data = [("play-circle","Listen Now"), ("binoculars", "Browse"), ("rss","Radio")]
library_data = [("play-circle", "Playlists"), ("music", "Songs"), ("user", "Made for You"), ("users", "Artists"), ("bookmark", "Albums")]
playlists_data = [("library","Recently Added"), ("library","Recently Played")]

def MusicSidebarLi(icon, text): return Li(A(DivLAligned(UkIcon(icon), P(text),cls='space-x-2')))
sb = NavContainer(
    NavHeaderLi(H3("Discover")),*[MusicSidebarLi(*o) for o in discoved_data],
    NavHeaderLi(H3("Library")),*[MusicSidebarLi(*o) for o in library_data],
    NavHeaderLi(H3("Playlists")),*[MusicSidebarLi(*o) for o in playlists_data],
    cls=(NavT.primary,'space-y-3','pl-8'),
)

def page():
    return Div(Container(music_headers,cls='py-8'), DividerSplit(),
        Grid(sb,
            Div(cls="col-span-4 border-l border-border")(
                Div(cls="px-8 py-6")(
                    Div(cls="flex items-center justify-between")(
                        Div(cls="max-w-80")(tabs),
                        Button(cls=ButtonT.primary)(Span(cls="mr-2 size-4")(UkIcon('circle-plus')),"Add music")),
                    Ul(id="component-nav", cls="uk-switcher")(
                        Li(*music_content),
                        Li(podcast_tab())))),
            cols=5))

music_homepage = page()