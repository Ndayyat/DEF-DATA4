#devs_money = 100
#dev_can_play_smash = True
#if devs_money > 10 and dev_can_play_smash:
 #   print("Dev enters a smash tournament!")
#elif devs_money < 10 and dev_can_play_smash:
 #   print("Dev is too poor to enter")
#else:
 #   print("Dev just can't play smash")

#mark = input("give me your mamrk?")
#mark1=float(mark)

# if mark1 >= 85:
#    print("Distinction")
# elif mark1 >= 65 :
#    print("Pass")
# else:
#    print("Fail")

# count = 0

# while count < 5:
#     name = str(input("What is your name?"))
#     print(name, "is awesome!")
#     count += 1

# count = 0
# friends = []
# while count < 5:
#     name = input("enter your name: ")
#     friends.append(name)
#     count += 1 
# for friend in friends:
#     print(friend, "is awesome")
# \
# # for i in range(5, 11):
# #     print(i, name)

# for i in range(10, 21, 2):
#     print(i)

# Score = 500
# while Score > 100 or Score < 0:
#     Score = int(input("enter a score: "))
#     if Score > 100 or Score < 0:
#         print("Not a valid score, try again")
# if Score >= 85:
#     print("Distinction")
# elif Score >= 65:
#     print("Pass")
# else:
#     print("Fail")

# for i in range(5, 11):
# #     print(i, name)


# # Temp = []
# for i in range(0, 101,10):

    
#     Tempc.append(i)
#     fconvert = (i*9/5) + 32
#     Tempf.append(fconvert)
# print (Tempc,, '|' , Tempf )

#  Write a Python program that accepts a word from the user
# and reverse it


# userWord = input("wrdin: ")  # accept a word from the user

# Q: do we know how many letters?  NO
# Q: is there way of finding out how many letters were entered?  len()

# letterCount = len(userWord)

# Q: Now I know how many letters. Can I loop? Which loop?

# revWord = ""
# for i in range(letterCount-1,-1,-1):
#     revWord = revWord + userWord[i]

# print(revWord)


#revWord = userWord[::-1]

# def stock_stuff(inputvar):
# 2	    productcodelen = len(inputvar)
# 3	    return productcodelen
# 4	
# 5	
# 6	
# 7	
# 8	product_code = input("What do you want to buy?")
# 9	
# 10	returnvar = stock_stuff(product_code)
# 11	
# 12	print("Your product code was", returnvar,"chars long")



# def stock_stuff(inputvar,inputvar2):
#     productcodelen = len(inputvar)
#     if int(inputvar2)%2 == 0:
#         quant = "it is even"
#     else:
#         quant = "it is odd"
#     return (productcodelen,quant)



# product_code = input("What do you want to buy?")
# quantity = input("How Many")

# returnvar = stock_stuff(product_code,quantity)

# print(returnvar)




# temp = []
# t =0
# for i in range(0, 101,10):
#     temp.append(i)

# while t in temp: 
#     tempc = t
#     tempf = (t*9/5) + 32
#     print (tempc, "°C ", '|' , tempf, "°F" )
#     t += 10
#     if t > 100: 
#         break








# def add_calc(number1, number2):
#     answer = number1 + number2
#     return answer

# added_number = add_calc(5,5)
# print(added_number + 20)


def results(int_homework, int_assessment, int_finalexam):
    answer = (int(int_homework) + int(int_assessment) + int(int_finalexam)) /175 *100 
    return answer


name = str(input("enter your name"))
homework = 26
while homework > 25 :
   homework = float(input("enter your homewrk score"))
   if homework > 25 or homework < 0:
       print("not avlid score, try again")

assessment = 51
while assessment > 50 :
    assessment = float(input("enter your assessment score"))
    if assessment > 50 or assessment < 0:
      print("invalid score, try again")

finalexam = 101
while finalexam > 100 :
    finalexam = float(input("enter your final exam score"))
    if finalexam > 100 or finalexam < 0:
      print("invalid score, try again")

grade = results(homework, assessment, finalexam)
print(name, "got", grade)

