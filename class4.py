stringExample = "Hello, World!"
print(stringExample)

stringExample2 = """Hola

 martin"""  # triple quotes are sensitive to new lines
print(stringExample2)

# string with index
print(stringExample[2])

# last character
print(stringExample[-1])

# reverse
print(stringExample[::-1])

# substring
print(stringExample[2:5])  # [start:end]

# With +
print(stringExample + " " + stringExample2)

# length
print(len(stringExample))

# lower
print(stringExample.lower())

# upper
print(stringExample.upper())

# strip is used to remove whitespace, in javascript it's trim
print(stringExample.strip())

# replace
print(stringExample.replace("World", "Python"))

# split
print("a,b,c".split(","))

# join
print("-".join(["Hello", "Python"]))

# find and index
print(stringExample.find("o"))  # returns -1 if not found
print(stringExample.index("World"))  # raises if not found

# count
print(stringExample.count("l"))

# startswith / endswith
print(stringExample.startswith("Hello"))
print(stringExample.endswith("!"))

# capitalize / title / swapcase
print("hello world".capitalize())
print("hello world".title())
print("Hello WORLD".swapcase())

# is* checks
print("12345".isdigit())
print("Hello".isalpha())
print("Hello123".isalnum())
print("   ".isspace())
print("hello".islower())
print("HELLO".isupper())

# lstrip / rstrip
print("   padded   ".lstrip())
print("   padded   ".rstrip())

# center / ljust / rjust
print("center".center(10, "-"))
print("left".ljust(8, "."))
print("right".rjust(8, "."))

# splitlines / partition
print("Line1\nLine2".splitlines())
print("a,b,c".partition(","))

print("---- List Methods ----")
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)
numbers.extend([5, 6])
print(numbers)
numbers.insert(1, 1.5)
print(numbers)
numbers.remove(1.5)
print(numbers)
last_item = numbers.pop()
print(last_item, numbers)
print(numbers.index(2))
print(numbers.count(2))
numbers_copy = numbers.copy()
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)
numbers_copy.clear()
print(numbers_copy)

print("---- Dict Methods ----")
person = {"name": "Alice", "age": 30}
print(person.get("city", "Unknown"))
print(list(person.keys()))
print(list(person.values()))
print(list(person.items()))
person.update({"city": "NYC"})
print(person)
removed_age = person.pop("age")
print(removed_age, person)
key, value = person.popitem()
print(key, value, person)
print(person.setdefault("country", "USA"))
print(person)
person_copy = person.copy()
person.clear()
print(person, person_copy)

print("---- Set Methods ----")
set_a = {1, 2, 3}
set_b = {3, 4}
set_a.add(4)
print(set_a)
set_a.update({5, 6})
print(set_a)
set_a.remove(6)
set_a.discard(10)
print(set_a)
popped_value = set_a.pop()
print(popped_value, set_a)
print(set_a.union(set_b))
print(set_a.intersection(set_b))
print(set_a.difference(set_b))
print(set_a.symmetric_difference(set_b))
print(set_a.issubset(set_a.union(set_b)))
print(set_a.issuperset({3}))
set_a.clear()
print(set_a)

print("---- Tuple Methods ----")
coords = (1, 2, 2, 3)
print(coords.count(2))
print(coords.index(3))
