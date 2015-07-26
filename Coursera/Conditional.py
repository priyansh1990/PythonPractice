__author__ = 'Pri'


def greet(friend, Money):
    print"Bigger Money Before", Money
    if friend and (Money > 20):
        print "Hi"
        Money -= 20
    elif friend:
        print("Hello")
    else:
        print ("Ha Ha")
        Money += 10
    print"Bigger Money After", Money
    return Money


money = 15
money = greet(True, money)
print "Money Call :", money
print ""

money = greet(False, money)
print "Money Call :", money
print ""

money = greet(True, money)
print "Money Call :", money
print ""
