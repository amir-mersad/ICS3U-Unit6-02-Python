#!/usr/bin/env python3

# Created by: Amir Mersad
# Created on: December 2019
# This program finds the max number


def max_num(input_list):
    # Process
    current_max = input_list[0]
    for counter in input_list:
        if counter > current_max:
            current_max = counter
    return current_max


def main():
    # This function gets the input and passes it to another function
    number_list = []

    # Input and part of Process
    while True:
        number_input = input('Enter the number:  (type "stop" when done)\t')
        if number_input == "stop":
            break
        elif number_input == "":
            pass
        else:
            try:

                number_input = float(number_input)
                number_list.append(number_input)
            except(Exception):
                print("Wrong input!!!")
                return

    # Passing to another funtion
    max_number = max_num(number_list)

    # Output
    print(max_number)


if __name__ == "__main__":
    main()
