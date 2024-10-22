# AI Assistant question:

Are Python tuples always hashable?

# AI Assistant Answer
Python tuples are generally hashable if all of their elements are also hashable. Hashability means that an object can be used as a key in a dictionary or as an element in a set, which requires it to have a stable hash value that doesn't change over its lifetime.

For a tuple to be hashable, each element it contains must also be hashable. Immutable types like integers, floats, strings, and other tuples are hashable. However, if a tuple contains a mutable object (like a list or dictionary), that tuple becomes unhashable because mutable objects do not have a consistent hash value.

For example:

- A tuple like `(1, 2, 'a')` is hashable.
- A tuple like `(1, [2, 3], 'a')` is **not** hashable because it contains a list, which is mutable and thus unhashable.

You can check whether a tuple is hashable using the `hash()` function:

```python
# Hashable tuple
t1 = (1, 2, 'a')
print(hash(t1))  # This will work

# Unhashable tuple
t2 = (1, [2, 3], 'a')
print(hash(t2))  # This will raise a TypeError
```