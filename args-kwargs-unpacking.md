- @name: args, kwargs for unpacking

# why THIS is awesome

case: you want to deal with functions that take arbitrary arguments

[LINK]()

## docs
```python
```

## use cases
```python
# @signatures: #1 unpacking a list in a function

add(1, 2)       # returns 3
add(*[1,2])     # returns 3

# @signatures: #2 *args and **kwargs

def magic(*args, **kwargs):
    print("unnamed args", args)
    print("keyword args:", kwargs)

magic(1,2, kale="veg", cali="table")
# unnamed args (1, 2)
# keyword args: {'kale': 'veg', 'cali': 'table'}
```

## examples
```python
```
