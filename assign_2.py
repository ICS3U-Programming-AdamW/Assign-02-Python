#!/usr/bin/env python3

# Created by: Adam Winogron
# Created on: April 23, 2022
# This program asks the user for a length
# and height and calculates the surface area and volume
# of a square-based pyramid with those dimensions.

# include math
import math


def main():

    # Describe program function
    print("If you give me the dimensions I need, I'll calculate \
the surface area and volume of a square-based pyramid!!")
    print("")

    # declare variables
    length_string = ""
    height_string = ""
    units = ""

    # Catch statement
    try:
        # Ask user for length of base
        length_string = input("The first thing I need is the\
 length of the square base: ")
        length = float(length_string)
        print("")

    except Exception:
        # tell the user their input wasn't an interger
        print()
        print("It seems that '{}' won't work! I need \
a number to do math!".format(length_string))

    else:
        try:
            # Ask user for height of pyramid
            height_string = input("Next I'll need the height \
of the pyramid!: ")
            height = float(height_string)
            print("")

            # ask user for the units
            units = input("The last thing I'll need is the units that this shape \
will be defined by (cm, in, m, etc.): ")
            print("")

    # MATH
            # calculate the base area
            base_area = (length**2)

            # calculate the side area
            pythag = (height**2 + ((length / 2) ** 2))
            side_height = (math.sqrt(pythag))
            side_area = ((side_height * length) / 2)

            # calculate the volume
            volume = ((height / 3) * base_area)

            # calculata the surface area
            surface_area = (base_area + (side_area * 4))

            # print the surface area
            print("The surface area of your pyramid is {:.2f} \
{}!".format(surface_area, units))
            print("")

            # print the volume
            print("The volume of your pyramid is {:.2f} \
{} cubed!".format(volume, units))
            print("")

        except Exception:
            # tell the user their input wasn't an interger
            print()
            print("It seems that '{}' won't work! \
I need a number to do math!".format(height_string))

        finally:
            # tell user to restart
            print()
            print("Restart the program and give me some new numbers!")


# call main()
if __name__ == "__main__":
    main()
