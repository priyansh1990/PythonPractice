# largest = None
# smallest= None
#
# while True:
#     inp = raw_input("Enter the number: ")
#     break
# if inp == "done":
#
#     try:
#         num = float(inp)
#     except:
#         print "Invalid Input"
#
#     if smallest is None:
#         smallest=num;
#
#     if num>largest:
#          num=largest
#     elif num<smallest:
#         smallest=num
#
#
# friends = ['Joseph', 'Glenn', 'Sally']
# for friend in friends :
#     print 'Happy New Year:',  friend
# print 'Done!'
#
# zork = 0
# for thing in [9, 41, 12, 3, 74, 15] :
#     zork = zork + thing
# print 'After', zork
#
# x = 'From marquard@uct.ac.za'
#
# print x[14:17]
#
# print ('banana\n')*7
#
# data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# pos = data.find('.')
# print data[pos:pos+3]
#
# x = range(5)
# print(x)
#
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print (c)
#
# text = "X-DSPAM-Confidence:    0.8475";
# number = text.find(':')
# n = text[number + 1:].strip()
# print float(n)

import SimpleGUICS2Pygame.simpleguics2pygame

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console



# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here

    # remove this when you add your code
    pass


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game

    # remove this when you add your code
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game

    pass

def input_guess(guess):
    # main game logic goes here

    # remove this when you add your code
    pass


# create frame


# register event handlers for control elements and start frame


# call new_game
new_game()


# always remember to check your completed program against the grading rubric
