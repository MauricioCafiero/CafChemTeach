# Some basics of Python
See below for examples of basic concepts in Python.

- [Basic For Loops](#basicforloops) <br>
- [For loops for lists/iterables](#forloopsforlists) <br>
- [For loops for dictionaries](#forloopsfordictionaries) <br>

## Basic For Loops 

### Basic loop over a range
Goes from 0 to one less than the arguement.
```
for i in range(10):
  value = i*i
  print(f"The square of {i} is {value}")
```

## For Loops for Lists
### Loop over an iterable
This can be a loop over a list, or a Dataframe column.
```
value_list = [0, 1, 2, 3, 4]

for value in value_list:
  val_squared = value*value
  print(f"The square of {value} is {val_squared}")
```
### Loop over an iterable with enumeration
Adds a counting variable to the loop.
```
value_list = [0, 1, 2, 3, 4]

for i, value in enumerate(value_list):
  val_squared = value*value
  print(f"The square of value {i+1} is {val_squared}")
```
### Loop over two iterables with zip
Loops over two iterables of the same length.
```
value_list = [0, 1, 2, 3, 4]
val_squared_list = [0, 1, 4, 9, 16]

for value, square in zip(value_list, val_squared_list):
  print(f"The square of {value} is {square}") 
```
### List comprehension
For loop contained in a list definition:
```
value_list = [0, 1, 2, 3, 4]

val_squared_list = [value*value for value in value_list]
```
or with conditions:
```
value_list = [0, 1, 2, 3, 4]

val_squared_list = [value*value for value in value_list if value % 2 == 0]
```

## For Loops for Dictionaries
### Loop over a dictionary by keys and values
Loop over keys and cooresponding values simultaneously.
```
mol_dict = {"methane": "CH4", "ethane": "C2H6", "ammonia": "NH3"}

for key, value in mol_dict.items():
  print(f"The formula for {key} is {value}")
```
### Loop over a dictionary by keys only
Loop over keys in a dictionary.
```
mol_dict = {"methane": "CH4", "ethane": "C2H6", "ammonia": "NH3"}

print("The molecules available in the list are:")
for mol in mol_dict.keys():
  print(f"{mol}")
```
### Loop over a dictionary by values only
Loop over values in a dictionary.
```
mol_dict = {"methane": "CH4", "ethane": "C2H6", "ammonia": "NH3"}

print("The formulae available in the list are:")
for mol in mol_dict.values():
  print(f"{mol}")
```
