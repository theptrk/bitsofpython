"""
This is how we use try:except:
Here the try block executes to completion
"""
obj = {
    "one": 1
}
try:
    print("in the try block accessing existing key")
    obj["one"] 
    print("finished try block")
except: 
    print("exception block")

"""
Here the try block breaks on accessing an object on a nonexistent key
"""
try:
    print("in the try block accessing non-existent key")
    obj["yo"] 
    print("finished try block")
except: 
    print("exception block")

"""
Here the try block breaks on dividing by zero
"""
try:
    print("in the try block dividing by zero")
    10/0
    print("finished try block")
except: 
    print("exception block")


"""
Here the try block breaks importing an uninstalled module
"""
try:
    print("in the try block trying to import an uninstalled module")
    import requests
    r = requests.get('https://api.github.com/events')
    print("finished try block")
except: 
    print("exception block")

