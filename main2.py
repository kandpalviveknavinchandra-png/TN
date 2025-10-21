# print("Gugu Gaga")

#type conversion

#name = input("Yo, Enter your name here!* :")

#age = int(input("Humph... age also! :"))

#ascii values ex: Ascii value of A is 65.
#print(ord("A"))
#not operation : reverses the boolean output
#print(not 1 == 1)
#print(True and bool(0))

#Brainrot = int (input("How many brainrot Reels today? :"))

#if Brainrot < 214:
    #print("You are no longer Tuff...")

#elif Brainrot < 344:
    #print("Ahh... Your edging streak has been dulled!")

#else:
    #print("You still TUFF my BOI!")

#QnA2
#Question = input("Enter Yo Name :")

#in1 = int(input("a :"))
#in2 = int(input("b :"))

#if in1 > in2:
    #print("The one with most AURA is in1!")

#else:
    #print("Unfortunately in2 has done more gooning...")

#QnA3
#Input = int(input("Enter the zesty number here :"))

#if Input %2 == 0:
   # print("The zestiness of the number is zesting(even)")

#else:
#    print("No zesty = no aura, meh...(odd)")

#if-elif ladder
#skip

"""

for loop
in range - start stop steps - start and steps are set as default as 0,1 if not mentioned in range 
a = range(5,51,5)
for i in a:
print(i)

"""

#table
# n = int(input("Which number's table? :"))

#for i in range(n,(n*10)+1,n):
    #print(i) 

#break continue else(if break runs else won't run and vice versa)
#for i in range(1,23):
    #if i == 12:
        #continue
    #print(i)

#break else relation
# for i in range(5,16):
#     if i == 13:
#         print("break break")
#         break
#     print(i)

# else:
#     print("no break break ")

#example1
# n = int(input("Enter yo numb here:"))

# for i in range(n):
#     print("YLIA is not a ROMCOM!")

#example2
# n = int(input("enter :"))

# if n < 1:
#     print("Aalu")
    
# for i in range(1,n+1):
#     print(i)

#4
# N = int(input("number :"))

# for i in range(1,11):
#     print(f"{N}*{i} = {N*i}")    

#5

# n = int(input("inp:"))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print(f" The sum is {sum}")
 
#6

# n = int(input("inp:"))
# fact = 1
# for i in range(1,n*1):
#      fact = fact * i
# print(f" The sum is {fact}")

#practice
# n = int(input("x:"))
# print(range(1,n*1))

#7

# n = int(input("which numb you puttin? :"))
# sum = 0
# for i in range(1,n):
#     if n%i == 0:
#         sum = sum + i

# if sum == n:
#     print("perfect")
# else:
#     print("aho!")

#prime or ksi
 
# n = int(input("enter yo num:"))

# count = 0

# for i in range(1,n+1):
#     if n%i == 0:
#         count = count + 1

# if count == 2:
#     print("ayo thats the OG prime!")

# else:
#     print("from the screen to....")

#reverse string + pallindrom
# string concetination = a+b 
# a = "Taumad"
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]

# if b == a:
#     print("palli")
# else:
#     print("ille!")

#string methods intro
# a = "ly78&&*86fr5*(&)P)__dne123re3"

# char = 0
# dig = 0
# schar = 0

# for i in a:
#     if i.isdigit():
#         dig += 1
#     elif i.isalpha():
#         char += 1
#     else:
#         schar += 1

# print(f"your digs are {dig}\nyor alphas are {char}\nyo special chars are {schar}")

#while loop
# a = 1

# while a<=30:
#     print(a)
#     a = a+1

#imp for while loop
#generate the inputted num in a new column/line

# n = int(input("enter the numb :"))

# while n>0:
#     print(n%10)
#     n = n//10
    
#reverse using while

# n = int(input("enter the numb :"))

# rev = 0 

# while n > 0:
#     rev = rev * 10 + n % 10
#     n = n//10

# print(rev)


#palli with while
# n = int(input("enter the numb :"))
# copy = n
# rev = 0 
#### reason to not use "n" further cause after running the while loop the original value of n has come down to zero which made the loop break
# while n > 0:
#     rev = rev * 10 + n % 10
#     n = n//10

# if rev == copy:
#     print("its a palli")
# else:
#     print("nalli!")

## game with while + intro of libraries

# import random 

# num = random.randint(1,100)

# tries = 0

# while True:
#     guess = int(input("guess the number :"))

#     if num == guess:
#         tries += 1
#         print(f"W, you did this in {tries} tries!")
#         break

#     elif num < guess:
#         print("down")
#         tries += 1

#     elif num > guess:
#         print("up")
#         tries += 1
    
#     else:
#         tries += 1
#         print("L")

##functions intro
# def add(a, b):
#     return a + b
# print(add(3, 6))

# def palli(st):
#     rev = ""
#     for i in range(len(st)-1,-1,-1):
#         rev = rev + st[i]

#     if rev == st:
#         print("palli")
#     else:
#         print("nalli")

# palli("papap")
# palli("sao")


#### revision:
# a = input("enter : ")
# b = "" 

# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]
# if b == a:
#     print("palli")
# else:
#     print("nalli")

## intro of list

# a = [1,2,3,4,5]

# for i in range(len(a)):
#     print(i)

## positive negative in list

# b = [1,2,-2,-3,4,-5,6,7,-8]
# print("the positive numbers are :")
# for i in b:
#     if i >= 0:
#         print(i)

# print("and the negative numbers are :")
# for i in b:
#     if i < 0:
#          print(i) 

##mean value

# c = [1,2,2,3,3,4,4,5,5,5]

# sum = 0

# for i in c:
#     sum = sum + i

# print(sum/len(c))

##greatest no. and its index

# l = [12,35,67,89,11,2]

# largest = l[0]
# index = 0

# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
#         index = i

# print(f"your largest number is {largest} and its index is {index}")

##second largest also:

# a = [2,3,4,5,6,7]

# larg = a[0]
# slarg = a[0]

# for i in a:
#     if i > larg:
#         slarg = larg
#         larg = i
#     elif slarg < i:
#         slarg = i

# print(slarg, larg)

## sorted unsorted

# l = [1,2,3,4,5]

# for i in range(len(l)-1):
#     if l[i] < l[i+1]:
#         continue
#     else:
#         print("unsorted list!")
#         break
# else:
#     print("sorted list")

## sorted unsorted by using a function:
# l = [4,5,7,9,10]  # ya koi bhi list

# if l == sorted(l):
#     print("ascending sorted")
# elif l == sorted(l, reverse=True):
#     print("descending sorted")
# else:
#     print("unsorted")

##Tuples 

# unpacking:
# a,b,c,d = (1,2,3,4)
# a = (1) 
# ab = (1,)

##sets
##compund_operation :
# a = {1,2,3,4}
# b = {3,4,5,6}
# print(a-b)
# b -= a #it will reverse the process 
# print(b)

## Dictionary:
# deepcopy shallow copy
"""deepcopy : variable 'a' contains some value and we have transferred its values to 'b' variable but when we make some changes in 'b' then the same changes will happen in 'a'

shallowcopy : its a counterpart of deepcopy cause as when we are transferring a variable's value in another at that moment we will use .copy() method which will provide the copied values of main variable to other! """

# a = [1,2,3]             # a = [1,2,3]
# b = a.copy()            # b = a
# b[0] = 400              # b[0] = 900
# print(a)                # print(a)

##exception handling

# raise :

# a = int(input("age : "))

# try:

#     if a < 10 or a > 18:
#         raise ValueError("Age must be between 10 and 18!")
#     else:
#         print("welcome!")

# except Exception as err:
#     print("There has been an error occured that the {err}")

# print("Welcome")

##File Handling

# p = open('main.py')
# print(p.read())

##write
# r = open("rudy.txt","w")
# r.write("Sim card changing machine activate!")
# r.close()
##append
# r = open("rudy.txt","a")
# r.write("Gali gali sim sim!")
# r.close()

##OOPs

##CONSTRUCTOR:

# class Carrier_Player:
#     def __init__(self, goals, assists, matches_played):
#         self.goals = goals
#         self.assists = assists
#         self.matches_played = matches_played

#     def show(self):
#         print(f"This player has contributed {self.goals + self.assists} G/A in {self.matches_played} matches!")

#         if self.goals + self.assists > self.matches_played:
#             print("THE GOAT")

#         else:
#             print("Better Luck Next Time!")

# Lionel_Andreas_Messi = Carrier_Player(870, 390, 1113)
# Cristiano_Ronaldo = Carrier_Player(940, 260, 1260)

# Lionel_Andreas_Messi.show()
# Cristiano_Ronaldo.show()

def info(**kwargs):
    print("yo info is:  ")
    for i in kwargs:
        print(f"{i} : {kwargs[i]}")

name = input("Enter your name : ")

info(name = "Rudeus Greyrat", age = 24, destiny = "Protect My Family.")

print(f"Your name has been successfully registered as {name}")
