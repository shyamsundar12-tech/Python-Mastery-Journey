# ============================================================
# PYTHON COLLECTIONS — BEGINNER NOTES
# Topics: List, Tuple, Set, Dictionary
# ============================================================


# ============================================================
# 1. LIST
# ============================================================

# A list:
# 1. Is ordered.
# 2. Allows duplicate values.
# 3. Can store different data types.
# 4. Is mutable (we can add, remove, or change items).
# 5. Supports positive and negative indexing.

a = [1, 2, 3, 4, 5]

# Accessing elements using positive indexing
print(a[0])  # First element: 1
print(a[1])  # Second element: 2
print(a[2])  # Third element: 3

# Accessing elements using negative indexing
print(a[-1])  # Last element: 5
print(a[-2])  # Second-last element: 4

# Finding the number of elements
print(len(a))  # Output: 5

# append() — adds ONE item at the end
a.append(6)
print(a)  # [1, 2, 3, 4, 5, 6]

# insert(index, value) — adds an item at a position
# Existing elements shift to the right.
a.insert(1, 10)
print(a)  # [1, 10, 2, 3, 4, 5, 6]

# Modifying an existing element
a[1] = 20
print(a)  # [1, 20, 2, 3, 4, 5, 6]

# extend() — adds elements from another iterable
b = [7, 8, 9]
a.extend(b)
print(a)  # [1, 20, 2, 3, 4, 5, 6, 7, 8, 9]

# append() vs extend()
x = [1, 2]
x.append([3, 4])
print(x)  # [1, 2, [3, 4]] — adds one nested list

y = [1, 2]
y.extend([3, 4])
print(y)  # [1, 2, 3, 4] — adds two individual elements

# remove(value) — removes the first matching value
numbers = [10, 20, 30, 20]
numbers.remove(20)
print(numbers)  # [10, 30, 20]

# pop(index) — removes and returns an item by index
numbers = [10, 20, 30, 40, 50]
removed = numbers.pop(2)
print(removed)  # 30
print(numbers)  # [10, 20, 40, 50]

# pop() without an index removes and returns the last item
removed = numbers.pop()
print(removed)  # 50
print(numbers)  # [10, 20, 40]

# del — removes an item by index
del numbers[0]
print(numbers)  # [20, 40]

# clear() — removes all items but keeps the list variable
numbers.clear()
print(numbers)  # []

# Checking whether a value exists
a = [10, 20, 30, 40, 50]
print(30 in a)      # True
print(100 in a)     # False
print(100 not in a) # True

# Looping through list elements
for item in a:
    print(item)

# Counting even numbers
numbers = [10, 15, 20, 25, 30, 35, 40]
count = 0

for item in numbers:
    if item % 2 == 0:
        count += 1

print("Even count:", count)  # 4

# Useful built-in functions
numbers = [10, 20, 30, 40, 50]

print(sum(numbers))  # Total: 150
print(max(numbers))  # Largest: 50
print(min(numbers))  # Smallest: 10
print(len(numbers))  # Count: 5

average = sum(numbers) / len(numbers)
print("Average:", average)  # 30.0

# A list can store different data types
mixed = [10, "Python", 3.5, True]
print(mixed)


# ============================================================
# 2. TUPLE
# ============================================================

# A tuple:
# 1. Is ordered.
# 2. Allows duplicate values.
# 3. Can store different data types.
# 4. Is immutable (its items cannot be reassigned).
# 5. Supports indexing and negative indexing.

a = (10, 20, 30, 40, 20)

# Accessing elements
print(a[0])   # 10
print(a[-1])  # 20

# Finding the number of elements
print(len(a))  # 5

# Checking membership
print(30 in a)  # True

# Counting occurrences of a value
print(a.count(20))  # 2

# Finding the index of the first matching value
print(a.index(30))  # 2

# Looping through a tuple
for item in a:
    print(item)

# Tuples cannot be modified directly.
# For example, a[0] = 100 would raise a TypeError.

# Converting a tuple into a list
b = list(a)
b[0] = 100
print(b)  # [100, 20, 30, 40, 20]

# The original tuple remains unchanged
print(a)  # (10, 20, 30, 40, 20)

# Converting a list into a tuple
c = tuple(b)
print(c)

# A one-element tuple needs a trailing comma
single = (10,)
print(type(single))  # <class 'tuple'>


# ============================================================
# 3. SET
# ============================================================

# A set:
# 1. Stores unique elements (duplicates are removed).
# 2. Does not support indexing.
# 3. Is mutable — elements can be added or removed.
# 4. Does not guarantee a meaningful display order.
# 5. Requires its elements to be hashable.

a = {1, 2, 3, 4}
print(a)

# Duplicate values are ignored
b = {1, 2, 3, 4, 1, 2}
print(b)  # {1, 2, 3, 4} — display order may vary

# Adding one element
a.add(10)
print(a)

# Adding multiple elements from an iterable
a.update([20, 30])
print(a)

# remove(value) — removes the value
# Raises KeyError if the value does not exist.
a.remove(3)
print(a)

# discard(value) — removes the value if present
# Does not raise KeyError if the value is absent.
a.discard(100)
print(a)

# pop() — removes and returns an arbitrary element
# It does not mean "remove the first element."
removed = a.pop()
print("Removed:", removed)
print(a)

# Checking membership
print(10 in a)

# Set operations
x = {1, 2, 3, 4}
y = {3, 4, 5, 6}

# Union: elements from both sets
print(x.union(y))  # {1, 2, 3, 4, 5, 6}

# Intersection: elements common to both sets
print(x.intersection(y))  # {3, 4}

# Difference: elements in x but not in y
print(x.difference(y))  # {1, 2}

# Removing all elements while keeping the set
x.clear()
print(x)  # set()

# An empty set must be created with set(), not {}
empty_set = set()
print(type(empty_set))  # <class 'set'>

# {} creates an empty dictionary, not an empty set.
empty_dictionary = {}
print(type(empty_dictionary))  # <class 'dict'>


# ============================================================
# 4. DICTIONARY
# ============================================================

# A dictionary:
# 1. Stores key-value pairs.
# 2. Is mutable.
# 3. Uses unique keys.
# 4. Preserves insertion order in modern Python.
# 5. Uses keys to access values instead of numeric indexes.
# 6. Requires keys to be hashable.

student = {
    "name": "Shyam",
    "age": 20,
    "gender": "male"
}

# Accessing values using keys
print(student["name"])    # Shyam
print(student["age"])     # 20
print(student["gender"])  # male

# get() — safely retrieves a value
print(student.get("age"))  # 20
print(student.get("grade", "Not available"))

# Adding a new key-value pair
student["course"] = "AI & ML"
print(student)

# Updating an existing value
student["age"] = 21
print(student)

# update() — adds or updates one or more key-value pairs
student.update({"age": 22, "city": "Chennai"})
print(student)

# pop(key) — removes a key and returns its value
removed_age = student.pop("age")
print("Removed age:", removed_age)
print(student)

# Checking whether a key exists
print("name" in student)  # True
print("age" in student)   # False

# Important: 'in' checks dictionary keys by default.
print("Shyam" in student)  # False — checks keys, not values

# Accessing keys
print(student.keys())

# Accessing values
print(student.values())

# Accessing key-value pairs
print(student.items())

# Looping through keys
for key in student:
    print(key)

# Looping through values
for value in student.values():
    print(value)

# Looping through both keys and values
for key, value in student.items():
    print(key, ":", value)

# pop() removes one key; clear() empties the dictionary.
student.clear()
print(student)  # {}

# del student deletes the variable itself.
# After that, using student again would raise NameError.
# Example:
# del student


# ============================================================
# 5. QUICK COMPARISON
# ============================================================

# LIST:
# Ordered, indexed, mutable, duplicates allowed.
# Example: [10, 20, 20, 30]

# TUPLE:
# Ordered, indexed, immutable, duplicates allowed.
# Example: (10, 20, 20, 30)

# SET:
# Unique elements, no indexing, mutable collection.
# Example: {10, 20, 30}

# DICTIONARY:
# Key-value pairs, mutable, unique keys.
# Example: {"name": "Shyam", "age": 20}


# ============================================================
# END OF PYTHON COLLECTIONS NOTES
# ============================================================
