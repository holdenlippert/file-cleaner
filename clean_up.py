import os
import subprocess


def get_ignorelist(filename='ignorelist.txt'):
    try:
        with open(filename) as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return []


ignorelist = get_ignorelist()

for filename in os.listdir():
    if filename in ignorelist or os.path.isdir(filename):
        continue
    print(filename)
    subprocess.run(["open", filename])
    # os.system(f"open {filename}")
    if input("> ").lower() == "del":
        print("Deleting...\n")
        os.remove(filename)
    else:
        print("Saving.\n")
