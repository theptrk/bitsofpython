## lists unpacked with *
```python
# we got this
list(range(3,6))

# but say we have this args list and want to use it for "range"
args = [3,6]

# * to unpack
list(range(*args))
```

## dictionaries unpacked with **
```python
def parrot(state="california", color="blue"):
    print("this {} parrot is from {}".format(color, state)

details = {"state": "hawaii", "color": "blue"}
parrot(**details)
```
