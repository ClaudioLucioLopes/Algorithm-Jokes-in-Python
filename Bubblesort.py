#Just a Joke with bubblesort
#This has a complexity analysis of O(n^2), more exactly: 7n^2-7n
v=[45,39,355,9898,3,9]
n=len(v)
for i,itemi in enumerate(v[:-1]):
    for j,itemj in enumerate(v[:-1-i]):
        print(i,j)
        if v[j]>v[j+1]:
            temp=v[j]
            v[j]=v[j+1]
            v[j+1]=temp
print(v)
