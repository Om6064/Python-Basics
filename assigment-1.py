# info = """my name is patel aryan manojbhai i am 19 years old"""

# print(info)

# 2 ND
# p = float(input("Enter Principal Amout : "))
# r = float(input("Enter Rate Of Intrest : "))
# n = float(input("Enter Number Of Years : "))

# si = (p*r*n)/100
# print(si)

# 3 RD
# p1_age = int(input("Enter person 1 age : "))
# p1_name = input("Enter person 1 name : ")

# p2_age = int(input("Enter person 2 age : "))
# p2_name = input("Enter person 2 name : ")

# if(p1_age >= 18) :
#     print(p1_name, "is Audalt : ")
# else :
#     print(p1_name, "is Not Audalt : ")

# if(p2_age >= 18) :
#     print(p2_name, "is Audalt : ")
# else :
#     print(p2_name, "is Not Audalt : ")

# 4 TH
# known_city = ["surat","ahabdabad","mumbai","delhi"]

# name  = input("Enter a Person Name : ")
# city = input("Enter a Person City : ")

# if (city in known_city):
#     print(name, "is from City : ")
# else :
#     print(name,"Is From Village : ")

# 5 TH
# num = int(input("Enter Num For Mul : "))

# for i in range(1,11):
#     print(num,"*",i,"=",num*i)


# 6 TH
# num = int(input("Enter Num : "))
# if(num%2 == 0) :
#     print("IT is Even : ")
# else :
#     print("it is odd")

# 7 TH
# num1 = int(input("Enter Num1 : "))
# num2 = int(input("Enter Num2 : "))
# num3 = int(input("Enter Num3 : "))

# if(num1 < num2 and num1 < num3):
#     print(num1 , " is smallest")
# elif(num2 < num1 and num2 < num3):
#     print(num2 , " is smallest")
# else:
#     print(num3 , " is smallest")

# 8 TH
# num1 = int(input("Enter Num1 : "))
# num2 = int(input("Enter Num2 : "))
# num3 = int(input("Enter Num3 : "))

# if(num1 < num2 < num3 or num3 < num2 < num1):
#     print(num2 , " is Midal")
# elif(num2 < num1 < num3 or num3 < num1 < num2):
#     print(num1 , " is Midal")
# else :
#     print(num3 , " is Midal")

# 10 TH
# input =  "welcome to the world of AI"
# re_input = input[::-1]
# print(re_input)

# 11 TH
# input = "Chocolate cookie."
# word  = input.split()[-1]
# re_input = input.replace(word,"Vanila")
# print(re_input)

# 12 TH
# SKIP

# 13 TH AND 14TH
# para = """"AI, or artificial intelligence, is revolutionizing various industries.
#  AI technologies are becoming increasingly important in today's world.
#  The future of AI looks promising."""

# c = para.count("AI")
# print(c)

# re_para = para.replace("AI","IOT")
# print(re_para)

# 14 TH
# s1 = "welcome to the world of AI"
# word = s1.split()

# result = ""

# for i in word:
#     result += i[0].upper()

# print(result)

# 15 TH
# s1 = "welcome to the world of AI"
# s = s1.split()
# print(s)

# 16 TH
# s1 = "welcome to the world of AI"

# at = s1.find("AI")
# print(at)

# 17 TH
s1 = "welcome to the world of AI"
result = ""

for i in range(len(s1)):
    if(i % 2 ==0):
        result += s1[i]
print(result)






