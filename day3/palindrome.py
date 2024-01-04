# Input phrase
phrase = input("Phrase: ")

# Reverse phrase
reversed = ""
for c in phrase:
    reversed = c + reversed

# Check if palindrome
if reversed == phrase:
    print("Palindrome.")
else:
    print("Not Palindrome.")