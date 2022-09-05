letters =  ['a','b','c']


for i in range(len(letters)): # [0,1,2]
    print(letters[i]) 


for letter in letters:
    print(letter)


for position, letter in enumerate(letters[1:]):
    print(f"{position=}, {letter=}")