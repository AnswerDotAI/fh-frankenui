# CONTRIBUTING

## Library Contributions

> The code for all components in the library in the Jupyter notebooks (.ipynb files).   Edit those, not the .py files.

This is an [nbdev](https://nbdev.fast.ai/) library. The notebooks are located in `nbs`.  

### Exporting the Modules

You can use `nbdev_export` to export the notebooks to the library directory, `monsterui`.  

### Cleaning NB metadad

You can use `nbdev_clean` to clean the nb metadata from the .py files.  

## Docs Contributions

The docs are run using [FastHTML](https://fastht.ml/) and can be run locally with:

```bash
cd docs
pip install -r requirements.txt
python main.py
```

This will start up the MonsterUI documentation site, which is a FastHTML app.  Then you can see the site locally at http://localhost:5001/
