import sys
import os
import fileinput


class Tokenizer:
    def __init__(self, text_file):
        self.text_file = text_file
        self.tokens = {}

    def tokenize_file(self):
        for line in fileinput.input(self.text_file):
            for token in line.strip().split():
                try:
                    token.encode(encoding="utf-8").decode("ascii")
                except UnicodeDecodeError:
                    continue
                token = token.lower()
                self.tokens[token] = self.tokens.get(token, 0) + 1

    def list_tokens(self):
        if not self.tokens:
            self.tokenize_file()
        return list(self.tokens.keys())


def main(text_files):
    results = []
    for text_file in text_files:
        tokenizer = Tokenizer(text_file)
        results.append(tokenizer.list_tokens())
    common = [value for value in results[0] if value in results[1]]
    print(len(common))


if __name__ == "__main__":
    command_line = sys.argv
    if len(command_line) < 3:
        print("Must specify two file names")
        exit()
    file_names = command_line[1:3]
    for file_name in file_names:
        if not os.path.exists(file_name):
            print(f"File name {file_name} does not exist")
            exit()

    main(file_names)
