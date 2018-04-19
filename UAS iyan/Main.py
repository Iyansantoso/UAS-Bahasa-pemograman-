import texttable as tt
import getpass
from perhitungan.penilaian import nilai_mahasiswa
from perhitungan.perhitungan import pembayaran
from perhitungan.kalkulator import menu_cal


def menu():
    print("\n\t======================================")
    print("\tKAMPUS PELITA BANGSA")
    print("\t========================================")
    print("\n\t---pilihan---")
    print("\t1. nilai mahasiswa")
    print("\t2. pembayaran mahasiswa")
    print("\t3. kalkulator")

    pilih=input("\n\tsilahkan pilih : ")
    if pilih == "1":
        nilai_mahasiswa()
    elif pilih == "2":
        pembayaran()
    elif pilih == "3":
        menu_cal()
    else:
        exit
    tanya()
                                             
def tanya():
    tanya = input("\nkembali ke menu (y/t)? ")
    if tanya == "y":
        menu()
    elif tanya == "t":
        exit
    else:
        print("\n\tsalah input...!!!")
        
username = input("\nusername :")
password = getpass.getpass()
print("==================================================================")

if username == "iyan santoso" and password == "iyan123":
    menu()


else:
    print("maaf password atau username anda salah........")
    
        

    
