# Fh-FrankenUI

> [!WARNING]
>
> This library is still in active development, however there are many
> great things you can do with it already. We’d really like you try to
> it and tell us how it works for you - but please be aware there will
> improvements to the API over time

## Installation

To install this library, uses

`pip install git+https://github.com/AnswerDotAI/fh-frankenui.git`

Check out the docs [here](https://fh-frankenui.answer.ai/)

## Getting Started

To get started, check out:

1.  Start by importing the modules as follows:

``` python
from fasthtml.common import *
from fh_frankenui.core import *
```

2.  Instantiate the app with the fh-frankenui headers

``` python
app = FastHTML(hdrs=Theme.slate.headers())

# Alternatively, using the fast_app method
app, rt = fast_app(pico=False, hdrs=Theme.slate.headers())
```

> *The color option can be any of the theme options available out of the box*


More resources and improvements to the documentation will be added here
soon!
