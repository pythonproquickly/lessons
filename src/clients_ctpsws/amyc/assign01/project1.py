import pathlib
from os.path import exists
import shutil
import os


def get_input():
    while True:
        search = input()
        if len(search) < 4:
            print("ERROR")
            continue
        input_path = search[2:]
        search_type = search[0]
        if search_type in ("DR") and search[1] == " ":
            if exists(input_path):
                break
        print("ERROR")
        continue
    return search_type, input_path


def ls_files(dir):
    files = list()
    for item in os.listdir(dir):
        abspath = os.path.join(dir, item)
        try:
            if os.path.isdir(abspath):
                files = files + ls_files(abspath)
            else:
                files.append(abspath)
        except FileNotFoundError:
            pass
    return files


def display(search_type, input_path):
    path = pathlib.Path(input_path)
    if search_type == "D":
        files = [str(file) for file in path.iterdir() if file.is_file()]
    elif search_type == "R":
        files = ls_files(path.name)
    files = [os.getcwd() + "/" + file for file in files]
    files = sorted(files, key=lambda a: (a.count("/"), (a).lower()))
    display_files(files)
    return files


def display_files(files):
    # files = sorted(files, key=lambda a: (a.count("/"), (a+"/").lower()))
    for file in files:
        print(file)


def filter(files):
    while True:
        action = input()
        interesting = []
        if action == "A" or (len(action) > 3 and action[1] == " "):
            if action == "A":
                interesting = files
            elif action[0] == "N":
                for file in files:
                    if pathlib.Path(file).name == action[2:].strip():
                        interesting.append(file)
            elif action[0] == "E":
                for file in files:
                    if pathlib.Path(file).suffix == action[2:].strip():
                        interesting.append(file)
            elif action[0] == "T":
                for file in files:
                    p = pathlib.Path(file)
                    if not p.is_file():
                        continue
                    with p.open() as f:
                        try:
                            content = f.readlines()
                        except Exception:
                            continue
                        for line in content:
                            if action[2:] in line:
                                interesting.append(file)
            elif action[0] == "<":
                for file in files:
                    if pathlib.Path(file).stat()[6] < int(action[2:].strip()):
                        interesting.append(file)
            elif action[0] == ">":
                for file in files:
                    if pathlib.Path(file).stat()[6] > int(action[2:].strip()):
                        interesting.append(file)
            if not interesting:
                exit()
            display_files(interesting)
            take_action(interesting)

        print("ERROR")
        continue


def take_action(results):
    while True:
        action = input()
        if action == "F":
            for file in results:
                p = pathlib.Path(file)
                if not p.is_file():
                    continue
                with p.open() as f:
                    try:
                        content = f.readlines()
                        print(content[0])
                    except Exception:
                        print("NOT TEXT")
                        continue
        elif action == "D":
            for file in results:
                p = pathlib.Path(file)
                if p.is_dir():
                    continue
                shutil.copy(file, file + ".dup")
        elif action == "T":
            for file in results:
                pathlib.Path(file).touch()
        else:
            print("ERROR")
            continue
        break
    exit()


def main():
    search_type, input_path = get_input()
    files = display(search_type, input_path)
    action_code, condition = filter(files)


if __name__ == "__main__":
    main()
