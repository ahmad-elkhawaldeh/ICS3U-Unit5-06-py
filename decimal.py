#!/usr/bin/env python3

# Created by : Ahmad
# Created on : Dec 2021
# this program rounds off decimal numbers


def roundingOff(number, round):
    for loop in range(round[0]):
        number[0] *= 10
    number[0] = int(number[0] + 0.5)
    for loop in range(round[0]):
        number[0] /= 10


def main():
    try:
        number = [float(input("Enter the number you want to round: "))]
        round = [int(input("Enter how many decimal places you want to round by: "))]
        roundingOff(number, round)
        print("\nThe rounded number is " + str(number[0]))
    except Exception:
        print("This is not a number")


if __name__ == "__main__":
    main()
