num=int(input("Enter any Integer:"))
n=int((num/2)+1)
if (num==0 or num==1):
    print("Prime Number is not defined for 0 and 1")
else:
    for i in range(2,n):
        if num%i==0:
            print(num,"is not Prime number")
            break
        else:
            print(num,"is Prime number")
            break

