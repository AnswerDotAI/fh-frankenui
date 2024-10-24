# CONTRIBUTING

The code for all components lives in the Jupyter notebooks (.ipynb files). 
Edit those, not the .py files.

## Exporting the fh-frankenui modules

This is an [nbdev](https://nbdev.fast.ai/) library. The notebooks are located in lib_nbs.
When you run `watch_export` from the repo root, .py files are exported
into the library directory, `fh_frankenui`:

```bash
watch_export
```

It's nice to have this constantly running in a terminal tab.

## Running the docs locally

In addition to the above, it's nice to have 2 more terminal tabs open to run the
docs from your computer.

In one terminal, from the `docs/` directory you can run `watch_export` to constantly 
watch the notebooks, exporting Python modules from them whenever they change:

```bash
watch_export --nbs . --lib app --force
```

In a second terminal run `main.py` in the docs directory to run the docs locally:

```bash
python main.py
```

This will start up the fh-frankenui documentation site, which is a FastHTML app.
Then you can see the site locally at http://0.0.0.0:5001/
