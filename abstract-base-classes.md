# abstract base classes (abc)

- similar to Java interfaces or Haskell typeclasses, use these when you want to 
create a template of functionality that other "classes" need to implement. In
python this process is called "virtual subclassing"

- why virtual? a real subclass knows its relationship with the parent class
  through its `__bases__` attribute, and can thus implicitly delegate the
resolution of missing methods. A virtual subclass knows nothing about the class
that registered it, and nowhere in the subclass will you find something that
links it to the parent class. *Thus, a virtual parent class is useful only as a
categorization*

- mro()? No. ABCs will not be represented in a classes MRO.

## how to break the agreement
```python
import abc

class myABC(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self):
        pass

class Concrete(myABC):
    pass

kale = Concrete()
# TypeError: Can't instantiate abstract class myABC with abstract methods get
```

## how to honor the agreement
```python
import abc

class myABC(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self):
        pass

class Concrete(myABC):
    def get(self):
        print("I am gettin' it")

kale = Concrete()
kale.get()
# I am gettin' it
```

### example uses in `_collections_abc.py`
```python
from abc import ABCMeta

# ...
class Sequence(metaclass=ABCMeta):
    # ...

# ...
Sequence.register(tuple)
Sequence.register(str)
Sequence.register(range)
# ...
```
sources:
[thedigitalcatonline](http://blog.thedigitalcatonline.com/blog/2016/04/03/abstract-base-classes-in-python/)
[python docs](https://docs.python.org/3/library/abc.html)
