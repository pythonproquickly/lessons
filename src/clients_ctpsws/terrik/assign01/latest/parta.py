import sys
import os


def tokenize_file(text_file, tokens):
    with open(text_file, 'r') as tf
        for line in tf:
            tokens = line.strip().split():
                try:
                token.encode(encoding="utf-8").decode("ascii")
            except UnicodeDecodeError:
                continue
            token = "".join(
                "" if ch in "\"'!@#$%^&*()-_+= " else ch for ch in token
            )
            if len(token) > 0:
                token = token.lower()
                tokens[token] = tokens.get(token, 0) + 1
    return tokens

def list_tokens(tokens):
    if not tokens:
        tokenize_file()
    return list(tokens.keys())

def calculate_token_frequencies(tokens):
    if not self.tokens:
        self.tokenize_file()

def print_token_frequencies(tokens):
    for key, value in self.tokens.items():
        print(f"{key}\t{value}")


def main(text_file):
    tokens = {}
    tokenizer.list_tokens(tokens)
    tokenizer.calculate_token_frequencies(tokens)
    tokenizer.print_token_frequencies(tokens)


if __name__ == "__main__":
    command_line = sys.argv
    if len(command_line) < 2:
        print("Must specify a file name")
        exit()
    file_name = command_line[1]
    if not os.path.exists(file_name):
        print(f"File name {file_name} does not exist")
        exit()

    main(file_name)
