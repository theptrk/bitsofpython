[ ] imports
```python
import csv
import json
```

[ ] seperate the header and the data; convert data to list
```python
with open('./somedir/somefile.csv', newline='') as f:
    reader = csv.reader(f)
    header = next(reader)
    data = [row for row in reader]
```

[ ] optional: fn to convert your list to dicts; note: this will increase
overall memory footprint since we are copying keys
```python
def convert_to_dicts(header, data):
    results = []
    for line in data:
        line_dict = {}
        for i, val in enumerate(line):
            line_dict[header[i]] = val
        results.append(line_dict)
    return results
```

[ ] filter the data as needed
```python
only_certain_lines = [line for line in dicts 
                    if line["Taxes"] 
                    and line["Shipping Province"] == "CA"]
```

[ ] sum as needed
```python
sum_subtotal = sum(float(line["Subtotal"]) for line in only_certain_lines)
```

[ ] use a Counter object to count things
```python
from collections import Counter

# here we will some the "Subtotal" fields by "Shipping City"
my_counter = Counter()
for line in only_certain_lines:
    my_counter[line["Shipping City"].title()] += float(line["Subtotal"])
    
# print the subtotals of the line items
for x,y in dict(city_count).items():
    print(f'{x} : ${round(y,2)}')
```
