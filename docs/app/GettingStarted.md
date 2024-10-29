# Fh-FrankenUI

> A FrankenUI wrapper to let you style websites quickly and beautifully with FastHTML.  

*This library is still in active development, however there are many great things you can do with it already.*  

We'd really like you try to it and tell us how it works for you - but please be aware there will improvements to the API over time.  

---

## Installation

#### To install this library, run:

>`pip install git+https://github.com/AnswerDotAI/fh-frankenui.git`

---

## Getting Started

#### Start by importing the modules as follows:

>`from fasthtml.common import *`

>`from fh_frankenui.core import *`

#### Instantiate the app with the fh-frankenui headers

>`app = FastHTML(hdrs=Theme.slate.headers())`
  
*Alternatively, using the fast_app method*
  
>`app, rt = fast_app(pico=False, hdrs=Theme.slate.headers())`

**The color option can be any of the theme options available out of the box**

---

From here, you can explore the API Reference & examples for a full reference.

You can also check out these demo videos to as a quick start guide:

+ The [AnswerAI Dev Chat](https://www.youtube.com/watch?v=K5FFPHlWMiY) where Isaac & Jeremy explore the framework
+ This [video](https://www.loom.com/share/0916e8a95d524c43a4d100ee85157624?sid=9be07e55-c962-4dbd-978c-aa6a0bcee7b3) where Isaac iteratively builds a form in 5 minutes with the framework

More resources and improvements to the documentation will be added here soon!
