import os
import subprocess
import sys
from simple_term_menu import TerminalMenu


KEEP = "Keep"
DELETE = "Delete"

redtext = lambda s: f'\x1b[31m{s}\x1b[0m'


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


def handle_file(filename):
    proc = subprocess.run(["open", filename], capture_output=True, encoding='utf-8')
    if proc.stderr:
        print(redtext(f"There was a problem opening {filename}:"))
        print(redtext(proc.stderr))
    action = prompt(filename)
    if action == DELETE:
        print(f"Deleting {filename}")
        os.remove(filename)
    elif action == KEEP:
        print(f"Keeping {filename}")


def main(argv):
    ignorelist = get_ignorelist()

    for filename in os.listdir():
        if filename in ignorelist or os.path.isdir(filename):
            continue
        handle_file(filename)


if __name__ == "__main__":
    main(sys.argv)
