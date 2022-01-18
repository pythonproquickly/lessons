import pathlib
from os.path import exists
import shutil


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


def display(search_type, input_path):
    # stop condition
    # if not input_path:
    #    return []
    path = pathlib.Path(input_path)
    if search_type == "D":
        files = [str(file) for file in path.iterdir() if file.is_file()]
    elif search_type == "R":
        files = [str(file) for file in path.glob("**/*") if file.is_file()]
        # to recurse:
        # replace line above and use line for D in this elif  but without if
        # for each directory call display with files += display("R", files)
        # note line above
    display_files(files)
    return files


def display_files(files):
    files = sorted(files, key=lambda a: (len(a), a))
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
                    if pathlib.Path(file).name == action[2:]:
                        interesting.append(file)
            elif action[0] == "E":
                for file in files:
                    if pathlib.Path(file).suffix == action[2:]:
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
