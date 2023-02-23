"""
Program: sort_and_search_list_test.py
Author: Lily Ellison
Last date modified: 02/23/2023

The purpose of this program is to test sort_and_search_list.py. However, I was not sure how to test functions that
request input, so output from those in included in comments below instead.
"""
import unittest
from fun_with_collections.sort_and_search_list import sort_list


class MyTestCase(unittest.TestCase):
    def test_sort_list(self):
        my_list = [3, 7, -9]
        expected = [-9, 3, 7]
        actual = sort_list(my_list)
        self.assertEqual(expected, actual)


"""
Test of search_list (tests for make_list and get_input are in basic_list.py):

Run 1:
Please enter a whole number: 6
Please enter a whole number: 4
Please enter a whole number: 22
Please enter a whole number: 31
Please enter a whole number: 55
First list, as entered: [6, 4, 22, 31, 55]
First list, in numerical order: [4, 6, 22, 31, 55] - sort worked
What number would you like to search for? k - invalid input
Not a whole number. Please try again. - worked
What number would you like to search for? .5 - invalid input
Not a whole number. Please try again. - worked
What number would you like to search for? -9 - not in list
-9 not found. - worked

Process finished with exit code 0

Run 2:
Please enter a whole number: 46
Please enter a whole number: 52
Please enter a whole number: 5
Please enter a whole number: 10
Please enter a whole number: 8
First list, as entered: [46, 52, 5, 10, 8]
First list, in numerical order: [5, 8, 10, 46, 52] - sort worked
What number would you like to search for? 10 - present
10 found at index 2 - worked

Process finished with exit code 0
"""