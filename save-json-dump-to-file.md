# filesystem

You might want to save JSON payloads onto a local filesystem for offline use or
backup
[LINK]()

## how to save json data
```python
"""
data is the data from the api endpoint
prefix is the file prefix that we would like to save
"""
import json

def save_data(data, prefix):
    # get a timestamp (optional)
    now = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    if prefix[-1] == '/':
        filepath = prefix + now
    else:
        filepath = prefix + '/' + now

    # open a writable file object
    f = open(filepath, 'w')

    # dump json data to the file
    json.dump(data, f)

    # close the file
    f.close()

    # return the data for a consumer of this function 
    return json.dumps(data)
```
