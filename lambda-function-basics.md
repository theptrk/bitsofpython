# lambda expression roadmap

## this is how to go from a named function to a lambda function
```python
## start with a named function
def add(a, b):
    return a + b

# step 1: delete "def", function name and whitespace
# >>> (a, b): return a + b

# step 2: delete return
# >>> (a, b): a + b

# step 3: add "lambda" and now you have a lambda function
lambda a, b: a + b

# test drive
# >>> (lambda a, b: a + b)(10, 20)
# 30
```

# map and filter with lambdas
```python
seq = [1,2,3,4,5]

# get a list of squared "seq" items
map(lambda num: num * 2, seq)
# [2,4,6,8,10]

# get a list of even "seq" items
filter(lambda num: num % 2 == 0, seq)
# [2,4]

# note map and filter are lazy and produce an iterator
# we would use list() here to be able to print the result
```

# reduce with lambdas
```python
# reduce was taken out of the language proper in Python3 so must be imported
from functools import reduce

# reduce takes a lambda
# >>> reduce((lambda x, y: x * y), [1,2,3,4])
24

# reduce takes an optional initial value
# >>> reduce((lambda x, y: x + y), [1,2,3,4], 500)
510
```
