def calculation(bkanak, bDewasa, bTua,duit):
        totaltiketbudak = bkanak * 7
        totaltiketdewasa = bDewasa * 14
        totaltikettua = bTua * 10
        kos = totaltiketbudak + totaltiketdewasa + totaltikettua
        if duit >= kos:
            final_total = duit - kos
            print(f"\nTiket yang dibeli:-\nKanak-kanak: {bkanak}\nDewasa: {bDewasa}\nWarga emas: {bTua}\nHarga keseluruhan: RM{kos}\nBaki: RM{final_total}")
        else:
            print("Maaf, duit yang anda masukkan tidak mencukupi")

print("##################################################################")
print("                Hai Selamat Datang Ke Zoo Putra                   ")
print("##################################################################")
print("                          HARGA TIKET                             ")
print("KANAK-KANAK(UMUR 12 TAHNU KE BAWAH)                         RM7.00")
print("DEWASA(UMUR 13-59 TAHUN                                    RM14.00")
print("WARGA EMAS(60 TAHUN KE ATAS)                               RM10.00\n")

bkanak = int(input("Bilangan tiket kanak-kanak: "))
bDewasa = int(input("Bilangan tiket dewasa: "))
bTua = int(input("Bilangan tiket warga emas: "))
duit = int(input("Duit yang diberi: "))

calculation(bkanak, bDewasa, bTua ,duit)

print("                       -TERIMA KASIH-                             ")
print("##################################################################")