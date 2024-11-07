from fasthtml.common import *
from fh_frankenui.core import *
from utils import create_flippable_card, fn2code_string

def prerequisites():
    return Section(
        H2("Prerequisites"),
        P("""The fh-FrankenUI library automatically handles a lot of styling for you, but it assumes you structure your page with HTML.
          If you aren't familiar with the basics of HTML, check out the """, 
          A("W3 Schools HTML references", href="https://www.w3schools.com/html", cls=AT.muted), 
          " to learn more about the basics of HTML."),
        cls='my-4 py-4'
    )

def next_steps():
    return Section(
        H2("Next Steps"),
        P("""Once you have a good grasp of HTML, you can reference the following resources to continue to expand your capabilities.  Instead of trying to learn all of these, focus on the ones that are relevant to something specific you want to do."""),
        List(map(Li, [
          A("Improving Aesthetics with Spacing", href="https://frankenui.fasthtml.io/docs/getting_started/SpacingTutorial", cls=AT.muted), 
          A("Manipulating Page and Element Layout", href="https://frankenui.fasthtml.io/docs/getting_started/LayoutTutorial", cls=AT.muted), 
          A("FlexBox Froggy", href="https://flexboxfroggy.com/", cls=AT.muted),
          A("Accessibility", href="https://frankenui.fasthtml.io/docs/getting_started/Accessibility", cls=AT.muted),
        ]), cls=ListT.bullet),
        cls='my-4 py-4'
    )

def page():
    return Article(
        ArticleTitle("Styling Rules of Thumb"),
        ArticleMeta("A guide to making a pretty good looking website in a hurry"),
        prerequisites(),
        next_steps(),
        # button_section(),
        # typography_section(),
    )


def accessibility_section():
    # TODO: Alt tags
    # TODO: Aria labels
    # TODO: High contrast
    # TODO: Prefers reduced motion
    pass 

def further_reading():
    # TODO: Tailwind CSS
    # TODO: FlexBox Froggy
    # TODO: Accessibility
    pass 

def button_section():
   def _ex_buttons():
       return Form(
           Grid(LabelInput("Email"),
                LabelInput("Name"), 
                cols=2), 
           Grid(Button("Submit Information", cls=ButtonT.primary),
                Button("Delete Information", cls=ButtonT.danger),
                Button("Cancel"),
                cols=3)
       )

   return Section(
        H2("Pick button styles based on desired behavior"),
        Blockquote("The aethetic of a button should match the desired behavior",cls='uk-blockquote mb-8'),
        Strong("What to do:"),
        List(
            Li("Use ButtonT.primary for the most important actions (ie add to card, checkout, etc.)"),
            Li("Use ButtonT.secondary for actions that are important but not the primary action (ie save, etc.)"),
            Li("Use ButtonT.danger for destructive actions"),
            Li("Use default styling for UX actions (ie go cancel, close etc.)"),
            cls=ListT.bullet
        ),
        create_flippable_card(*fn2code_string(_ex_buttons)),
        cls='my-4 py-4'
    )

def typography_section():
    def _ex_typography():
        return Div(cls='space-y-5')(
            Div(cls='space-y-3')(
                H1("The main heading"),
                Blockquote("A section describing easy ways to make generally good looking text"),
            ),
            Div(cls='space-y-3')(
                H2("My First Section"),
                P("A short description of what's in this section", cls=TextFont.muted_sm),
                P("""Now I can write the main content of the page with a normal P tag.  
                We can use this for longer text like paragraphs.
                It's ideal because this text is highly readable.
                I can write longer sentences and paragraphs without is being really hard to read with highly styled text.
                Often if you aren't careful with styling you can make the text hard to read, especially if you aren't thinking about light vs dark backgrounds.
                """))
        )


    return Section(
        H2("Use consistent typography"),
        Blockquote("Consistency is key to a polished user experience",cls='uk-blockquote mb-8'),
        Strong("What to do:"),
        List(
            Li("Use H1-4 for headings"),
            Li("Use P with cls=TextFont.muted_sm subheadings like "),
            Li("Use P for most body text"),
            cls=ListT.bullet),
        create_flippable_card(*fn2code_string(_ex_typography)),
        cls='my-4 py-4'
    )

