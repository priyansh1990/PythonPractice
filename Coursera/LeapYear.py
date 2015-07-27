# __author__ = 'Pri'
#
# # Conditionals Examples
#
# # Return True if year is a leap year, false otherwise
# def is_leap_year(year):
# if (year % 400) == 0:
# return True
# elif (year % 100) == 0:
#         return False
#     elif (year % 4) == 0:
#         return True
#     else:
#         return False
#
#
# year = 2012
# leap_year = is_leap_year(year)
#
# if leap_year:
#     print year, "is a leap year"
# else:
#     print year, "is not a leap year"
#

# import random
#
#
# def random_Dice():
#     die1 = random.randrange(1, 7)
#     die2 = random.randrange(1, 7)
#
#     return die1 + die2
#
#
# print("Sum of two random dice", random_Dice())
# print("Sum of two random dice", random_Dice())
# print("Sum of two random dice", random_Dice())

# a = 10
# b = 2
# x = 4
# print 5 + 2

# n = 123
#
#
#
# print ((n - n % 10) / 10) % 10
# print (n - n % 10) / 10
# print ((n - n % 10) % 100) / 10
# import random
#
# print random.randint(0, 10)
# print random.randrange(0, 10)

import math


def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale

project_to_distance(2, 7, 4)