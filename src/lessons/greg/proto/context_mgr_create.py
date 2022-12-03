class ContextManager:
    def __init__(self):
        print("init method called")

    def __enter__(self):
        print("enter method called")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("exit method called")


class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


def main():
    with ContextManager() as just_to_understand_flow:
        print("with statement block")

    with FileManager("test.txt", "w") as f:
        f.write("Test")

    print(f.closed)


if __name__ == "__main__":
    main()