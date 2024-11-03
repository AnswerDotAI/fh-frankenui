# CONTRIBUTING

## Library Contributions

> The code for all components in the library in the Jupyter notebooks (.ipynb files).   Edit those, not the .py files.

This is an [nbdev](https://nbdev.fast.ai/) library. The notebooks are located in `nbs`.  

### Exporting the Modules

You can use `nbdev_export` to export the notebooks to the library directory, `fh_frankenui`.  

Another option is to run run `watch_export` from the repo root, which will the nbs export to .py files automatically on modification.It's nice to have this constantly running in a terminal tab.

### Cleaning NB metadad

You can use `nbdev_clean` to clean the nb metadata from the .py files.  For convenience, I recommend using `nbdev_install_hooks` when in this repository to automatically do the clean for you so you don't have to remember to do it.

## Docs Contributions

The docs are run using [FastHTML](https://fastht.ml/) and can be run locally with:

```bash
cd docs
pip install -r requirements.txt
python main.py
```

This will start up the fh-frankenui documentation site, which is a FastHTML app.  Then you can see the site locally at http://localhost:5001/
