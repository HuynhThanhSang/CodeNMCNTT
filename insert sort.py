#thuat toan sap xep
m=[1,4,6,3,8,2,7]
def chen(ds,x,k):
    i=k-1
    while(ds[i]>x) and (i>=0):
        ds[i+1]=ds[i]
        i=i-1
    ds[i+1]=x
for j in range(1,len(m),1):
    chen(m,m[j],j)
print(m)
