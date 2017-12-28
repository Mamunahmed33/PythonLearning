list1 = {"Mamun", "Jobayer", "Samrat"}
list2 = {"Khandaker", "Ahmed", "Samim"}

names = zip(list1, list2)  # Works on unique names

for a, b in names:
    print(a,b)