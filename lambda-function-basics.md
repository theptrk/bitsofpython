# lambda expression roadmap
```python
## start here
def times_two(var):
        return var * 2

# delete "def", function name and whitespace
# >>> (var): return var*2

# delete return
# >>> (var): var*2

# add "lambda"
# >>> lambda var: var*2
```

# map and filter with lambdas
```python
seq = [1,2,3,4,5]

# get a list of squared "seq" items
list(map(lambda num:num*2, seq))

# get a list of even "seq" items
list(filter(lambda num:num%2 == 0, seq))
```

# reduce with lambdas
```python
from functools import reduce

# reduce takes a lambda
# >>> reduce((lambda x, y: x * y), [1,2,3,4])
24

# >>> reduce((lambda x, y: x + y), [1,2,3,4])
10
```
