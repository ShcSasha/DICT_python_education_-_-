print ("Hello! My name is DICT_Bot")
print ("I was created in 2021")
name = input("Plase, remind me your name:")
print ("What a great name you have,", name)
print ("Let me gess your age. ")
print ("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print ("Your age is " + str(age) + " that's a good time to start programming!")
print ("Now i will prove to you that I can count to any number you want.")
number = int(input())
for i in range(number + 1):
    print(i, '!', sep='')
print ("Let's test your programming knowledge.")
print ("Why do we use methods?")
print ("1. To repeat a statement multiple times.")
print ("2. To decompose a program into several small subroutines.")
print ("3. To determine the execution time of a program.")
print ("4. To interrupt the execution of a program.")
x = 0
while x != 2:
     x = int(input())
     if x == 2:
            print("Completed, have a nice day!")
     else :
       print("Please, try again.")
print("Congratulations, have a nice day!")
