"""
Question 1
You are given a list of strings from which you want to generate all the unique
values.

For example, if you were given this list:

['a', 'A', 'b', 'B', 'B', 'A', 'a', 'c']
your result should contain these values:

['a', 'A', 'b', 'B', 'c']
Note that the order of the elements in the resulting list is not important.

You can use this list for this exercise.

l = ['AAPL', 'AAPL', 'Aapl', 'aapl', 'MSFT']
Question 2
Using the same data we saw in Question 1, the goal is to find all the unique
values in a case-insensitive fashion.

For example, AAPL, Aapl and aapl should each be considered to be the same
value.

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
"""