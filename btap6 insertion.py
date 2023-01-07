#baitap6 chuong7
#thuat toan sap xep
m=[12,13,11,10,10,9,8,7,6,5]
def chen(ds,x,k):
    i=k-1
    while(ds[i]>x) and (i>=0):
        ds[i+1]=ds[i]
        i=i-1
    ds[i+1]=x
for j in range(1,len(m),1):
    chen(m,m[j],j)
print(m)
