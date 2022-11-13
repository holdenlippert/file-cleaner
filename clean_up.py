import os
import subprocess
from simple_term_menu import TerminalMenu


KEEP = "Keep"
DELETE = "Delete"


def get_ignorelist(filename='ignorelist.txt'):
    try:
        with open(filename) as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return []


def prompt(filename):
    options = [KEEP, DELETE]
    title = f"What would you like to do with {filename}?"
    terminal_menu = TerminalMenu(options, title=title)
    selection = terminal_menu.show()
    return options[selection]


ignorelist = get_ignorelist()

for filename in os.listdir():
    if filename in ignorelist or os.path.isdir(filename):
        continue
    subprocess.run(["open", filename])
    action = prompt(filename)
    if action == DELETE:
        print(f"Deleting {filename}")
        os.remove(filename)
    elif action == KEEP:
        print(f"Keeping {filename}")
