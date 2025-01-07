sentence="count the number of occurrences"
ll=sentence.split(" ")
print(ll)
j=1
for i in ll:
    for j in ll:
        if len(i)>len(j):
            max=i
        else:
            max=j 
            break
print(max)


