- @name: range 
- @returns: <range> immutable sequence of numbers as an "iterator"

# why range is awesome

Unlike list and tuple, range returns the same amount of memory since it only
represents the start, stop and step values, calculating the individual values
and subranges as needed

[range](https://docs.python.org/3/library/stdtypes.html#range)

## docs
```python
# >>> range(5)
[0,1,2,3,4]

# @signatures: #1
range(stop)
# where stop is excluded from the returned list

# @signatures: #2
range(start, stop[, step])
# where step defaults to 1
```

## use cases
```python
# we use these for looping
>>> for i in range(6):
...     print(i)
0
1
2
3
4
5

# we can loop over a len(list) with range
>>> numbers = ['one', 'two', 'three', 'four', 'five']
>>> for i in range(0, len(numbers)):
...     print(numbers[i])
... 
one
two
three
four
five

# we can nest to loop over list, then loop over items
>>> list = ['a', 'bb', 'ccc']
>>> for word in list:
...     for letter in word:
...             print(letter)
...
a
b
b
c
c
c
```

## examples
```python
# >>> list(range(5))
[0, 1, 2, 3, 4]
# >>> list(range(1, 5))
[1, 2, 3, 4]
# >>> list(range(0, 20, 5))
[0, 5, 10, 15]
# >>> list(range(0, 7, 3))
[0, 3, 6]
# >>> list(range(0, -5, -1))
[0, -1, -2, -3, -4]
# >>> list(range(0))
[]
# >>> list(range(1, 0))
[]
```
