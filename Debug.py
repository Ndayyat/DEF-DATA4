
import pdb

pdb.set_trace()


def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
            return True




# def product(n):
#     total = 1
#     for n in n:
#         total *= n
#     return total

# print(product([4,4,5]))


# user_funds = 10.31
# item_price = int(input("Burger price:"))

# if item_price < user_funds:
#     print("You have enough money!")
# if item_price == user_funds:
#     print("You have the precise amount of money")
# if item_price < user_funds:
#     print("Sorry you don't have enough money")




# item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
# n = 0

# while n < 5:
#     n =+ 1
#     for i in item_list:
#         print (i)
#         n =+ 1
#         # if n == 5:
#         #     break
#     print(item_list[4])





# n = 0

# while n < 5:
#     for i in item_list:
#         print(item_list[i])

# print item_list[5]

# item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]

# n = 0
# while n < 5:
#     n += 1
#     for i in item_list:
#         print(i)

# print (item_list[4])