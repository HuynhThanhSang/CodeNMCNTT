#thuat toan sap xep noi bot
def bubble_sort(kq):
    for i in range(0,n-1,1):
        for j in range(i+1,n,1):
            if kq[i]>kq[i+1]:
                x=kq[j]
                kq[j+1]=kq[j]
                kq[j]=x
    return kq
