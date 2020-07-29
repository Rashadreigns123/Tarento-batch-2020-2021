# Accept a String input-Verify whether the pairs and the orders of "{", "}", "(", ")", "[", "]" are correct in exp. Print well formed if every opening brace has an equivalent closing brace.Print invalid if every opening brace does not have an equivalent closing brace"""

# function to check if 
# paranthesis are balanced 
def areParanthesisBalanced(expr) : 
	stack = [] 

	# Traversing the Expression 
	for char in expr: 
		if char in ["(", "{", "["]: 

			# Push the element in the stack 
			stack.append(char) 
		else: 

			# IF current character is not opening 
			# bracket, then it must be closing. 
			# So stack cannot be empty at this point. 
			if not stack: 
				return False
			current_char = stack.pop() 
			if current_char == '(': 
				if char != ")": 
					return False
			if current_char == '{': 
				if char != "}": 
					return False
			if current_char == '[': 
				if char != "]": 
					return False

	# Check Empty Stack 
	if stack: 
		return False
	return True


# Driver Code 
if __name__ == "__main__" : 
	expr = input("Enter the string to be verified: ") 
	if areParanthesisBalanced(expr) : 
		print("Balanced"); 
	else : 
		print("Not Balanced"); 



