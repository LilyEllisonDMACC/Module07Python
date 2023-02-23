"""
Program: keyword_arbitrary_args.py
Author: Lily Ellison
Last date modified: 02/23/2023

The purpose of this program is to make a function that uses arbitrary argument lists and keyword arguments to return a
string.
"""


def average_scores(*args, **kwargs):
    """
    Accepts any number of grade point values and key word/value pairs, calculates the grade point average, selects the
    relevant keywords and corresponding values, organizes them in a statement and returns that statement
    :param args: grade point values to be averaged
    :param kwargs: keywords and values to be selected and assigned to appropriate variables
    :return: results: a statement containing GPA, name, and course
    """
    # Use *args for average calculation
    total = 0
    #keeps track of how many values
    count = 0
    #loops thru values
    for num in args:
        #totals the numbers
        total += num
        #counts the loops and therefore the numbers
        count += 1
    #calculates average
    average = total/count
    #declares variables keywords will be assigned to
    f_name = ""
    l_name = ""
    cour = ""
    #loops thru keyword/value pairs
    for key, value in kwargs.items():
        #selects for keyword
        if key == "first_name":
            #assigns value to variable
            f_name = value
        if key == "last_name":
            l_name = value
        if key == "course":
            cour = value
    #creates string to return with information
    result = "Name: " + f_name + " " + l_name + " GPA: " + str(average) + " Course: " + cour
    return result


if __name__ == '__main__':
    #calling function and printing results with various arguments and keyword values
    print(average_scores(4, 3, 2, 4, first_name='Michelle', last_name='Ruse', course='World domination'))
    print(average_scores(2, 3, 4, first_name='Michael', last_name='Rose', course='Cooking books'))
    print(average_scores(3, 2, 3, 4, 2, first_name='Hienz', last_name='Doofenshmirtz', course='Evil 101'))


"""
Results:
    Name: Michelle Ruse GPA: 3.25 Course: World domination
    Name: Michael Rose GPA: 3.0 Course: Cooking books
    Name: Hienz Doofenshmirtz GPA: 2.8 Course: Evil 101

    Process finished with exit code 0
"""
