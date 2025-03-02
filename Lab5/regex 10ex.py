import re 


with open ("C:/Users/Диас/Documents/Labs/labs_PP2/Lab5/row.txt",'r') as f:
    data = f.read()

    print("Task 10")
matches=re.sub(r"[A-Z]",'_',data)
print(matches)