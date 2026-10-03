# Tkinter GUI for Git

> [!NOTE] **Unintended behaviour**
> This may have unintended behaviour on Windows and Linux.

## Description

This is a dead simple GUI for Git, intended for beginners. It's built in tkinter and runs without any external Python packages, only ones included in Python.

## Requirements

- Python 3.15 or above for `main.py`. `legacy.py` will run on older versions of Python.
- [Git](https://git-scm.com/)

## Installation

1. Download either the `main.py` or `legacy.py` file.
2. Ensure python and git are installed on your system.
3. move the python file to the directory that contains your git project. Ensure git is initialised with `git init`.
4. Run the python file with `python3 main.py` or `python legacy.py`.

## Features

The features are intentionally kept simple, with the aim of making it easy to use for beginners.

We have:

- A commit message box and a commit button (automatically adds all the files)
- A push button (only use when connected to a remote repository)
- A pull button (only use when connected to a remote repository)

## Why Python 3.15 or above?

This project imports some modules (like `webbrowser` and `sys`) that may only be used in very specific situations. To speed up startup times, it uses `lazy import`, which only loads the package when used. Lazy imports have only been recently added in Python 3.15.
