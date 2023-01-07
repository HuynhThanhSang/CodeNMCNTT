#de qui
def giai_thua (n):
    if n==1:
       return 1
    else:
        return n*giai_thua(n-1)
#goi ham tinh n!
n=int(input("nhap so n can tinh giai thua="))
print(n,"!= ", giai_thua(n))
n=int(input("nhap so phan tu"))


