# 3/16/2022
import sys, random, time

print("press Control-C to stop.")

try:
    import bext
except ImportError:
    print(
        """This program requires the bext module which you can install at /
    https://pypi.org/project/Bext/"""
    )

# set up the constraints:
width, height = bext.size()
width -= 1
number_of_logos = 10  # try changing this from 1 to 100
pause_amount = 0.05
colors = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]

up_right = "ur"
up_left = "ul"
down_right = "dr"
down_left = "dl"
directions = [up_right, up_left, down_right, down_left]

# Key names for logo dictionaries:
color = "color"
x = "x"
y = "y"
direction = "direction"


def main():
    bext.clear()

    # generate some logos
    logos = []
    for i in range(number_of_logos):
        logos.append(
            {
                color: random.choice(colors),
                x: random.randint(1, width - 4),
                y: random.randint(1, height - 4),
                direction: random.choice(directions),
            }
        )
        if logos[-1][x] % 2 == 1:
            # make sure x is even so it can hit the corner.
            logos[-1][x] -= 1

    corner_bounces = 0  # count how many times a logo hits a corner.
    while True:  # main program loop.
        for logo in logos:
            bext.goto(logo[x], logo[y])
            print("    ", end="")  # Try commenting this line out.

            original_direction = logo[direction]

            # see if the logo bounces off the corners:
            if logo[x] == 0 and logo[y] == 0:
                logo[direction] = down_right
                corner_bounces += 1
            elif logo[x] == 0 and logo[y] == height - 1:
                logo[direction] = up_right
                corner_bounces += 1
            elif logo[x] == width - 3 and logo[y] == 0:
                logo[direction] = down_left
                corner_bounces += 1
            elif logo[x] == width - 3 and logo[y] == height - 1:
                logo[direction] = up_left
                corner_bounces += 1

            # see if the logo bounces off the left edge:
            elif logo[x] == 0 and logo[direction] == up_left:
                logo[direction] = up_right
            elif logo[x] == 0 and logo[direction] == down_left:
                logo[direction] = down_right

            # see if the logo bounces off the right edge:
            # (width - 3 because 'dvd' has 3 letters.)
            elif logo[x] == width - 3 and logo[direction] == up_right:
                logo[direction] = up_left
            elif logo[x] == width - 3 and logo[direction] == down_right:
                logo[direction] = down_left

            # see if the logo bounces off the top edge:
            elif logo[y] == 0 and logo[direction] == up_left:
                logo[direction] = down_left
            elif logo[y] == 0 and logo[direction] == up_right:
                logo[direction] = down_right

            # see if the logo bounces off the bottom edge:
            elif logo[y] == height - 1 and logo[direction] == down_left:
                logo[direction] = up_left
            elif logo[y] == height - 1 and logo[direction] == down_right:
                logo[direction] = up_right

            if logo[direction] != original_direction:
                # change color when logo bounces:
                logo[color] = random.choice(colors)

            # Move the logo. (X moves by 2 because the terminal characters are
            # twice as tall as they are wide.)
            """directions = {up_right: (2, -1),
                          up_left: (-2, -1),
                          down_right: (2, 1),
                          down_left: (-2, 1)
                          }
            logo[x] += directions[logo[direction]]
            logo[y] += directions[logo[direction]]"""
            if logo[direction] == up_right:
                logo[x] += 2
                logo[y] -= 1
            elif logo[direction] == up_left:
                logo[x] -= 2
                logo[y] -= 1
            elif logo[direction] == down_right:
                logo[x] += 2
                logo[y] += 1
            elif logo[direction] == down_left:
                logo[x] -= 2
                logo[y] += 1

        # Display the number of corner bounces:
        bext.goto(5, 0)
        bext.fg("white")
        print("corner bounces:", corner_bounces, end="")

        for logo in logos:
            # Draw the logos at their new location:
            bext.goto(logo[x], logo[y])
            bext.fg(logo[color])
            print("dvd", end="")

        bext.goto(0, 0)

        sys.stdout.flush()  # required for bext running programs.
        time.sleep(pause_amount)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("Bouncing dvd logo by Al Sweigart")
        sys.exit()  # when ctrl-c is pressed, end the program.
