import re

def isBalanced(input_string):
	'''
	Check if a given string is balanced in terms of
	brackets: (),{} and []

	An empty string is considered as invalid
	'''

	opening_chars, closing_chars = [], []

	# Preliminary checks
	if (not checkString(input_string) 
		or len(input_string)%2 != 0
		or len(input_string) == 0):
		return False

	for char in input_string:
		if isOpening(char):
			opening_chars.append(char)
		else:			
			if isCorrectClosing(opening_chars.pop(), char):
				continue
			else:
				return False

	return True

def isOpening(input_char):
	return re.match("^[({\[]*$", input_char)

def checkString(input_string):
	return re.match("^[()\[\]{}]*$", input_string)

def isCorrectClosing(opening, closing):
	if (opening == "(" and closing == ")"
	or opening == "[" and closing == "]"
	or opening == "{" and closing == "}"):
		return True

	return False
