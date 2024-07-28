l1=[]
n=int(input("Enter how meny item store in the list : "))
for i in range(1,n+1):
    l1.append(int(input(f"Enter the {i}s element: ")))
    i+=1
print(f"your given list = {l1}")
sum=0
for i in l1:
    sum+=i
    i+=1
print(f"sum of the given list {sum}")