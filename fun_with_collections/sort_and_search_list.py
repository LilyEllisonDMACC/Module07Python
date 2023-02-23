"""
Program: sort_and_search_list.py
Author: Lily Ellison
Last date modified: 02/22/2023

The purpose of this program is to make a list, sort that list, and then search that list for a value.
"""

'''
You can make a new file sort_and_search_list.py. For this assignment, you can hard-code a list you pass to the 
sort_list() and search_list() in your main. For extra credit, you and use the previous assignment get_list()
Write sort_list() to sort the list

    What is the return statement?
        Write a comment explaining why you included return OR
        Write a comment explaining why your code has no return statement.

Write search_list() 

    What is the return statement?
        Write a comment explaining why you included return OR
        Write a comment explaining why your code has no return statement.

Write main

    call sort_list()
    call search_list()


'''


def make_list(num):
    """
    Accepts a number which is used to determine the number of items in the list. Calls get_input() function to request
    and receive user input to add integers to the list. Validates input and returns the list with the designated number
    of items
    :param num: tells the function how many items to include in the list. The get_input() function is used to get user
    input and this function validates it before adding it to the list. A valid entry decreases this number, preventing
    infinite looping.
    :return: returns a list of integers with as many members as the original num passed to the function as an argument.
    """
    #Declares list:
    my_list = []
    #Establishes a loop that will run num number of times:
    while num > 0:
        #Calls get_input() function and assigns it to a variable:
        list_number = get_input()
        #Sets up a try/except:
        try:
            #Tries to cast input as integer:
            add_number = int(list_number)
        #Exception thrown if unable to cast as integer:
        except:
            #Gives reason for repeat:
            print("Not a whole number. Please try again.")
        #As long as input is integer:
        else:
            #Adds input to the list:
            my_list.append(add_number)
            #Reduces the number of times it will ask for another integer:
            num -= 1
    #Sends list back where method was called.
    return my_list


def get_input():
    """
    Requests a whole number be entered by the user and returns user's entry to where it was called from.
    :return: user's input, to be validated elsewhere.
    """
    user_answer = input("Please enter a whole number: ")
    return user_answer


if __name__ == '__main__':
    first_list = make_list(5)
    print("First list, as entered: " + str(first_list))
