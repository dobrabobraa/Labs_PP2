import re 


with open("C:/Users/Диас/Documents/Labs/labs_PP2/Lab5/row.txt",'r') as file:
    data = file.read()


print("Task 1")
matches = re.findall("a.*b", data)
print(matches)

print("Task 2")
matches = re.findall("a.*bb+|abbb+", data)
print(matches)

print('Task 3')
matches = re.findall("[a-z]_+[a-z]+", data)
print(matches)

print('Task 4')
matches = re.findall(r"[A-Z][a-z]+", data)
print(matches)

print('Task 5')
matches = re.findall(r"a+.b", data)
print(matches)

print("Task 6")
matches=re.sub(r"[., ]",':',data)
print(matches)

print("Task 7")
matches=re.sub(r"_",'',data)
print(matches)