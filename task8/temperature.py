def celsius_to_fahrenheit(*temperatures):
    return [(celsius * 9/5) + 32 for celsius in temperatures]

print(celsius_to_fahrenheit(38))