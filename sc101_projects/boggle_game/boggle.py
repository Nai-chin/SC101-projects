"""
File: boggle.py
Name: Livia Tseng 曾迺芩
----------------------------------------
This program manipulate the boggle game using recursion and backtracking.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global variable
# dict, Store all the vocabulary from FILE
word_dict = []


def main():
	"""
	This program manipulate the boggle game.
	User should input 4 rows of letters that each row has 4 alphabet which separated by single space.
	Then the program will print all the words found and show the number of words found in the end.
	"""
	start = time.time()
	# Prepare the 4 x 4 alphabet grid in dict format:
	# key = index of row, val = lst in lst, store 4 alphabet in each row at index 0, and default 1 at index 1
	letters = {}
	for i in range(4):
		row = input(f'{i + 1} row of letters: ').lower().split()
		if len(row) != 4:
			print('Illegal input')
			break

		for ch in row:
			if not ch.isalpha() or len(ch) != 1:
				print('Illegal input')
				break

		letters[i] = []
		for j in range(len(row)):
			letters[i].append([row[j], 1])

	# for i in range(4):
	# 	row = input(f'{i+1} row of letters: ')
	# 	if len(row) != 7 or row[1] != ' ' or row[3] != ' ' or row[5] != ' ':
	# 		# Length over 7 or not separated by single space
	# 		print('Illegal input')
	# 		break
	# 	elif not row[0].isalpha() or not row[2].isalpha() or not row[4].isalpha() or not row[6].isalpha():
	# 		# Input not alphabet
	# 		print('Illegal input')
	# 		break
	# 	else:
	# 		row = row.lower()
	# 		letters[i] = []
	# 		for j in range(len(row)):
	# 			if row[j] == ' ':
	# 				pass
	# 			else:
	# 				letters[i].append([row[j], 1])

	# Prepare the dictionary for looking up words in grid
	read_dictionary()

	# Start to look up words in the given grid
	boggle(letters)

	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def boggle(letters):
	"""
	This is the boggle game function to look up words in the given grid, letters.
	:param letters: dict, for example, {index of row: [[a, 1], [b, 1], [c, 1], [d, 1]]}
	"""
	ans_l = []
	# Using for loop to go through all the
	for x in range(4):
		for y in range(4):
			cur_w = letters[y][x][0]
			letters[y][x][1] = 0
			helper(letters, cur_w, x, y, ans_l)
			letters[y][x][1] = 1
	print(f"There are {len(ans_l)} words in total.")


def helper(letters, cur_w, x, y, ans_l):
	"""
	This is the helper function of boggle(letters)
	:param letters: dict, the alphabet grid which user input.
	:param cur_w: str, stores the string when backtracking.
	:param x: int, the index of the chosen alphabet within the list (row).
	:param y: int, in which row the chosen alphabet is.
	:param ans_l: lst, stores the words found without duplicate.
	"""
	if has_prefix(cur_w):
		if 4 <= len(cur_w) <= 16:
			if cur_w in word_dict:
				if cur_w not in ans_l:
					print(f"Found \"{cur_w}\"")
					ans_l.append(cur_w)
					# For case room, roomy
					for_loop(letters, x, y, ans_l, cur_w)
			else:
				# For case that length of words longer then 4
				for_loop(letters, x, y, ans_l, cur_w)
		else:
			for_loop(letters, x, y, ans_l, cur_w)


def for_loop(letters, x, y, ans_l, cur_w):
	"""
	This is the function hide the repeated parts of backtracking.
	"""
	for i in range(-1, 2):
		for j in range(-1, 2):
			if x + i < 0 or y + j < 0 or x + i > 3 or y + j > 3:
				# x + i & y + j should within the 4 x 4 grid
				pass
			elif i == 0 and j == 0:
				# The center alphabet which is already added to cur_w
				pass
			elif letters[y + j][x + i][1] == 0:
				# The alphabet is already used
				pass
			else:
				cur_w += letters[y + j][x + i][0]
				letters[y + j][x + i][1] = 0
				helper(letters, cur_w, x + i, y + j, ans_l)
				cur_w = cur_w[:-1]
				letters[y + j][x + i][1] = 1


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global word_dict
	with open(FILE, "r") as f:
		for line in f:
			line = line.strip()
			word_dict.append(line)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in word_dict:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
