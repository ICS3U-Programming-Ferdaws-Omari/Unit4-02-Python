#!/usr/bin/env python3
# Created By: Ferdaws
# Date: April 2022
# This program checks the condition at the end of the loop.
def main():
    # factorial loop
    loop_counter = 0
    factorial_answer = 1

    # get user number
    print("")

    # calculate the user number and factorial answer
    try:
        user_number = int(input("Enter a positive number: "))
        while True:
            loop_counter = loop_counter + 1
            factorial_answer = factorial_answer * loop_counter
            print("Tracking {} times through loop.".format(loop_counter))
            if loop_counter >= user_number:
                break

        print("")
        print("{}! = {}".format(user_number, factorial_answer))
    except Exception:
        print("This was not a whole number , please enter a whole number")
    finally:
        print("Thanks for playing")
   


if __name__ == "__main__":
    main()