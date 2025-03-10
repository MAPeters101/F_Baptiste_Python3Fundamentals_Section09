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
print('-'*80)

s1 = set('abc')
s2 = set('abcd')
print(s1 < s2)
print(s1 <= s2)
print(s2 >= s1)
print(s2 > s1)
s3 = set('abc')
print(s1 < s3)
print(s1 <= s3)
print(s1 == s3)
print('-'*80)


s1 = set('abc')
s2 = set('bcd')
print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s2 - s1)
print('-'*80)


str_1 = 'python is an awesome language!'
str_2 = 'a python is also a snake'
set_1 = set(str_1)
set_2 = set(str_2)
print(set_1)
print(set_2)
print(set_1 & set_2)
print()

s1 = {'FB', 'AMZN', 'AAPL', 'NFLX', 'GOOG', 'MSFT'}
s2 = {'BABA', 'WMT', 'COST'}
s3  = {'TSLA', 'F', 'GM'}
consolidated = s1 | s2 | s3
print(consolidated)

consolidated = list(s1 | s2 | s3)
print(consolidated)
print('='*80)


sold = {'w1', 'w2', 'w3', 'w4'}
returned = {'w1'}
non_returned = sold - returned
print(non_returned)









