IB = 25000
ED = 6000
RC = 8000

print("=====MASUKKAN JUMLAH MAKANAN YANG DIPESAN=====")

ikanbakar = int(input("IKAN BAKAR        Rp 25.000,00   : "))
esdoger = int(input("ES DOGER          Rp 6.000,00    : "))
rujakcingur = int(input("RUJAK CINGUR      Rp 8.000,00    : "))

print("=====TOTAL=====")

IB1 = int(IB)*ikanbakar
ED1 = int(ED)*esdoger
RC1 = int(RC)*rujakcingur

print("TOTAL IKAN BAKAR        : Rp ", IB1)
print("TOTAL ES DOGER          : Rp ", ED1)
print("TOTAL RUJAK CINGUR      : Rp ", RC1)
print("Jumlah total biaya yang harus dibayar adalah Rp ", IB1+ED1+RC1)


