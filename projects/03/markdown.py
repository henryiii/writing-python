#!/usr/bin/env uv run


import rich
import click
from rich.markdown import Markdown


def print_markdown(markdown):
    """Print a formatted markdown string with rich."""
    rich.print(Markdown(markdown))


if __name__ == "__main__":
    print_markdown()
