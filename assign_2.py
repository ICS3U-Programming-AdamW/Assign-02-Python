#!/usr/bin/env python3

# Created by: Adam Winogron
# Created on: April 23, 2022
# This program asks the user for a length
# and height and calculates the surface area and volume 
# of a square-based pyramid with those dimensions.

# include math
import math


def main():
    
    #Describe program function
    print("If you give me the dimensions I need I'll calculate\
 the surface area and volume of a square-based pyramid!!")
    print("")

    # Catch statement
    try:
        # Ask user for length of base
        length_string = input("the first thing I need is the length of the square base:")
        length = int(length_string)
        print("")

        # Ask user for height of pyramid
        height_string = input("next I'll need the height of the pyramid!:")
        height = int(height_string)
        print("")

        # calculate the base area
        base_area = (length**2)

        # calculate the side area
        pythag = (height**2 + ((length / 2) ** 2))
        side_height = (math.sqrt(pythag))
        side_area = ((side_height * length) / 2)

        # calculate the volume
        volume = ((height / 3) * base_area)

        # calculata the surface area
        surface_area = (base_area + (side_area * 4)

        # print the surface area
        print("the surface area of your pyramid is {} units!".format(surface_area))
        print("")

        # print the volume
        print("the volume of your pyramid is {} units cubed!".format(volume))
        print("")

    except Exception:
        #tell the user their input wasn't an interger
        print("It seems that '{}' won't work! I need a number to do math!")

    finally:
        print("Restart the program and give me some new numbers!")


if __name__ == "__main__":
    main()
