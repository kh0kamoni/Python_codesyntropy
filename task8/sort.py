def sortby_length(*strings):
    return sorted(strings, key=len)

print(sortby_length('kkhoka', 'python', 'c'))