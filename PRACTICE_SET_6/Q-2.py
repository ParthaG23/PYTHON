s1=int(input("enter your first subject marks:"))
s2=int(input("enter your second subject marks:"))
s3=int(input("enter your third subject marks:"))
if (s1<40 or s2<40 or s3<40):
    print("you are fail")
elif((s1+s2+s3)/3)<40:
    print("you are fail")
else:
    print("you are passed")    
