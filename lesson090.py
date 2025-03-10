s1 = set('abc')
s2 = {True, False}
s3 = {'a', 100, 200}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))
print(s3.isdisjoint(s1))
print()

s = set()
s.add(100)
print(s)

s.add(200)
print(s)

s.add(200)
print(s)
print('-'*80)


s = set('abc')
print(s.remove('a'))
print(s)
print(s.discard('b'))
print(s)
s.discard('x')
print(s)
#s.remove('x')





