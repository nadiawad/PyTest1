'''
This is a mulit-line comment
'''
# And this is a one-line comment

import webbrowser
import time
print("Hello World!               "+time.ctime())

total_breaks = 3
count = 1
while (count <= total_breaks) :
    time.sleep(5)
    #webbrowser.open("https://www.google.com")
    print("Have a break!              "+time.ctime())
    count+=1

print("Done for today! Goodbye    "+time.ctime())

