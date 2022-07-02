import search
import testChange


while True:
      
    print("1. Mencari Data Router CSR1000")
    print("2. memembuat Loopback Data Router CSR1000 ")
    print("3. Keluar")
    Pilihan = int(input("Masukan Pilihan : "))
    if Pilihan == 1:
        search.testFilter()
    elif Pilihan == 2:
        testChange.netconfChange()
    elif Pilihan == 3:
        break 