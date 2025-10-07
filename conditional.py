# if-Statement

# age = 20
# if age >= 18:
#     print("You are allowed to vote in the election")


# # esle-statement:
# age = 12
# if age >= 18:
#     print("You are allowed to vote in the election")
# else:
#     print("You are a minor")


# elif-statement
#Age Classification

# age = 17

# if age < 13:
#     print("You are child")
# elif age < 18:
#     print("You are a teenager")
# else:
#     print("You are an adult")

# Nested conditional statements
# Number Classification

# number = int(input("Enter a number: "))

# if number > 0:
#     print("The number is positive.")
    
#     if number % 2 == 0:
#         print("It's even.")
#     else:
#         print("it's odd.")
# else:
#     print("the number is zero or negative")


#Leap Year Checker

# year = int(input("Enter a year: "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year ")
#         else:
#             print(f"{year} is NOT a leap year ")
#     else:
#         print(f"{year} is a leap year ")
# else:
#      print(f"{year} is a NOT leap year ")



# #simple calculator
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# operation = input("Choose operation(+,-,*,/)")

# if operation == "+":
#     result = num1 + num2
# elif operation == "-":
#     result = num1 - num2
# elif operation == "*":
#     result = num1 * num2
# elif operation == "/":
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         result = "Error dividing by zero"
# else:
#     result = "Invalid operation"

# print("Result", result)

#Write a program that checks if a nyumber is prime 

# num = int(input("Enter the number"))

# if num <= 1:
#     print("Prime numbers must be greater than 1: ")
# elif num == 2 or num ==3:
#     print(f"{num} is a PRIME number")
# elif num % 2 == 0 or num % 3 == 0:
#     print(f"{num} is NOT a prime number")
# else:
#     print(f"{num} might be a  PRIME number (full check needs loops)")


#create a program that checks username plus password login 

username = True 
# password = False

# if username and password:
#     print("Login successful")
# else:
#     print("Invalid login credentials")

# correct_username = "admin"
# correct_password = "1234"

# username = input("Enter username: ")
# password = input("Enter password: ")

# if username == correct_username and password == correct_password:
#     print("Login successful")
#     if username != correct_username:
#         if password != correct_password:
#             print("Invalid password")
#         print("Invalid username")
# else:
#     print("Invalid login credentials")

# Write tem
# >=90 ----> A
# 80-89 -----> B
# 70 -79 ----> c
# else ---> 

# grade = int(input("Enter the grade: "))
# if grade >= 90:
#     print(grade, "A")
# elif grade >= 80:
#     print(grade, "B")
# elif grade >=70:
#     print(grade, "C")
# else:
#     print(grade, "F")

#REPORT CARD

Mathematics = int(input("Enter mathematics score: "))
English = int(input("Enter English score: "))
Science = int(input("Enter science score: "))
History = int(input("Enter History score: "))
ICT = int(input("Enter ICT score: "))

if Mathematics < 0 or Mathematics > 100:
    print(Mathematics, "Mathematics score is invalid")
else:
    print(Mathematics, "Mathematics Score is valid")
if English < 0 or English > 100:
    print(English, "English score is invalid")
else:
    print(English, "English score is valid")
if History < 0 or History > 100:
    print(History, "Hsitory score is invalid")
else:
    print(History, "HIstory score is valid")
if Science < 0 or Science > 100: 
    print(Science, "Science score is invalid")
else:
    print(Science, "Science score is valid")
if ICT < 0 or ICT > 100:
    print(ICT, "ICT score is invalid")
else:
    print(ICT, "ICT score is valid")

 #Report Card Two 


correct_username = "lucky"
correct_password = "0000"

username = input("Enter username: ")
password = int(input("Enter password: "))

if username == correct_username and password == correct_password:
    print("Login successful")
else:
    print("Invalid login credentials")

Term = str(input("Enter the term: "))
print(Term)

Academic_session = (input("Enter academic session: "))
print(Academic_session)

sex = (input("Enter sex: "))
print(sex)

Attendance = (input("Enter attendace: "))
print(Attendance)

Class = (input("Enter class: "))
print(Class)

Mathematics_1st_CA = int(input("Enter mathematics 1st CA score: "))
English_1st_CA = int(input("Enter English 1st CA score: "))
Science_1st_CA = int(input("Enter Science 1st CA score: "))
History_1st_CA = int(input("Enter History 1st CA score: "))
ICT_1st_CA = int(input("Enter ICT 1st CA score: "))

# Second CA
Mathematics_2nd_CA = int(input("Enter mathematics 2nd CA: "))
English_2nd_CA = int(input("Enter English 2nd CA score: "))
Science_2nd_CA = int(input("Enter Science 2nd CA score: "))
History_2nd_CA = int(input("Enter History 2nd CA score: "))
ICT_2nd_CA = int(input("Enter ICT 2nd CA score: "))

# Exams
Mathematics_Exams = int(input("Enter mathematics exam score: "))
English_Exams = int(input("Enter English exam  score: "))
Science_Exams = int(input("Enter Science exam  score: "))
History_Exams = int(input("Enter History exam  score: "))
ICT_Exams = int(input("Enter ICT exam  score: "))

if Mathematics_1st_CA < 0 or Mathematics_1st_CA > 20:
    print("Invalid Score")
else:
    print("Mathematics 1st CA", Mathematics_1st_CA)
if Mathematics_2nd_CA < 0 or Mathematics_2nd_CA > 20:
    print("Invalid Score")
else:
    print("Mathematics 2nd CA", Mathematics_2nd_CA)
if Mathematics_Exams < 0 or Mathematics_Exams > 60:
    print("Invalid Score")
else:
    print("Mathematics Exam", Mathematics_Exams)


Mathematics_Total = Mathematics_1st_CA + Mathematics_2nd_CA + Mathematics_Exams
if Mathematics_Total > 100:
    print("Mathematics Total is invalid")
else:
    print("Mathematics Total: ", Mathematics_Total)
    if Mathematics_Total >= 70:
        print(Mathematics_Total, "Mathematics Total is A Excellent")
    elif Mathematics_Total >= 60:
        print(Mathematics_Total, "Mathematics Total is B Very Good")
    elif Mathematics_Total >= 50:
        print(Mathematics_Total, "Mathematics Total is C Good")
    elif Mathematics_Total >= 45:
        print(Mathematics_Total, "Mathematics Total is D Fair")
    elif Mathematics_Total >= 40:
        print(Mathematics_Total, "Mathematics Total is E Pass")
    else:
        print(Mathematics_Total, "Mathematics Total is F Fail")

if English_1st_CA < 0 or English_1st_CA > 20:
    print("Invalid Score")
else:
    print("English 1st CA", English_1st_CA)
if English_2nd_CA < 0 or English_2nd_CA > 20:
    print("Invalid Score")
else:
    print("English 2nd CA",English_2nd_CA)
if English_Exams < 0 or English_Exams > 60:
    print("Invalid Score")
else:
    print("English Exam", English_Exams)

English_Total = English_1st_CA + English_2nd_CA + English_Exams
if English_Total > 100:
    print("English Total is invalid")
else:
    print("English Total: ", English_Total)
    if English_Total >= 70:
        print(English_Total, "English Total is A Excellent")
    elif English_Total >= 60:
        print("English Total is B Very Good")
    elif English_Total >= 50:
        print("English Total is C Good")
    elif English_Total >= 45:
        print("English Total is D Fair")
    elif English_Total >= 40:
        print("English Total is E Pass")
    else:
        print("English Total is F Fail")


if Science_1st_CA < 0 or Science_1st_CA > 20:
    print("Invalid Score")
else:
    print("Science 1st CA is", Science_1st_CA)
if Science_2nd_CA < 0 or Science_2nd_CA > 20:
    print("Invalid Score")
else:
    print("Science 2nd is", Science_2nd_CA)
if Science_Exams < 0 or Science_Exams > 60:
    print("Invalid Score")
else:
    print("Science Exam is", Science_Exams)

Science_Total = Science_1st_CA + Science_2nd_CA + Science_Exams
if Science_Total > 100:
    print("Science Total is invalid")
else:
    print("Science Total: ", Science_Total)
    if Science_Total >= 70:
        print(Science_Total, "Science Total is A Excellent")
    elif Science_Total >= 60:
        print(Science_Total, "Science Total is B Very Good")
    elif Science_Total >= 50:
        print(Science_Total, "Science Total is C Good")
    elif Science_Total >= 45:
        print(Science_Total, "Science Total is D Fair")
    elif Science_Total >= 40:
        print(Science_Total, "Science Total is E Pass")
    else:
        print(Science_Total, "Science Total is F Fail")


if History_1st_CA < 0 or History_1st_CA > 20:
    print("Invalid Score")
else:
    print("History 1st CA", History_1st_CA)
if History_2nd_CA < 0 or History_2nd_CA > 20:
    print("Invalid Score")
else:
    print("History 2nd CA", History_2nd_CA)
if History_Exams < 0 or History_Exams > 60:
    print("Invalid Score")
else:
    print("History Exam", History_Exams)

History_Total = History_1st_CA + History_2nd_CA + History_Exams
if History_Total == History_1st_CA + History_2nd_CA + History_Exams:
    print("History Total: ", History_Total)
    if History_Total >= 70:
        print(History_Total, "History Total is A Excellent")
    elif History_Total >= 60:
        print(History_Total, "History Total is B Very Good")
    elif History_Total >= 50:
        print(History_Total, "History Total is C Good")
    elif History_Total >= 45:
        print(History_Total, "History Total is D Fair")
    elif History_Total >= 40:
        print(History_Total, "History Total is E Pass")
    else:
        print(History_Total, "History Total is F Fail")


if ICT_1st_CA < 0 or ICT_1st_CA > 20:
    print("Invalid Score")
else:
    print("ICT 1st CA", ICT_1st_CA)
if ICT_2nd_CA < 0 or ICT_2nd_CA > 20:
    print("Invalid Score")
else:
    print("ICT 2nd CA", ICT_2nd_CA)
if ICT_Exams < 0 or ICT_Exams > 60:
    print("Invalid Score")
else:
    print("ICT Exam", ICT_Exams)

ICT_Total = ICT_1st_CA + ICT_2nd_CA + ICT_Exams
if ICT_Total > 100:
    print("Invalid ICT Total")
else:
    print("ICT Total: ", ICT_Total)
    if ICT_Total >= 70:
        print(ICT_Total, "ICT Total is A Excellent")
    elif ICT_Total >= 60:
        print(ICT_Total, "ICT Total is B Very Good")
    elif ICT_Total >= 50:
        print(ICT_Total, "ICT Total is C Good")
    elif ICT_Total >= 45:
        print(ICT_Total, "ICT Total is D Fair")
    elif ICT_Total >= 40:
        print(ICT_Total, "ICT Total is E Pass")
    else:
        print(ICT_Total, "ICT Total is F Fail")

    Total_Score = Mathematics_Total + English_Total + Science_Total + History_Total + ICT_Total
    if Total_Score > 500:
        print("Invalid Total Score")
    else:
        print("Total Score:", Total_Score)

Average_Score = Total_Score / 5
if Average_Score > 100:
    print("Invalid Average Score")
else:
    if Average_Score >= 70:
        print(Average_Score, "An excellent performance. Keep it up!")
    elif Average_Score >= 60:
        print(Average_Score, "A very good performance. Keep it up")
    elif Average_Score >= 50:
        print(Average_Score, "A good performance. You can do better.")
    elif Average_Score >= 45:
        print(Average_Score, "A fair perfromance. You have to do better.")
    else: 
        print(Average_Score, "You have to believe in yourself and put in more effort")
