## Writing Software in Python

## Outline

The focus today: learning how to go from research code to something reusable with structure.

We are also trying not to overlap with the packaging session tomorrow! Be sure to visit that one too.

- Scripts instead of notebooks
- Writing a CLI (built-in)
- Scripts with dependencies
- Writing a CLI (using a dependency)
- Tools for packaging
- Making a reproducible environment
- Task runners

## Installation

I recommend doing this on your computer, so you'll have something to take home. Let's install:

- uv: Brew (macOS), pipx, command line: <https://github.com/astral-sh/uv>
- pixi: Brew (macOS), command line: <https://pixi.sh/latest>
- nox: Brew (macOS), pipx

Optional:

- pipx: Brew (macOS), pip, etc: <https://pipx.pypa.io/stable>
- Python launcher for Unix: Brew, command line: <https://python-launcher.app/install>

## Running the slides

```bash
uv tool install jupyterlab --with jupyterlab_rise --with jupyterlab_code_formatter
jupyter-lab .
```