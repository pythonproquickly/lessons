import string
characters = string.ascii_lowercase.replace("j", ".")


key = "playfair example"
key_matrix = ["" for i in range(5)]

j = 0
i = 0

for c in key:
    if c in characters:
        key_matrix[i] += c

        characters = characters.replace(c, ".")

        j += 1
        if j > 4:
            i += 1
            j = 0

for c in characters:
    if c != ".":
        key_matrix[i] += c

        j += 1
        if j > 4:
            i += 1
            j = 0


print(key_matrix)
plain_text = "hidethegoldinthetreestump"
plain_text_pairs = []
cipher_text_pairs = []
# If both letters are the same (or only one letter is left), add an "X" after the first letter. Encrypt the new pair
# and continue. Some variants of Playfair use "Q" instead of "X", but any letter, itself uncommon as a repeated pair,
# will do.
i = 0
while i < len(plain_text):
    a = plain_text[i]
    b = ""

    if i + 1 == len(plain_text):
        b = "x"
    else:
        b = plain_text[i + 1]

    if a != b:
        plain_text_pairs.append(a + b)
        i += 2
    else:
        plain_text_pairs.append(a + "x")
        i += 1

print(plain_text_pairs)
# If the letters appear on the same row of your table, replace them with the letters to their immediate
# right respectively (wrapping around to the left side of the row if a letter in the original pair was on the right
# side of the row).
for pair in plain_text_pairs:
    applied_rule = False
    for row in key_matrix:
        if pair[0] in row and pair[1] in row:
            j0 = row.find(pair[0])
            j1 = row.find(pair[1])

            cipher_text_pair = row[j0 + 1 % 5] + row[j1 + 1 % 5]
            cipher_text_pairs.append(cipher_text_pair)
            applied_rule = True

    if applied_rule:
        continue
# If the letters appear on the same column of your table, replace them with the letters immediately
# below respectively (wrapping around to the top side of the column if a letter in the original pair was on the
# bottom side of the column).
    for j in range(5):
        col = "".join([key_matrix[i][j] for i in range(5)])
        if pair[0] in col and pair[1] in col:
            j0 = col.find(pair[0])
            j1 = col.find(pair[1])

            cipher_text_pair = col[j0 + 1 % 5] + col[j1 + 1 % 5]
            cipher_text_pairs.append(cipher_text_pair)
            applied_rule = True
    if applied_rule:
        continue
    # If the letters are not on the same row or column, replace them with the letters on the
# same row respectively but at the other pair of corners of the rectangle defined by the original pair. The order is
# important – the first letter of the encrypted pair is the one that lies on the same row as the first letter of the
# plaintext pair.
    i0 = 0
    i1 = 0
    j0 = 0
    j1 = 0
    for i in range(5):
        row = key_matrix[i]
        if pair[0] in row:
            i0 = i
            j0 = row.find(pair[0])

        if pair[1] in row:
            i1 = i
            j1 = row.find(pair[1])

    cipher_text_pair = key_matrix[i0][j1] + key_matrix[i1][j0]
    cipher_text_pairs.append(cipher_text_pair)

print(cipher_text_pairs)