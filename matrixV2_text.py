"""MATRIX ANIMATION USING PYTHON: V2 (Text effects)"""

import random
import time

# characters = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 0 ! @ # $ % ^ & * ( ) _ + - = [ ] { } | ; : ' \" , . < > ? / ` ~ "
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;:'\",.<>?/`~"
array = list(characters)

def matrixV2_text():
    while True:
        print(" Made by CGR ".join(random.choices(array, k=(len(characters)))))
        time.sleep(0.05)

matrixV2_text()