# source of words:  https://github.com/dwyl/english-words/
with open("words_alpha.txt", "r") as word:
    words = word.readlines()

five_chars = [word.strip() for word in words if len(word.strip()) == 5]
