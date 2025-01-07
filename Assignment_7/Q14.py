str="characters"
strrev=""
n=len(str)//2
for i in str[:n]:
    strrev=i+strrev
print(strrev)
rest=str[n:]
strnew=strrev+rest
print(strnew)

