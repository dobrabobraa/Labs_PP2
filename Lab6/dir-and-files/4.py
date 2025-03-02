import os
import string

with open("C:/Users/Диас/Documents/Labs/labs_PP2/Lab6/examples/text.txt") as f:
    data = f.read()  

print(len(list(data.split("\n"))))
f.close()