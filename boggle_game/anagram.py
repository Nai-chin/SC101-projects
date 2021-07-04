"""
File: anagram.py
Name: Livia Tseng 曾迺芩
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

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


# Global Variable
word_dict = {}               # dict, Store all the vocabulary from FILE


def main():
    """
    This program helps users to check the anagrams of the words they input.
    """
    start = time.time()
    ####################
    read_dictionary()
    print(f"Welcome to stanCode \"Anagram Generator\" (or {EXIT} to quit)")
    while True:
        search_target = input("Find anagrams for: ")
        if search_target == EXIT:
            break
        else:
            find_anagrams(search_target)
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    """
    This function reads and stores the words in the dictionary to prepare the dictionary.
    """
    global word_dict
    with open(FILE, "r") as f:
        for line in f:
            line = line.strip()
            if line[0:2] not in word_dict:
                word_dict[line[0:2]] = {line: 1}
            else:
                word_dict[line[0:2]][line] = 1


def find_anagrams(s):
    """
    :param s: The word user input to search anagrams.
    :return: lst, contains all the anagrams.
    """
    ans_l = []  # Storing the anagrams found in dictionary
    current_w = ""
    dict_s = {}  # key: alphabet of s, value: numbers of the alphabet in s.
    for ch in s:
        if ch in dict_s:
            dict_s[ch] += 1
        else:
            dict_s[ch] = 1
    print("Searching…")
    helper(s, dict_s, len(s), current_w, ans_l)
    return print(f"{len(ans_l)} anagrams:{ans_l}")


def helper(s, dict_s, len_s, current_w, ans_l):
    """
    A helper function for find_anagrams.
    :param s: str, the word that user wants to find anagrams.
    :param dict_s: dict, dictionary for looking up anagrams.
    :param len_s: int, length of s for base case.
    :param current_w: str, stores the string when backtracking.
    :param ans_l: lst, stores the anagrams without duplicate.
    """
    if len(current_w) <= 1:
        for ch in s:
            if dict_s[ch] > 0:
                # Choose
                current_w += ch
                dict_s[ch] -= 1
                # Explore
                helper(s, dict_s, len_s, current_w, ans_l)
                # Un-choose
                dict_s[ch] += 1
                current_w = current_w[:-1]

    elif len(current_w) == len_s:
        if current_w in word_dict[current_w[0:2]]:
            if current_w not in ans_l:
                print("Found: "+current_w)
                print("Searching…")
                ans_l.append(current_w)
    else:
        if not has_prefix(current_w):
            pass
        else:
            for ch in s:
                if dict_s[ch] > 0:
                    # Choose
                    current_w += ch
                    dict_s[ch] -= 1
                    # Explore
                    helper(s, dict_s, len_s, current_w, ans_l)
                    # Un-choose
                    dict_s[ch] += 1
                    current_w = current_w[:-1]


def has_prefix(sub_s):
    """
    :param sub_s: str, a substring to check if any word start with it in the dictionary
    :return: bool, return False if no words start with the substring.
    """
    # Check
    if sub_s[0:2] in word_dict:
        for word in word_dict[sub_s[0:2]]:
            if word.startswith(sub_s):
                return True
    return False


if __name__ == '__main__':
    main()
