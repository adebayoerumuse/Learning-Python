# Variables, Data Types, and Operators

#Variable

Age = 12
print(Age)

name = 'lukcy'
print(name)

# rules in naming variables
fruit = 'mango'
print(fruit)

_number = 1
print(_number)

#Must start with  (a-z), (A-Z) or underscore(_)
# 2boys = 2
#my-first-name = 'Dan' # wrong
my_first_name = 'Dan' 
myFirstName = 'Dan'
MyFirstName = 'Dan'

#print(my-first-name)
print(my_first_name)

# Variable Types
1
# integer(int) ; 4, 6, -5
# float: 5.7, 2.9
# String  = 'Dan', "Dan"
# bool: True or False

# Type Casting and Converion

age_str = '25'
age_int  = int(age_str)
print(age_int)

height = 5.9
height_int = int(height)
print(height_int)

number = 123

number_str = str(number)
print(type(number_str))


# Getting user input
# input()

#user_age = input('Enter your age: ')
#print(f'your age is {user_age}')


# Getting User Input
#input() 

#my_age = input("Enter your age: ")

#print(my_age)


# operators
num1 = 1
num2 = 2
total = num1 + num2
print(total)

# Division(/)
div1 = 10
div2 = 5
total_div = div1 / div2
print(total_div)

# Floor Division(//)
div3 = 10
div4 = 3
total_div2 = div3 // div4
print(total_div2)

# modulus(%)
mod1 = 10
mod2 = 2
result = mod1 % mod2
print(result)

#Exponential(**)
power_result = 2 ** 3 # 8

# Equal to (==)

val1 = 5
val2 = 5
is_equal = (val1 == val2)

# Not Equal to (!=)

#>, < >= <=


# Logical operators
# b#Boolean  = True of False

#1.  and: Returns True only if both conditions are True
is_logged_in = True
has_admin_rights = True

can_access = is_logged_in and has_admin_rights
print(can_access) #True


# 2. or
is_logged_in = True
has_admin_rights = False

can_access = is_logged_in and has_admin_rights
print(can_access) #True

# 3. not:
is_active = True
ouput = not is_active