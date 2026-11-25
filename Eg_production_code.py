z=[1,2,3,4,5,1,222,3,2,35555555597,4,5,3,4,5,5,6]
dup=[]
for i in z:
    if z.count(i)>1 and i not in dup:
        dup.append(i)
print(dup)

    
