"""
Question 1
You are given a list of strings from which you want to generate all the unique values.

For example, if you were given this list:

['a', 'A', 'b', 'B', 'B', 'A', 'a', 'c']
your result should contain these values:

['a', 'A', 'b', 'B', 'c']
Note that the order of the elements in the resulting list is not important.

You can use this list for this exercise.

l = ['AAPL', 'AAPL', 'Aapl', 'aapl', 'MSFT']
Solution
The simplest way to get all unique values from a list is simply to make a set out of it:

unique_values = set(l)
unique_values
{'AAPL', 'Aapl', 'MSFT', 'aapl'}
Question 2
Using the same data we saw in Question 1, the goal is to find all the unique values in a case-insensitive fashion.

For example, AAPL, Aapl and aapl should each be considered to be the same value.

Solution
For this we'll use casefold() to first casefold each string.

We could certainly first create a list with the casefolded strings, and then make a set out of it:

l2 = []
for symbol in l:
    l2.append(symbol.casefold())
l2
['aapl', 'aapl', 'aapl', 'aapl', 'msft']
unique_values = set(l2)
unique_values
{'aapl', 'msft'}
This works, but we could also just add the casefolded strings to a set directly.

We create an empty set first:

unique_values = set()
Then we loop through the strings, and add the casefolded version of the string to the set:

for symbol in l:
    unique_values.add(symbol.casefold())
unique_values
{'aapl', 'msft'}
Later, we'll study comprehensions and see another way of doing this:

unique_values = {symbol.casefold() for symbol in l}
unique_values
{'aapl', 'msft'}
Don't worry if you don't quite understand this code yet, we'll get there soon! I just wanted to show you that this alternative, using a set comprehension, is a very simple way of solving this problem.

Question 3
Given this data structure:

data = {
    'd1': {'a': 1, 'b': 2, 'c': 3},
    'd2': {'b': 20, 'c': 30, 'd': 40},
    'd3': {'d': 100, 'x': 200}
}
Find all the unique keys in the sub-dictionaries.

In this case above, your result should be:

{'a', 'b', 'c', 'd', 'x'}
Of course, the order in the result is irrelevant (there is no ordering in sets).

Solution
We can recover the keys of a dictionary using the keys() method, and we know that dictionary keys also behave like sets - and we can find the union of sets.

data['d1'].keys()
dict_keys(['a', 'b', 'c'])
And we can union these keys across all three dictionaries:

data['d1'].keys() | data['d2'].keys() | data['d3'].keys()
{'a', 'b', 'c', 'd', 'x'}
This works fine, but the issue is that we assumed that there were three items in data, named d1, d2, and d3.

This is not very generic code.

Instead, we could approach the problem this way.

First we can just loop over the values in data - those will be the sub-dictionaries:

for d in data.values():
    print(d)
{'a': 1, 'b': 2, 'c': 3}
{'b': 20, 'c': 30, 'd': 40}
{'d': 100, 'x': 200}
Now, we can start with an empty set and keep replacing this set with it's union with the keys of each dictionary:

result = set()
for d in data.values():
    result = result | d.keys()

result
{'a', 'b', 'c', 'd', 'x'}
As you can see, this code makes no assumption about the number of entries in data.
"""