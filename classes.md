- @name: class
- @returns:

# why THIS is awesome

[LINK]()

## docs
```python
# @signatures: #1 - bare example

# declaring a class
class Vehicle:
    pass

# creating an instance 
car = Vehicle()

# @signatures: #2 - full example
class Vehicle:
    def __init__(self, wheels, tank, seating):
        self.wheels = wheels
        self.tank = tank
        self.seating = seating

    # getter
    def wheels(self):
        return self.wheels

    # setter
    def set_wheels(self, number):
        self.wheels = number

# creating an instance 
tesla = Vehicle(4, 'electric', 5)

# @signatures: #3 - pythonic getter and setters
class Vehicle:

    def __init__(self, wheels, tank, seating):
        # ...

    @property
    def wheels(self):
        return self.wheels

    @wheels.setter
    def wheels(self, number):
        self.wheels = number

# creating an instance 
tesla = Vehicle(4, 'electric', 5)
tesla.wheels = 2

# @signatures: #4 - inheritence
class Motorcycle(Vehicle):
    def __init__(self, wheels, tank, seating):
        Vehicle.init(self, wheels, tank, seating)

bike1 = Motorcycle(2, 'gas', 1)

```

## use cases
```python
```

## examples
```python
```
