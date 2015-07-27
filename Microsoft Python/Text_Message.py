# from babel.dates import format_datetime
# from babel.numbers import format_currency
# import datetime
#
# area = 0
# height = 9
# width = 20
#
# area = width * height / 2
#
# print("The area of triangle is %03d" % area)
#
# print("I Have {0:d}   cats".format(6))
# print("I Have {0:3d}  cats".format(6))
# print("I Have {0:03d} cats".format(6))
# print("I Have {0:f}   cats".format(6))
# print("I Have {0:.2f} cats".format(6))
#
# print("Here are three numbers {0:d} "
# "The second is {1:d} and {2:d}".format(7, 8, 9))
#
# currentDate = (datetime.date.today())
# print(currentDate)
# print(currentDate.strftime('%d %B %y'))
# print(currentDate.strftime('%d %b %y'))
# print(currentDate.strftime('%A %d %B %y'))
#
# currentTime=datetime.datetime.now()
#
country = raw_input("Which country are you from").upper()
#
# if(country=="USA"):
# print("Hello")
# elif(country=="GERMANY"):
#     print("Gluten")
# elif(country=="FRANCE"):
#     print("Bonjour")
# else:
#     print("Sorry")
#
# wonLottery = True
# bigWin = True
#
# if (wonLottery and bigWin):
#     print("Big Win")

pet = "MOOSE"
freshCofee = True

if country == "CANADA" and pet == "MOOSE" \
        or pet == "BEAVER":
    if freshCofee:
        print("Go Buy some Coffee")
        print("Do you play hockey Too")