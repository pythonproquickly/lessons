
import sys

def tokenize(file_path: str) -> list:
    lines = []
    punctuations = "!\"#$%&'()*+, -./:;<=>?@[\]^_`{|}~"
    # use readline()?
    with open(file_path) as open_file:
        for line in open_file:
            lines.append(line.lower().rstrip(("\n")))
    text = " ".join(lines)
    for ch in text:
        #if not ch.isalnum():
        if not ch.isascii():
            text = text.replace(ch, ' ')
    for punctuation in punctuations:
        # not in-place (doesn't change content directly)
        text = text.replace(punctuation, ' ')
    return [token for token in text.split(" ") if token not in [' ', '']]


def computeWordFreqeuncies(tokens: list) -> dict:
    tokenMap = {}
    for token in tokens:
        #token = token.lower()
        if token not in tokenMap:
            tokenMap[token] = 0
        tokenMap[token] += 1
    return tokenMap

if __name__ == "__main__":
    print("Name of the file: ", sys.argv[0])
    print("number of command-line arguments:", len(sys.argv))
    text1_path = set(tokenize(sys.argv[1]))
    text2_path = set(tokenize(sys.argv[2]))
    common_tokens = text1_path.intersection(text2_path)
    print("number of similar tokens: ")
    print(len(common_tokens))