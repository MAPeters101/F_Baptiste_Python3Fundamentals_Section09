s = {'a', 'b', 'c'}
print(s)
print(type(s))
print()

s = set(['a', 'b', 'c'])
print(s)
print(type(s))
print()

s = set('abc')
print(s)
print(type(s))
print()

s = set('python')
print(s)
print(type(s))
print()

s = set(['a', 'a', 'b', 'b'])
print(s)
print(type(s))
print()

s = set('banana')
print(s)
print(type(s))
print()

s = {}
print(s)
print(type(s))
print()

s = set()
print(s)
print(type(s))
print(len(s))
print('-'*80)


s = set('python')
print('p' in s, 'x' not in s)
for item in s:
    print(item)

s2 = s.copy()
print(s2)

from copy import deepcopy
s2 = deepcopy(s)
print(s2)
