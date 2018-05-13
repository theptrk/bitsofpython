- @name: collections > defaultdict
- @returns:

# why THIS is awesome

python will throw an error on a regular undefined dictionary lookup

```
empty_dict = {}
y = empty_dict["kale"]

#KeyError!
```

often you use a dictionary to count items, defaultdict uses your set default as
the return value when something is undefined

[LINK]()

## docs
```python
# @signatures: #1 int default
defaultdict(int)

# @signatures: #2 list default
defaultdict(list)

# @signatures: #3 dict default
defaultdict(dict)
```

## use cases
```python
# @signatures: #1 int default and adding to value
word_counts = defaultdict(int)
for word in document: 
    word_counts[word] += 1

# @signatures: #2 list default and appending to list
my_lists = defaultdict(list)
my_lists[2].append(1)                   # my_lists contains {2: [1]}

# @signatures: #3 dict default and setting dictionary values
my_lists = defaultdict(dict)
my_lists["Joel"]["City"] = "Seattle"    # { "Joel": { "City":"Seattle"}}
```

## examples
```python
```
