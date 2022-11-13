import os
import subprocess


white_list = ['Thumbs.db', '.DS_Store', '.localized', 'desktop.ini']

for filename in os.listdir():
    if filename in white_list or os.path.isdir(filename):
        continue
    print(filename)
    subprocess.run(["open", filename])
    # os.system(f"open {filename}")
    if input("> ").lower() == "del":
        print("Deleting...\n")
        os.remove(filename)
    else:
        print("Saving.\n")
