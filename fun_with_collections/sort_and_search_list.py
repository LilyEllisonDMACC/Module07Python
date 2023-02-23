"""
Program: sort_and_search_list.py
Author: Lily Ellison
Last date modified: 02/22/2023

The purpose of this program is to make a list, sort that list, and then search that list for a value using various
functions.
"""


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


def sort_list(submitted_list):
    """
    Sorts an unsorted list
    :param submitted_list: a list of integers, validated by another function
    :return: Returns sorted list. Not needed for this program directly, but testing would not work without it.
    """
    submitted_list.sort()
    return submitted_list


def search_list(submitted_list):
    """
    Accepts a list, prompts user for a value to search for in list, validates input, searches list, returns search
    results
    :param submitted_list: list of integers searched
    :return: results: tells user if the number was not found or the index of the number in the list if it was found
    """
    #Primes variable used to run while loop:
    valid_input = False
    #Established while loop:
    while not valid_input:
        num_to_find = input("What number would you like to search for? ")
        try:
            # Tries to cast input as integer:
            find_number = int(num_to_find)
        # Exception thrown if unable to cast as integer:
        except:
            # Gives reason for repeat:
            print("Not a whole number. Please try again.")
            continue
        # As long as input is integer:
        else:
            #Exits while loop:
            valid_input = True
    try:
        #Searches for the validated input:
        num_index = submitted_list.index(find_number)
    except:
        #Declares value not found:
        result = num_to_find + " not found."
    else:
        #States where the number is in the list using its index value
        result = num_to_find + " found at index " + str(num_index)
    finally:
        #Result returned to calling location
        return result


if __name__ == '__main__':
    #Create a list using make_list and get_input:
    first_list = make_list(5)
    #Display results as a list:
    print("First list, as entered: " + str(first_list))
    #Sort the list:
    sort_list(first_list)
    #Display sorted results:
    print("First list, in numerical order: " + str(first_list))
    #Start the search function:
    search_results = search_list(first_list)
    #Display the search results:
    print(search_results)
