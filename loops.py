# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)
# print(11)


# for i in range(11):
#     print(i)

# for loop and while loop

#for loop with custom start and stop
# for num in range(1, 6):
#     print(num)

# range with step
# for i in range(1, 10, 2):
#     print(i)

# for i in range(10, 0, -1):
#     print(i)

# looping through a string
# for ch in "python":
#     print(ch)

#While loop
#while condition:
    # code block

# count = 0
# while count < 5:
#     print(count)
#     count += 1     # count += 1 means count = count + 1

# num = 10
# while num > 1:
#     print(num)
#     num-=1

# #infinite loop #
# while True:
#     print("This loop never ends")

#use break statement to come out of an infinite loop

# count = 0
# while True:
#     print("Looping...", count)
#     count += 1
#     if count == 10:
#         break

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

#continue
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

#pass - Do nothing(placeholder)
# for  i in range(5):
#     if i == 3:
#         pass
#     print(i)


#Nested Loops
# for i in range(3): # 0,1, 2
#     for j in range(2): # 0, 1
#         print(i, j)


# for i in range(3): #0 1 2
#     for j in range(2): # 0 1
#         if j == 1:
#             break
#         print(f"{i}, {j}")

#     print("inner finished for i=", i)

    # [ # i for loop
    #   0  [0 1] ===> j for loop 0 0, 0 1
    #   1  [0 1]  ===> j for loop1 0,  1 1
    #    2 [0 1] #  ===> j for loop 2 0, 2, 1
    # ]
stop = False
for i in range(10):
     for j in range(10):
        if i * j == 12:
             print("Found pair", i,j)
             stop = True
             break
        if stop:
            break


    