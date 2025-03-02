"""RIGHT ANGLED TRIANGLE ANIMATION WITH PYTHON"""

import random
import time

def animation():
    text = str(input("Enter the text you want to animate: "))
    string = text * len(text)

    for i in range(len(string)):
        print("{:<10} {:>100}".format(string[:i+1], "Made by @CGR"))
        time.sleep(0.10)
        
        
        
        
        

animation()