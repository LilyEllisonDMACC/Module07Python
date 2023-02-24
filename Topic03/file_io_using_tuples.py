import os as os

"""
Program: file_io_using_tuples.py
Author: Lily Ellison
Last date modified: 02/24/2023

The purpose of this program is to accept test scores for a named student, store them as a tuple, add them to a file, and
print that file to the screen 

"""


def write_to_file(name_score_tuple):
    """
    Accepts a tuple and appends it to a file
    :param name_score_tuple: tuple containing a name and scores for a student
    :return: None (adds info to file to print later
    """
    #open file to add info to the end (a for append):
    s = open('student_info.txt', 'a')
    #write the information as a string to the end of the file and start a new line
    s.write(str(name_score_tuple) + "\n")
    #close the file:
    s.close()


def get_student_info(a_name):
    """
    Accepts a student name, asks how many scores they want to enter, validates scores, appends scores to a list, adds
    name and list to a tuple and passes the tuple to another method to write to a file.
    :param a_name: string passed to function
    :returns void - passes info to write_to_file() as a tuple
    """
    score_list = []
    count = -1
    #indicates which student is being assigned the scores
    print("Hello, " + a_name + "!")
    #runs as long as the number of scores to enter is an integer greater than 0
    while type(count) != int or count < 0:
        count = input("How many scores would you like to enter? ")
        try:
            #validates entry is an integer
            count = int(count)
            #cannot add negative entries
            if count < 0:
                print("Invalid input, please try again.")
                #sets count to -1 to prompt while loop
                count = -1
                continue
            #if no scores to enter, a null list is submitted
            elif count == 0:
                print("No scores to enter. Null score set.")
            else:
                #runs as many loops as scores to enter
                while count > 0:
                    current_score = input("Please enter a test score: ")
                    try:
                        #validates score as integer
                        current_score = int(current_score)
                        #selects scores out of range
                        if current_score < 0 or current_score > 100:
                            print("Invalid entry, please try again. ")
                            continue
                        else:
                            #adds valid, in range scores to list
                            score_list.append(current_score)
                            #decreases count by 1
                            count -= 1
                    except:
                        print("Invalid entry, please try again. ")
                        continue
        except:
            print("Invalid entry, please try again. ")
            continue
    #declares and creates a tuple with the names and scores
    name_score_tuple = (a_name, score_list)
    #sends tuple to write method and calls method
    write_to_file(name_score_tuple)


def read_from_file():
    """
    Opens the student info file, reads the information and prints it to the screen
    :return: void, prints info to the screen
    """
    #opens file to read:
    s = open('student_info.txt', 'r')
    #reads file and stores info as variable
    all_student_info = s.read()
    #prints variable to screen
    print(all_student_info)
    #closes file
    s.close()


if __name__ == "__main__":
    #creates blank file each time program begins
    open("student_info.txt", "w").close()
    #calls the get student method and passes student's name as arg
    get_student_info('Phineas')
    get_student_info('Ferb')
    get_student_info('Isabella')
    get_student_info('Bufford')
    #calls the read file to display info
    read_from_file()

    """
    Testing:
Hello, Phineas!
How many scores would you like to enter? zero
Invalid entry, please try again. 
How many scores would you like to enter? -1
Invalid input, please try again.
How many scores would you like to enter? 0
No scores to enter. Null score set.
Hello, Ferb!
How many scores would you like to enter? 1
Please enter a test score: 1000
Invalid entry, please try again. 
Please enter a test score: -10
Invalid entry, please try again. 
Please enter a test score: a
Invalid entry, please try again. 
Please enter a test score: 100
Hello, Isabella!
How many scores would you like to enter? 2
Please enter a test score: 99
Please enter a test score: 98
Hello, Bufford!
How many scores would you like to enter? 3
Please enter a test score: 80
Please enter a test score: 81
Please enter a test score: 82
('Phineas', [])
('Ferb', [100])
('Isabella', [99, 98])
('Bufford', [80, 81, 82])


Process finished with exit code 0

    
    """