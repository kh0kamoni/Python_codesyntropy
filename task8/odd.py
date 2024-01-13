# Define odd detector
def odds(*numbers):
    odd_list = []
    for number in numbers:
        if number % 2 == 0:
            odd_list += [number]
    return odd_list
        

print(odds(2, 3, 4, 5, 6, 7, 8))