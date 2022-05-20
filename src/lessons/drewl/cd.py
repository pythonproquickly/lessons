# 3/11/2022

# Project #14 (pg. 64) from the Big Book of Small Python Projects.
import sys, time
import sevseg

seconds_left = 30

# ??? Why is there a try block before the while loop.
try:
    while True:
        print("\n" * 5)
        hours = str(seconds_left // 3600)
        minutes = str((seconds_left % 3600 // 60))
        seconds = str(seconds_left % 60)

        # Get the digit strings from the sevseg module:
        hour_digits = sevseg.getSevSegStr(hours, 2)
        hour_top_row, hour_middle_row, hour_bottom_row = hour_digits.splitlines()

        minute_digits = sevseg.getSevSegStr(minutes, 2)
        (
            minute_top_row,
            minute_middle_row,
            minute_bottom_row,
        ) = minute_digits.splitlines()

        second_digits = sevseg.getSevSegStr(seconds, 2)
        (
            seconds_top_row,
            seconds_middle_row,
            seconds_bottom_row,
        ) = second_digits.splitlines()

        # Display the digits:
        print(hour_top_row + "      " + minute_top_row + "      " + seconds_top_row)
        print(
            hour_middle_row
            + "      "
            + minute_middle_row
            + "      "
            + seconds_middle_row
        )
        print(
            hour_bottom_row
            + "      "
            + minute_bottom_row
            + "      "
            + seconds_bottom_row
        )

        if seconds_left == 0:
            print()
            print("     * * * BOOM * * *")
            break

        print()
        print("Press Control-C to quit.")

        time.sleep(1)  # one second pause.
        seconds_left -= 1
except KeyboardInterrupt:
    print("Countdown by Al Blah Blah.")
    sys.exit()  # When control C is pressed, end the program.
