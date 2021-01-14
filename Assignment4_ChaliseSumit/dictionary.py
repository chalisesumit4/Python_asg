gradeCounts = {"A":8, "D":3, "B":15, "F":2, "C":6}

print("a")
print("___")
print(gradeCounts.keys())
print("--------------")
print("b")
print("___")
print(gradeCounts.values())
print("--------------")
print("c")
print("___")
print(gradeCounts.items())
print("--------------")
print("d")
print("___")
print("Sorted dictionary: ")
sorted_dict = sorted(gradeCounts.items())
print(sorted_dict)
print("--------------")
print("e")
print("___")
sum = 0
for key in gradeCounts:
    sum += gradeCounts[key]
print("Average: ", sum/len(gradeCounts))
print("--------------")
print("f")
print("---")

emp_st = ""
for key,value in sorted_dict:
    emp_str = ""
    for i in range(0,value):
        emp_str = emp_str + "*"
    print(key,":", emp_str)

print("End of program")
