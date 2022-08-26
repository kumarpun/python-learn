# Type of data or value is known as data type
#
# 5 data types in python
# 1. Number
# 2. String
# 3. List
# 4. Tuple
# 5. Dictionary

"""
By using type() method we can find the type of a variable
"""

a = 5
b = 5.2
c = "python"
d = 5j
print(type(a))
print(type(b))
print(type(c))
print(type(d))

"""
List = Storing the different data type value in order, list is changeable in run time, allow duplicate values
values should be assign to a variable in '[]'
ex - name_list = ["python", 1, 2, 3]
"""
name_list = [1, "list", 2, 3]
print(name_list)
print(type(name_list))

name_list[1] = "hello"
print(name_list)

"""
Tuple = storing the different data type value in order, unchangeable in run time, allows duplicate values
values should be assign to a variable in '()'
"""
name_tuple = (1, "tuple", 2, 3)
print(name_tuple)
print(type(name_tuple))

# name_tuple[1] = "hello"
# print(name_tuple)

"""
Dictionaries are the key and value pairs which are written with curly brackets
"""
employeeData = {
    "name": "kumar",
    "number": 12345,
    "DOB": 1996
}
print(employeeData)
print(type(employeeData))
print(employeeData["name"])
