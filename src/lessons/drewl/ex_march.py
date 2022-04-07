# 3/10/2022

def main():
    print("Running main program.\n")


def generation_finder(age):
    """Assigns a generation based on age."""
    generation = "no idea"
    if age > 76:
        generation = "the Traditionalist generation"
    elif age <= 75 and age >= 57:
        generation = "the Baby Boomer generation"
    elif age <= 56 and age >= 45:
        generation = "Generation X"
    elif age < 45 and age > 26:
        generation = "the Millenial generation"
    elif age <= 26:
        generation = "Generation Z"
    return generation


if __name__ == "__main__":
    main()

# ??Question for Andy??: I would like to keep the notes and calculations below as a reference. Where is a good place
# to put them? At the bottom of the program or in another module?

# # generation_z = 26
# # years 1996  to 2015
# millenials = 45
# # years 1977 to 1995
# generation_x = 57
# # years 1965 to 1976
# baby_boomer = 76
# # years 1946 to 1964
# traditionalists = 77
# # years 1945 and before

#
# years = [1946, 1965, 1977, 1996]
# ages = []
# for year in years:
#     age = 2022 - year
#     ages.append(age)
# print(f"Ages are:{ages}")
# # output:
# # Ages are:[76, 57, 45, 26]

message = "Welcome to the generation identifier. Enter your information below \
to identify which generation you were born in.  "
print(message)
while True:
    user = input("Enter your name: ").lower()
    age = int(input("Enter your age: "))
    gen = generation_finder(age)
    user_info = f"Hello {user.title()}, you are {age} years old and you belong to {gen}."
    print(user_info)

    ask = input("Do you want to enter another person's age(y/n)? ").lower()
    if ask in ("no", "n", "nope"):
        print("See you next time.")
        break
    elif ask in ("y", "yes", "yeah"):
        print("\nrestarting...")
        continue
    else:
        print("Goodbye.")
        break
