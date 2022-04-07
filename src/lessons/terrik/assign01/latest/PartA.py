import sys
import os
import fileinput
import string

# fileinput library validated; part of the built-in python module
# Guaranteed filename inputs are correct and don't have to worry about failing to open file due to not existing or incorrect filename

# any character that isn't a alphanumeric will be treated as delimiters including:
# punctuations, foreign characters, accents
class Tokenizer:
    def __init__(self, text_file):
        self.text_file = text_file
        self.tokens = {}

    """
    It would be O(N*M) + a little bit of O(p) because N is the number of lines of the text (which will be read line by line)
    and the M is the number of tokens in that line. There will be significantly less items to iterate over compared to
    the outside for loop iterating over the lines for large files.
    """

    def tokenize_file(self):
        with open(self.text_file) as open_file:
            # O(n)
            for line in open_file:
                tokens = line.strip().split()
                # O(m): m number of tokens; subsets of file; m:n is very small the larger the file
                for token in tokens:
                    # try:
                    #     token.encode(encoding = "utf-8").decode("ascii")
                    # # ignores token
                    # except UnicodeDecodeError:
                    #     continue
                    token = token.lower()
                    working_token = token
                    # O(p): p is number of ch; less than the number of tokens.
                    # use comma as a word delimeter in token
                    # iterate with an index
                    # as long as we havent already found a comma add one
                    # when done split the working variable based on a comma
                    # iterate and append
                    for idx, ch in enumerate(token):
                        if ch not in string.ascii_lowercase + " 0123456789":
                            if "," not in token[0:idx + 1]:
                                working_token = working_token.replace(ch, ",")
                            continue
                    token = working_token.split(",")
                    for split_token in token:
                        if split_token != '':
                            self.tokens[split_token] = self.tokens.get(split_token, 0) + 1

    def list_tokens(self):
        if not self.tokens:
            self.tokenize_file()
        # O(N)
        return list(self.tokens.keys())

    def calculate_token_frequencies(self):
        if not self.tokens:
            self.tokenize_file()

    def print_token_frequencies(self) -> None:
        # O(nlogn) n is the number of tokens to be sorted
        # O(n) accessing each key,value pair in the tokens dictionary
        print(self.tokens.items())
        for k, v in sorted(self.tokens.items(), key=lambda x: x[1], reverse=True):
            print(k + "\t" + str(v))


def main(text_file):
    tokenizer = Tokenizer(text_file)
    tokenizer.list_tokens()
    tokenizer.calculate_token_frequencies()
    tokenizer.print_token_frequencies()


if __name__ == "__main__":
    if not os.path.exists(sys.argv[1]):
        print(f"{sys.argv[1]} does not exist")
        exit()
    text_file = sys.argv[1]
    main(text_file)
