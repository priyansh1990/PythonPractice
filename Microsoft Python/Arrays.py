# import turtle
#
# counter = 0
#
# while counter != 4:
#     turtle.forward(100)
#     turtle.right(90)
#     counter+=1
# print("Congrats")


guest=['Susan', 'Cris','Bill','Satya','Bill']
guest.append("Colin")
# print(guest[-1])
#
# # guest[3]='Soanl'
#
# guest.remove('Bill')
# del guest[0]
#
# print(guest.index('Bill'))

numberOfValue=len(guest)

guest.sort()

for steps in range(numberOfValue):
    print(guest[steps])

print'Hi'*5

hrs = raw_input("Enter Hours:")
hrsRate = raw_input("Enter Hours Per Rate:")
hrs = float(hrs)
hrsRate = float(hrsRate)
totalMoney = hrs*hrsRate
print totalMoney
__author__ = 'Pri'
