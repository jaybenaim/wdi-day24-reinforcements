
SUFFIXES = {1: 'st', 2: 'nd', 3: 'rd'}
def ordinal(num):
    if 10 <= num % 100 <= 20:
        suffix = 'th'
    else:
        suffix = SUFFIXES.get(num % 10, 'th')
    return str(num) + suffix


print(ordinal(21))
print(ordinal(22))
print(ordinal(23))
print(ordinal(24))
print(ordinal(2))





