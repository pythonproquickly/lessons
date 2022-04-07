# 2/28/2022

# Question 1: Does this work only for strings?
statement = "Find the number of letters and iterate through them."

# for i in range(len(statement)):
#     print(i)

# Output: Prints the index.
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# for i, letter in enumerate(statement):
#     print(i, letter)

# Output: Prints both index and letter
# 0 F
# 1 i
# 2 n
# 3 d
# 4
# 5 t
# 6 h
# 7 e
# 8
# 9 n
# 10 u
letter_count = f"Total letters: {len(statement)}"
print(letter_count)

spaces = []
i = 0
while i < len(statement):
    if statement[i] == " ":
        # print(i, "Lost in SPACE")
        spaces.append(i)
        i += 1

    else:
        i += 1
        # print(i)


# print(spaces, len(spaces))
positions = f"\nThere are {len(spaces)} in the sentance."\
    f"\nThey are located at positions:{spaces}"
print(positions)

