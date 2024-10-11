# AUTOGENERATED! DO NOT EDIT! File to edit: ../06_auth.ipynb.

# %% auto 0
__all__ = ['auth_homepage', 'page']

# %% ../06_auth.ipynb
from fasthtml.common import *
from fasthtml.svg import *
from fh_frankenui import *
from fh_matplotlib import matplotlib2fasthtml
import numpy as np
from pathlib import Path
import matplotlib.pylab as plt

# %% ../06_auth.ipynb
def page():    
    left = Div(cls="col-span-1 hidden flex-col justify-between bg-zinc-900 p-8 text-white lg:flex")(
        Div(cls=(TextB.wt_bold,TextB.sz_medium))("Acme Inc"),
        Blockquote(cls="space-y-2")(
            P(cls=TextB.sz_large)('"This library has saved me countless hours of work and helped me deliver stunning designs to my clients faster than ever before."'),
            Footer(cls=TextB.sz_small)("Sofia Davis")))

    right = Div(cls="col-span-2 flex flex-col p-8 lg:col-span-1")(
        Div(cls="flex flex-none justify-end")(Button("Login", cls=ButtonT.ghost, uk_toggle="#demo")),
        CenteredDiv(cls='flex-1')(
            Div(cls=f"space-y-6 w-[350px]")(
                Div(cls="flex flex-col space-y-2 text-center")(
                    H3("Create an account"),
                    P(cls=TextT.muted_sm)("Enter your email below to create your account")),
                Form(cls='space-y-6')(
                        Input(placeholder="name@example.com"),
                        Button(Span(cls="mr-2", uk_spinner="ratio: 0.54"), "Sign in with Email", cls=(ButtonT.primary, "w-full"), disabled=True),
                        HSplit("Or continue with",cls=TextT.muted_sm),
                        Button(Icon('github',cls='mr-2'), "Github", cls=(ButtonT.default, "w-full"), uk_toggle="#demo")),
                P(cls=(TextT.muted_sm,"text-center"))(
                "By clicking continue, you agree to our ",
                A(cls="underline underline-offset-4 hover:text-primary", href="#demo", uk_toggle=True)("Terms of Service")," and ",
                A(cls="underline underline-offset-4 hover:text-primary", href="#demo", uk_toggle=True)("Privacy Policy"),"."))))
    
    return Grid(left,right,cols=2, gap=0,cls='h-screen')

# %% ../06_auth.ipynb
auth_homepage = page()
