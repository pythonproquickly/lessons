import os

if os.path.isfile("/home/andy/myfile.txt"):
    print("File exists")
else:
    print("File does not exist")


filenames = [f"demo{n}.txt" for n in range(5)]
for filename in filenames:
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass
    with open(filename, "w") as f:
        f.write("this is line 1")
        for data in range(10):
            f.write(f"{data} blah blah")

with open("demo1.txt", "r") as f:
    contents = f.readlines()

print(contents, type(contents))

with open("demo1.txt", "r") as f:
    print(f.readline(), type(f.readline()))
