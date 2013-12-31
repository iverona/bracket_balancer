import re

def isBalanced(input_string):
	'''
	Check if a given string is balanced in terms of
	brackets: (),{} and []

	An empty string is considered as valid
	'''
	openings, closings = "{[(", "}])"

	opening_chars, closing_chars = [], []

	cleaned_string = ''.join(re.findall("[()\[\]{}]", input_string))

	# Preliminary check
	if (len(input_string)%2 != 0):
		return False

	for char in input_string:
		if char in openings:
			opening_chars.append(char)
		else:			
			if isCorrectClosing(opening_chars.pop(), char):
				continue
			else:
				return False

	return True

def isCorrectClosing(opening, closing):
	'''
	Might be achieved using the openings 
	and closings positions, but looks 
	cleaner this way
	'''

	if (opening == "(" and closing == ")"
	or opening == "[" and closing == "]"
	or opening == "{" and closing == "}"):
		return True

	return False
