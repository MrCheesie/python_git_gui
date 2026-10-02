#!/usr/bin/env python3

"""
Created on Fri Oct 2 2:01pm 2026

@author: Alris Dhanwani
"""

import os
import webbrowser
from pydoc import text
import subprocess
from tkinter import *  # pyright: ignore[reportWildcardImportFromLibrary]
from tkinter import messagebox

VERSION: str = "0.0.1"

# init tkinter
WINDOW = Tk()
WINDOW.title(f"Git GUI {VERSION}")
WINDOW.geometry("200x200")
# make widgets
commit_msg_entry = Entry(WINDOW)



def commit(commit_msg) -> str:
    subprocess.run(['git', 'add', '.'], check=True)
    commit_result = subprocess.run(['git', 'commit', '-m', f"\"{commit_msg}\""], shell=False, check=True, text=True, capture_output=True)
    return commit_result.stdout

def push() -> str:
    result = subprocess.run(['git', 'push'], check=True, text=True, capture_output=True)
    return result.stdout or result.stderr

def pull() -> str:
    result = subprocess.run(['git', 'pull'], check=True, capture_output=True, text=True)
    return result.stdout


def on_commit():
    message: str = commit_msg_entry.get().strip()

    if message:
        messagebox.showinfo("Commit successful", commit(commit_msg=message))
        commit_msg_entry.delete(0, "end")
    else:
        messagebox.showwarning("Error", "Enter a commit message")

def on_push() -> None:
    try:
        messagebox.showinfo("Push successful", push())
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Push failed", e.stderr or str(e))

def on_pull() -> None:
    messagebox.showinfo("Push successful", message=pull())

# more widgets
commit_button = Button(
    WINDOW,
    text="Commit",
    command=on_commit
)

push_button = Button(WINDOW, text="Push", command=on_push)
pull_button = Button(WINDOW, text="Pull", command=on_pull)

commit_msg_entry.grid(row=1, column=0, sticky=W)
commit_msg_entry.insert(0, "Enter commit message here")
commit_button.grid(row=2, column=0)
push_button.grid(row=3, column=0)
pull_button.grid(row=4, column=0)

# -- Menu --
menu_bar = Menu(WINDOW)
WINDOW.config(menu=menu_bar)
credit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Credits', menu=credit_menu)
credit_menu.add_command(label="Made by Alris Dhanwani", command=lambda: webbrowser.open("https://github.com/MrCheesie/"))
credit_menu.add_command(label="GitHub Repo", command=lambda: webbrowser.open("https://github.com/MrCheesie/python_git_gui"))


# main func
def main():
    # check if git repo
    if not os.path.isdir(".git"):
        print("fatal: Not a git repo")
    else:
        print("is a git repo")

    WINDOW.mainloop() # run the main loop


if __name__ == '__main__':
    main()
