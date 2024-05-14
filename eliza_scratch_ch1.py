"function structure"
def double(x):
    """multiplies by 2"""
    return x * 2

def apply_to_one(f):
    """Calls function f with 1 as its argument"""
    return f(31)

my_double = double
x = apply_to_one(my_double)

"special characters"
tab_string = "\t"
raw_tab_string = r"\t"

"default argument values"
def my_print(message = "my default message"):
    print("Certainly! ", message)

"""my_print("hello")
my_print(x)
my_print(tab_string)
my_print(raw_tab_string)"""

first_name = "Eliza"
last_name = "Hubbard"
full_name = f"{first_name} {last_name}"

my_print(full_name)

"exception"

try:
    print(0 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")

"tuple, list format"
x = [0, 1 , 2 , 3, 4]

5 in [1, 2, 3] # false

my_list = [1,2]
my_tuple = (1,2)
other_tuple = 3, 4
my_list[1] = 3
print(my_list)

"dict format"

grades = {"Joel": 80, "Eliza": 95} # defines a grades dictionary with two value-key pairs
print(grades["Joel"])
kate_has_grade = "Kate" in grades
print(kate_has_grade)   # checks to see if Kate has a value in the grades dictionary

joels_grade = grades.get("Joel", 0)     # looks up joel's grade, returns 0 as default if none
kates_grade = grades.get("Kate", 0)

grades["Kate"] = 100                    # now adds a grade for Kate
print(grades["Kate"])


from collections import defaultdict

# Create a defaultdict where each key's default value is an empty list
fruit_colors = defaultdict(list)

# Add fruits to the dictionary
fruit_colors['Red'].append('Apple')
fruit_colors['Yellow'].append('Banana')
fruit_colors['Red'].append('Cherry')
fruit_colors['Purple'].append('Grape')

# Now you can easily access the list of fruits for each color
print(fruit_colors['Red'])    # Output: ['Apple', 'Cherry']
print(fruit_colors['Yellow'])  # Output: ['Banana']

for x in range(10):
    if x == 6:
        continue  # go immediately to the next iteration
    if x == 9:
        break     # quit the loop entirely
"    print(x)"

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

"""print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))"""

import random

print(random.randrange(1,79))

txt = "The best things in life are free!"
"""print("expensive" in txt)"""
print(txt[5:10])

age = 36
txt = "My name is John, and I am {}"
"""txt = f"My name is John, and I am {age}"""
print(txt.format(age))
"print(txt)"

pairs = [(x, y)
         for x in range(10)
         for y in range(10)]   # 100 pairs (0,0) (0,1) ... (9,8), (9,9)

print(pairs)

even_numbers = [x for x in range(5) if x % 2 == 0]  # [0, 2, 4]
squares      = [x * x for x in range(5)]            # [0, 1, 4, 9, 16]
even_squares = [x * x for x in even_numbers]        # [0, 4, 16]


assert even_numbers == [0, 2, 4]
assert squares == [0, 1, 4, 9, 16]
assert even_squares == [0, 4, 16]


names = ["Alice", "Bob", "Charlie", "Debbie", "Edna", "Frank"]

# not Pythonic
"""for i in range(len(names)):
    print(f"name {i} is {names[i]}")"""

# also not Pythonic
"""i = 0
for name in names:
    print(f"name {i} is {names[i]}")
    i += 1"""

# Pythonic
for i, name in enumerate(names, start = 3):
    print(f"name {i} is {name}")