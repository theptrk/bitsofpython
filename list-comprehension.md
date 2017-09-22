- @name: list comprehensions
- @returns: list

# why THIS is awesome

haskell + ruby like list comprehensions!

## docs
```python
# @signatures: #1
[<operator expression> for <i> in <list> [if <expression>]]
```

## basic list comprehension
```python
# say we want a list of the squared values of x
>>> x = [1,2,3,4]

# with for loop
>>> y = []
... for num in x:
...     y.append(num**2)
 
# with list comprehension
>>> [num**2 for num in x]
```

## list comprehension with predicate
```python
# say we want a list of the squared values of x larger than 1 but not 3
>>> my_list = [1,2,3,4]

# with list comprehension
>>> [x**2 for x in my_list if x > 1 and x != 3]

# note that the above is the same result as a "filter" and a "map"
>>> map(lambda n: n**2, filter(lambda n: n > 1 and n != 3, my_list))
```

## nested loop behavior
```python
# imagine you want to flatten a matrix

# here is what it looks like with a for loop
flattened = []
for row in matrix:
    for n in row:
        flattened.append(n)

# you sort of flatten the structure, here is the same code on one line
# flattened = [] for row in matrix:for n in row:flattened.append(n)

# here is the equivalent list comprehension
flattened = [n for row in matrix for n in row]

# note that python allows line breaks, so this is the same
flattened = [
    n
    for row in matrix
    for n in row
]
```