#!user/bin/env python3

# Created by: RJ Fromm
# Created on: September 2019
# This program calculates the volume of a frustum

import math


def main():

    height = int(input("Enter the height of the frustum (cm) : "))

    upper_base = int(input("Enter radius of upper base (cm) : "))

    lower_base = int(input("Enter radius of lower base (cm) : "))

    volume = 1/3 * math.pi * height * (
        upper_base**2 + lower_base**2 + upper_base * lower_base)

    print("The volume of the Frustum is {} cm3".format(volume))


if __name__ == "__main__":
    main()
