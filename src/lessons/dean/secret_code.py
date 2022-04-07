# caesar cypher

plain = "abcdefghijklmnopqrstuvwxyz .,"
coded = "wxyz .,abcdefghijklmnopqrstuv"

text = "this is going to be encrypted"

new_text = ""
for letter in text:
    new_text = new_text + coded[plain.find(letter)]

print(text)
print(new_text)
