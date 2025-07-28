# Eggdoc

## Usage

Manual installation

```bash
pip install sphinx myst-parser furo nbsphinx sphinx_codeautolink sphinx_math_dollar sphinx_design sphinx_inline_tabs sphinx_copybutton sphinx_subfigure sphinx-favicon sphinx-togglebutton
```

Via uv

```bash
uv run make html
```

# For github page

Around the github-pages Jekyll behaviour of ignoring top level directories starting with an underscore.
This is solved in a much neater way by creating a .nojekyll in the root of you github-pages which will disable Jekyll as described here and here.

# Refs

- https://pradyunsg.me/furo/
- https://sphinx-design.readthedocs.io/en/latest/badges_buttons.html#badges
- https://mystmd.org/
