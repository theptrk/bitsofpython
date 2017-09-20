- @name: range 
- @returns: <range> immutable sequence of numbers

# why range is awesome

Unlike list and tuple, range returns the same amount of memory since it only
represents the start, stop and step values, calculating the individual values
and subranges as needed

[range](https://docs.python.org/3/library/stdtypes.html#range)

```python
# >>> range(5)
[0,1,2,3,4]

# @signatures: #1
range(stop)
# where stop is excluded from the returned list

# @signatures: #2
range(start, stop[, step])
# where step defaults to 1

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

