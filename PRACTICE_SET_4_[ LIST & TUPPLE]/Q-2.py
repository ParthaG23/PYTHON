l1=[]
for i in range(1,6+1):
    l1.append(int(input(f"Enter the {i}s student marks: ")))
    i+=1
print(f"Enter your student marks list in unsorted order {l1}")
l1.sort()
print(f"Enter your student marks list in sorted order {l1}")