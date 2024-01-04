sentence = input("Sentence: ")
words = sentence.split()

i = 0

while i < len(words):
    count = 0  # Reset count for each word

    for j in words:
        if words[i] == j:
            count += 1

    print(f'"{words[i]}": {count} times')
    i += 1
