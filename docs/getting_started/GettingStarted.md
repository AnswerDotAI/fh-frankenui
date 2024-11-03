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

#### Start by importing the modules with one of these options:

```python
from fasthtml.common import *
from fh_frankenui.core import *
```

#### Instantiate the app with the fh-frankenui headers

```python
app = FastHTML(hdrs=Theme.slate.headers())
app, rt = fast_app(hdrs=Theme.slate.headers())
```

**The color option can be any of the theme options available out of the box**

---

From here, you can explore the API Reference & examples for a full reference.

You can also check out these resources:

+ View the [Fh-FrankenUI Tutorial App](https://fh-frankenui.answer.ai/tutorial_app) to understand how to use the library
+ The [AnswerAI Dev Chat](https://www.youtube.com/watch?v=K5FFPHlWMiY) where Isaac & Jeremy explore the framework
+ This [video](https://www.loom.com/share/0916e8a95d524c43a4d100ee85157624?sid=9be07e55-c962-4dbd-978c-aa6a0bcee7b3) where Isaac iteratively builds a form in 5 minutes with the framework

More resources and improvements to the documentation will be added here soon!

## LLM context files for Fh_FrankenUI

Using LLMs for development is a best practice way to get started and explore.  While LLMs cannot code for you, they can be helpful assistants.  You must check, refactor, test, and vet any code any LLM generates for you - but they are helpful productivity tools.

+ [llms.txt](https://raw.githubusercontent.com/AnswerDotAI/fh-frankenui/refs/heads/main/lib_nbs/llms.txt): Links to the neccesary reference documents to use the fh_frankenui library effectively.  Contains very little information directly in the document.
+ [llms-ctx.txt](https://raw.githubusercontent.com/AnswerDotAI/fh-frankenui/refs/heads/main/lib_nbs/llms-ctx.txt): Fh_FrankenUI specific context only (does not include FastHTML specific context)
+ [llm-ctx-full.txt](https://raw.githubusercontent.com/AnswerDotAI/fh-frankenui/refs/heads/main/lib_nbs/llms-ctx-full.txt): All inclusive FastHTML + FH_Frankenui context


