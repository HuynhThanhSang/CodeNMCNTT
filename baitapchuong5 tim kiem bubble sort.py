#thuat toan sap xep noi bot
def bubble_sort(kq):
    n=len(kq)
    for i in range(0,n-1,1):
        for j in range(i+1,n,1):
            if kq[i]>kq[j]:
                kq[i],kq[j]=kq[j],kq[i]
    return kq
kq=[]
n=int(input("nhap so phan tu"))
for i in range(0,n):
    a=int(input())
    kq.append(a)
print("chuoi sau khi duoc sap xep la:",bubble_sort(kq))
