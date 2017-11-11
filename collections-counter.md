- @name: Counter objects from collections lib

# why THIS is awesome
Python provides a convienient way to create a counter object from many
different "iterables" or "mappings"
[docs](https://docs.python.org/3/library/collections.html#collections.Counter)

## docs

## Counter comes from the collections class and must be imported
```python
# @import signature:
from collections import Counter

# @signature: create a new Counter
a = Counter()
```

## Counter takes any iterable
```python
# @signature: create a new Counter initialized with a string
b = Counter('yay')

# >>> b['y']
# 2
# >>> b['a']
# 1
# >>> b['h']
# 0

# @signature: create a new Counter initialized with a list (iterable)
c = Counter(['yay', 'hello', 'world', 'yay'])
# >>> c['yay']
# 2
# >>> c['hello']
# 1
# >>> c['earth']
# 0
```

## Counter takes a mapping
```python
# @signature: create a new Counter initialized with a dictionary (mapping)
d = Counter({'red': 4, 'blue': 2})
# >>> d['red']
# 4
```

## AWESOME FUNCTIONALITY - ADDING OR SUBTRACTING COUNTERS
```python
a = Counter({'hello': 2, 'world': 5})
b = Counter({'hello': 1, 'earth': 7})

# adding
a + b
# Counter({'hello': 3, 'world': 5, 'earth': 7})

# subtracting
a - b
# Counter({'hello': 1, 'world': 5})

# subtracting
b - a
# Counter({'earth': 7})
```

## methods
```python
# elements()
# most_common([n])
# subtract([iterable-or-mapping])
```
