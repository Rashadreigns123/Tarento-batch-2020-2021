" " "1. Given four strings A, B, C, D, write a program to check if D is an interleaving of A, B and C. D is said to be an interleaving of A, B and C, if it contains all characters of A, B, C and the order of all characters in individual strings should be preserved." " "


# Function to check if D is an interleaving of A,B  and C or not
def interleaved(A,B,C, D):

	# return true if we have reached end of all Strings
	if not A and not B and not C and not D:
		return True

	# return false if we have reached the end of D
	# but A or B or C are not empty
	if not D:
		return False

	# if A is not empty and its first character matches with
	# first character of D, recur for remaining substring
	if A and D[0] == A[0]:
		return interleaved(A[1:], B,C,D[1:])

	# if B is not empty and its first character matches with
	# first character of D, recur for remaining substring
	if B and D[0] == B[0]:
		return interleaved(A, B[1:], C,D[1:])
		
	# if C is not empty and its first character matches with
	# first character of D, recur for remaining substring
	if C and D[0] == C[0]:
		return interleaved(A,B,C[1:],D[1:])	
		

	return False
	
#taking input
A =input("Enter the A string: ")
B =input("Enter the B string: ")
C =input("Enter the C string: ")
D =input("Enter the D string: ")

if interleaved(A, B, C, D):
  print("D=ABC")
else:
  print("Cannot be interleaved")


	





