str='aabbbccccddddd'
n=len(str)
freq=5
for i in range(0,n):
    count=0
    char=str[i]
    while i<n and str[i]==char:
        count+=1
        i+=1
    if count==freq:
        print(char*freq)
        break
else:
    print("Not found")