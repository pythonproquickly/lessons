# 6/6/2022

"""Fibonacci sequence by Al Sweigart: Calculates number of the
fibonacci sequence: 0,1,1,2,3,5,8,13...
"""

import sys

print('''

The Fibonacci sequence begins with 0 and 1, and the next number is the sum of
the previous two numbers. The seqence continues forever:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987...
''')
while True: # Main program loop.
    while True: # Keep asking until the use enters valid input.
        print('Enter the Nth Fibonacci number you wish to')
        print('calculate (such as 5, 50, 1000, 9999), or Quit to quit')
        response = input('> ').upper()

        if response == 'Quit':
            print('Thanks for playing!')
            sys.exit()

        if response.isdecimal() and int(response) != 0:
            nth = int(response)
            break # Exit the loop when the user enters a valid number.

        print('Please enter a number greater than 0, or QUIT.')
    print()

    # Handle the specical cases if the user enters 1 or 2:
    if nth == 1:
        print('0')
        print()
        print('The #1 Fibonacci number is 0.')
        continue
    elif nth == 2:
        print('0, 1')
        print()
        print('The #2 Fibonacci number is 1.')
        continue

    # Display a warning if the user enters a large number:
    if nth >= 10_000:
        print('WARNING: This will take a while to display on the')
        print('screen. If you want to quit this program  before it is ')
        print('done, press Ctrl-C.')
        input('Press Enter to begin...')

    # Calculate the Nth Fibonnaci number:
    penultimate_number = 0
    last_number = 1
    fib_numbers_calc = 2
    print('0, 1, ', end='')  # Display the fist two Fibonacci numbers.

    # Display all the later numbers of the Fibonacci sequence:
    while True:
        next_number = penultimate_number + last_number
        fib_numbers_calc += 1

        # Display the next number in the sequence:
        print(next_number, end='')

        # Check if we've found the Nth number the user wants:
        if fib_numbers_calc == nth:
            print()
            print()
            print('The #', fib_numbers_calc, ' Fibonacci ',
                  'number is ', next_number, sep='')
            break

        # Print a comma in between the sequence numbers.
        print(', ', end='')

        # Shift the last two numbers:
        penultimate_number = last_number
        last_number = next_number


