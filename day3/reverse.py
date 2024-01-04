# Input string
string = input("String: ")

# Reverse string
reversed = ""
for i in string:
    reversed = i + reversed
    
# Print reversed string
print(reversed)