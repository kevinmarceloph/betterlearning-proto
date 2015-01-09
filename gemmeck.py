'''
plus_two = lambda x: x + 2
listy = [2, 10, 8, 7]
plused_two = map(plus_two, listy)
print plused_two

is_even = lambda x: x % 2 == 0
listy = [2, 10, 8, 7]
evens = filter(is_even, listy)
print evens

listy = [2, 10, 8, 7]
plus = lambda x, y: x + y
total = reduce(plus, listy)
print total

total = sum(listy)
print total
'''


number = int(raw_input('Enter your number: '))
listy = range(1, number + 1)
condition = lambda x: x % 3 == 0 or x % 5 == 0
filtered = filter(condition, listy)
print sum(filtered)
