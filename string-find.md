# find the existence of a substring

## method 1: in

```python
# case insensitive
def substring_finder(str, substr):
    return substr in str.lower()
```
## method 2: find
```python
def substring_finder2(str, substr):
    return str.lower().find(substr) > -1
```
