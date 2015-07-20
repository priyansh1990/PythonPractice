__author__ = 'Pri'

import time
import webbrowser
import twilio

print "Version " + (twilio.__version__)
total_break = 3
break_count = 0

print("This program was started on" + time.ctime())


while (break_count < total_break):
    time.sleep(15)
    break_count += 1
    print(break_count)
    webbrowser.open("http://www.google.com")
