"""MATRIX ANIMATION USING PYTHON: V2 (Text effects)"""
"""
 * Copyright (C) 2025 CGRofficialcode
 *
 * This code is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * Thiscode is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this code.  If not, see <https://www.gnu.org/licenses/>.
 *//
 """
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
