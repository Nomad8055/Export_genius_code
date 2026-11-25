x=[1,2,3,4,5,11,,22128365,,3,2,3,4,55,777773,44454,5,5,6]
dup=[]
for i in x:
    if x.count(i)>1 and i not in dup:
        dup.append(i)
print(dup)

    
