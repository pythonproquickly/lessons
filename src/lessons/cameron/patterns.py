def pattern1(size):
    for line in range(size):
        output[line] = str(size)
        print(''.join(output))
        output[line] = "P"


def pattern2(size):
    for line in range(size - 1, -1, -1):
        output[line] = str(size)
        print(''.join(output))
        output[line] = "P"


def pattern3(size):
    for line in range(size - 1, -1, -1):
        output[line] = str(size)
        print(''.join(output))


def pattern4(size):
    for line in range(size):
        output[line] = str(size)
        print(''.join(output))


print("""
Welcome to My Pattern Program
This program is written by ( your name ) . The purpose of this program is to 
create four different patterns of different sizes. The size of each pattern 
is determined by the number of columns or rows. For example, a pattern of
size 5 has 5 columns and 5 rows. Each pattern is made up of character P and a 
digit , which shows the size. The size must be between 2 and 9.
""")

while True:
    while True:
        print("""
        1. Pattern 1
        2. Pattern 2
        3. Pattern 3
        4. Pattern 4
        15. Quit
        """)
        pattern = int(input("Chose a pattern between 1 and 4, 15 to quit: "))
        if pattern in (1, 2, 3, 4, 15):
            break
        print("Incorrect: try again")
    if pattern == 15:
        break

    while True:
        size = int(input("Chose a pattern size between 2 and 9: "))
        if size in range(2, 10):
            break
        print("Incorrect: try again")

    print(f"Pattern {pattern} is displayed")
    output = ["P"] * size

    if pattern == 1:
        pattern1(size)
    elif pattern == 2:
        pattern2(size)
    elif pattern == 3:
        pattern3(size)
    elif pattern == 4:
        pattern4(size)
