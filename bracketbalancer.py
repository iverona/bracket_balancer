import re

def is_balanced(input_string):
	'''
	Check if a given string is balanced in terms of
	brackets: (),{} and []

	An empty string is considered as valid
	'''
	symbols = {'}':'{', ')':'(', ']':'['}

	cleaned_string = ''.join(re.findall("[()\[\]{}]", input_string))

	# Preliminary check
	if (len(cleaned_string)%2 != 0):
		return False

	chars_stack = []

	for char in cleaned_string:
		if char in symbols.values():
			chars_stack.append(char)
		else:			
			if not symbols[char] == chars_stack.pop():
				return False

	return True
