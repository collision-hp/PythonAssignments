n=int(input("Emter an integer"))
for i in range(2,n):
    if n%i==0:
        print("Non-Prime")
        break
else:
    print("Prime")