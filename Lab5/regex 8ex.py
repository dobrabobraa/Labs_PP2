import re 


with open("C:/Users/Диас/Documents/Labs/labs_PP2/Lab5/row.txt",'r') as f:
    data = f.read()
    
print("Task 8")

print(re.findall(r"[A-Z][^A-Z]*", data))