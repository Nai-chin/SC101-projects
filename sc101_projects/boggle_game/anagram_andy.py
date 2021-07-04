"""
File: anagram.py
Name: Andy Tsai
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop

dictionary = {}


def main():
    """
    TODO:This program recursively finds all the anagram(s)
        for the word input by user and terminates when the
        input string matches the EXIT constant defined
    """

    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    read_dictionary()

    while True:
        strings = input('Find anagrams for: ').lower()
        # Exit when user enters key word
        if strings == EXIT:
            break

        # Get execute time of anagram
        start = time.time()
        ans_lst = find_anagrams(strings)
        end = time.time()

        print(str(len(ans_lst)), ' anagrams found: ', sep='')
        print(ans_lst)
        print('------------------------------------------------------------------------------')
        print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    global dictionary
    # Store dictionary as dictionary
    # key - first two charters
    # value - words
    with open(FILE, 'r') as f:
        for word in f:
            word = word.strip()
            index = word[0:2]
            if index not in dictionary:
                dictionary[index] = [word]
            else:
                dictionary[index].append(word)


def find_anagrams(word):
    """
    :param word: the string inputted by user
    :return: list of anagrams
    """
    # Create variables
    word_len = len(word)
    result_lst = []
    current_word = ''
    check_index = []

    # call helper function
    helper(word, current_word, result_lst, check_index, word_len)

    return result_lst


def helper(given_word, current_word, result_lst, checker, word_len):
    # Base Case
    if len(current_word) == word_len and has_prefix(current_word) and current_word not in result_lst:
        print('found: ' + current_word)
        result_lst.append(current_word)

    # Recursion
    else:
        for index in range(len(given_word)):
            # check if the word is already added
            if index not in checker:

                # Choose
                checker.append(index)
                current_word += given_word[index]

                # Explore
                helper(given_word, current_word, result_lst, checker, word_len)

                # Un-Choose
                current_word = current_word[:len(current_word) - 1]
                checker.pop()


def has_prefix(sub_s):
    """
    :param sub_s: current word from anagram function
    :return: True or False
    """
    # Get the first two characters from sub_s
    check = sub_s[0:2]
    # If prefix in dictionary key then return True, else False
    if check in dictionary:
        if sub_s in dictionary[check]:
            return True
        else:
            pass
    return False


if __name__ == '__main__':
    main()
