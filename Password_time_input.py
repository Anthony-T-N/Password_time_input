""" Password_time_input.

Proof of concept.

A script that displays a login prompt that accepts generated passwords based on the current date.

"""

__author__ = 'Anthony T Nguyen'
__version__ = '1.0.0'
__date__ = '16.10.2019'

import time
import random

# Global variables.
todays_password = ("0")
current_item_1 = ("")
current_item_2 = ("")

def local_time_extraction():
    """ Local time extraction function.

    Function that extracts the local time and divides the stored string into components.

    """
    localTime = time.localtime(time.time())
    localTime_str = str(localTime);
    localTime_str = localTime_str.strip("time.struct_time()")
    # Now a list
    localTime_str = localTime_str.split(" ")
    print(localTime_str)

    x = 0
    variable_1 = 0
    variable_2 = 0
    random_element_1 = random.randint(0, 4)
    random_element_2 = random.randint(0, 4)
    global current_item_1
    global current_item_2
    for i in localTime_str:
        current_item = i.rsplit('=', 1)
        current_item = str(current_item[:-1])
        i = i.split('=', 1)[-1]
        # Removes comma from each element in list ???
        i = i[:-1]
        print(i)
        if (x == random_element_1):
            variable_1 = i
            current_item_1 = current_item
            print(current_item, x)
        if (x == random_element_2):
            variable_2 = i;
            current_item_2 = current_item
            print(current_item, x)
        x = x + 1
    calculations(variable_1, variable_2)

def calculations(var1, var2):
    """ Calculations function.

    Function that performs basic addition to the specificed variables.

    """
    var1 = int(var1)
    var2 = int(var2)
    global todays_password
    todays_password = str(var1 + var2)

def user_key_input():
     """ User Key Input Function.

    Function that returns user's input.

    """
    user_input = input("Enter today's password: ")
    return user_input

def main():
    """
    Begin
    """
    global current_item_1;
    global current_item_2;
    local_time_extraction()
    number_of_attempts = 0
    print("Hint: ", current_item_1, current_item_2)
    user_input = user_key_input()
    while True:
        if (user_input == todays_password):
            print("Access Granted")
            break;
        else:
            number_of_attempts = (number_of_attempts + 1)
            # Limits the number of password entry attempts.
            if (number_of_attempts == 4):
                print("Too many failed attempts");
                print("Closing...")
                break;
               #exit(0)
            print("Invalid password. Please try again")
            print("Attempt: ", number_of_attempts)
            user_input = user_key_input()

if __name__ == '__main__':
    main()
    
