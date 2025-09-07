stringExample = "Hello, World!"
print(stringExample)

stringExample2 = '''Hola

 martin''' #triple quotes are sensitive to new lines
print(stringExample)

# string with index
print(stringExample[2])

# reverse
print(stringExample[-1])

# sum
print(stringExample[2:5]) # [start:end]

# With +
print(stringExample + " " + stringExample2)

# length
print(len(stringExample))

# lower
print(stringExample.lower())

# upper
print(stringExample.upper())

# strip is used to remove whitespace
print(stringExample.strip())