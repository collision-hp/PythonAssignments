def fstr(str):
    ss=[]
    ss.append(str[0])
    for i in range(1,len(str)):
        if str[i]==str[i-1]:
            ss.append("*")
        else:
            ss.append(str[i])
    print(''.join(ss))
str=input("Enter a string")
fstr(str)

