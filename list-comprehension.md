- @name: list comprehensions
- @returns: list

# why THIS is awesome

haskell + ruby like list comprehensions!

## docs
```python
# @signatures: #1
[<operator expression> for <i> in <list> [if <expression>]]

[docs](https://docs.python.org/3/tutorial/datastructures.html)
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
>>> [num**2 for num in x] ```

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
# goal: flatten a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# for loop method: 
flattened = []
for row in matrix:
    for n in row:
        flattened.append(n)

# list comprehension method: 
# note: later `for`s can use the results of earlier ones
flattened = [n for row in matrix for n in row]

# note: python allows line breaks, so this is the same
flattened = [
    n
    for row in matrix
    for n in row
]

# note: if statements work after the `for in`
flattenedOver5 = [n for row in matrix for n in row if n > 5]
```

## double for different lists

```python
# this returns a list of tuples if the corresponding items are not equal
[(x,y) for x in [1,2,3] for y in [3,1,4] if x !=y]
```

## to dict and set
```python
# dict
square_dict = { x: x * x in range(5)]

# set
square_set =  { x * x in range(5)]
```

## convention: use _ when ignoring the value
```python
import random
four_uniform_randoms = [random.random() for _ in range(4)]
```

## dont try this at home: transposing a matrix
```python
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
[[row[i] for row in matrix] for i in range(4)]

# which is the same as zip
list(zip(*matrix))

# see unpacking argument lists for the * explanation
```
