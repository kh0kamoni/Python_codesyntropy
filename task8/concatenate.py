# Define fuction to concatenate abitrary string as argument input
def concatenate(*strings):
    joined_string = ' '.join(strings)
    return joined_string

# Print concatenated string
print(concatenate("Hello", "World", "!"))