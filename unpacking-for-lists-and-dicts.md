# lists unpacked with *
```python
# we got this
>>> def add(a, b):
...     return a + b
...

# but say we have this args list and want to use it for "range"
>>> addTheseNumbers = [3,5]

>>> add(addTheseNumbers);

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: add() missing 1 required positional argument: 'b'

# we need to use * to unpack lists
>>> add(*addTheseNumbers)
8

```

# dictionaries unpacked with **
```python
>>> def greet(name, origin):
...     return "Hello {} from {}!".format(name, origin)
...

>> me = {"name": "Patrick", "origin": "San Francisco"}

# incorrect no unpacking
>> greet(me)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: greet() missing 1 required positional argument: 'origin'

# incorrect unpacking with * on dictionary
>> greet(*me)
'Hello name from origin'

# correct dictionary unpacking with **
>> greet(**me)
'Hello Patrick from San Francisco'
```
