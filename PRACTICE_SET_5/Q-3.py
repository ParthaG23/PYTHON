dict={}
n=int(input("How many items dictionary you are created:"))
for i in range (1,n+1):
    dict.update({input("enter the key:\t"):input ("enter the value:\t")})
print(f"your given dictionary is \n{dict}")    