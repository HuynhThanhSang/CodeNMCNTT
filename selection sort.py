#thuat toan sap xep lua chon
def luachon(kq):
    n=len(kq)
    for i in range(0,n-1,1):
        nho_nhat=i
        for j in range(i+1,n,1):
            if kq[j]<kq[nho_nhat]:
                nho_nhat=j
        kq[i],kq[nho_nhat]=kq[nho_nhat],kq[i]
    return kq

