arr=[42,147]
for n in arr:
    div=[]
    for i in range(1,n+1):
        if n%i==0:
            div.append(i)
    print("Divisors for "+str(n)+" are:",end=" ")
    for i in div:
        print(i,end=" ")
    print("\nSum of Divisors are: ",end=" ")
    print(sum(div))