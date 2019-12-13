import time;
import random;

todays_password = ("0");
current_item_1 = ("");
current_item_2 = ("");

def local_time_extraction():
    localTime = time.localtime(time.time());
    localTime_str = str(localTime);
    localTime_str = localTime_str.strip("time.struct_time()");
    # Now a list
    localTime_str = localTime_str.split(" ");
    print(localTime_str);

    x = 0;
    z = 0;
    variable_1 = 0;
    variable_2 = 0;
    random_element_1 = random.randint(0, 4);
    random_element_2 = random.randint(0, 4);
    global current_item_1;
    global current_item_2;
    for i in localTime_str:
        current_item = i.rsplit('=', 1);
        current_item = str(current_item[:-1]);
        i = i.split('=', 1)[-1];
        # Removes comma from each element in list ???
        i = i[:-1];
        print(i);
        if (x == random_element_1):
            variable_1 = i;
            current_item_1 = current_item
            print(current_item, x);
        if (x == random_element_2):
            variable_2 = i;
            current_item_2 = current_item
            print(current_item, x);
        x = x + 1;
    calculations(variable_1, variable_2)

def calculations(var1, var2):
    var1 = int(var1);
    var2 = int(var2);
    global todays_password;
    todays_password = str(var1 + var2);

def user_key_input():
    user_input = input("Enter today's password: ");
    return user_input;

def main():
    """
    Begin
    """
    global current_item_1;
    global current_item_2;
    user_input = user_key_input();
    local_time_extraction();
    print("Hint: ", current_item_1, current_item_2);
    while True:
        if (user_input == todays_password):
            print("Access Granted");
            break;
        else:
            number_of_attempts = (number_of_attempts + 1);
            if (number_of_attempts == 4):
                print("Too many failed attempts");
                print("Closing...");
                break;
            print("Invalid password. Please try again");
            print("Attempt: ", number_of_attempts);
            user_input = user_key_input()
    
