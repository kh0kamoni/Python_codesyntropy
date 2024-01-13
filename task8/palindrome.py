# Define palindrome function
def palindrome(*strings):
        return all(string == string[::-1] for string in strings)
    
if palindrome('121', 'mom'):
    print("Palindrome")
else:
    print("Not palindrome")