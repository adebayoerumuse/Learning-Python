# The goal of this exercise is to help you practice the fundamental rules of Python and learn how 
# to identify common errors. Read each task carefully, write your code, and predict the output or error before you run it.
# Part 1: Syntax & Indentation

# Task 1: The First print() Write a single line of code that prints the message "Hello, Python!" to the console.
print "Hello, Python!" #incorrect
print("hello, Python!") # correct way

# Task 2: Correcting Indentation. The following code has an IndentationError. Correct the indentation so that 
# the program runs successfully. What does it print?

is_it_true = True
if is_it_true:
print()
print()
print("The condition is true.")
print("This line is also part of the if block.")

is_it_true = True
if is_it_true:
    print("The condition is true.")
    print("This line is also part of the if block.")


# Task 3: Case Sensitivity The following code is intended to print the value of the variable name. 
# Identify and correct the error. Why did it happen?

Name = "Alice"
print(Name)

# Task 4: Using Comments Add a single-line comment to explain what the first line of code does. 
# Then, use a multi-line comment to describe what the entire code block does.

age = 25
if age > 18:
    print("You are an adult.")
# The first lines gives the age of a person to be 25 years of age  
""""
While the first line gives the age of a person to be 25
The second line gives a conditon that about a person's age greater than 18
The last line of code states that any person above the age of 18 is considered an adult
"""
# Part 2: Semantics & Variable Assignment

# Task 5: Variable Types Write a Python script that defines a variable data. 
marital_status_str = "divorced"

# First, assign it an integer value and print its type. Then, on the next line, reassign 
# it to a string value and print its new type. What does this demonstrate about Python's variables?
total = 200
total_str = str (total)
print (total_str)
type (total_str)

# Task 6: The NameError The following code will produce an error. Explain why this error occurs and how to fix it.

greeting = message + "!"
message = "Hello"
print(greeting)

# Task 7: Predicting the Output Without running the code, predict what the final value of score will be. 
# Explain your reasoning.

score = 100
score = score + 50
print(score)
score = "Excellent"
print(score)

greeting = "Hello, World" + "!"
print(greeting)