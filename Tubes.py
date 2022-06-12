import csv
def login():
    namapembeli = input("Nama Pembeli = ")
    nohp = input("No HP = ")
    with open('datapembeli.csv', 'r') as auth:
        reader = csv.reader(auth)
        next(reader)
        for row in reader :
            if ([namapembeli, nohp] == row):
                print("Pengguna sudah memiliki akun")
                print("Data pengguna telah tervalidasi")
                return False
        print("Data pengguna tidak ditemukan dalam database")
        input_valid = False
        while (input_valid == False):
            Tidak_punya_akun = input("Apakah anda memang tidak memiliki akun? (Y/N) ")
            if Tidak_punya_akun == "Y":
                print("Data anda akan disimpan dalam database sebagai akun anda")
                print("Mohon lakukan kembali validasi data")
                with open("datapembeli.csv", "a") as csvfile:
                    newdata = csv.writer(csvfile, delimiter= ",")
                    newdata.writerow([namapembeli, nohp])
                input_valid = True
                login()
            elif Tidak_punya_akun == "N":
                print("Input invalid")
                input_valid = True
                login()
            else: 
                input_valid = False
login()
#Bagian validasi data selesai

def pemesanan():
    Pemesanan = input("Apakah anda ingin melakukan pemesanan? (Y/N) ")
    if Pemesanan == "Y" or "y":
        print("Menampilkan gambar seat kursi penonton")
        print("Menampilkan tabel harga dan sisa kursi")
    elif Pemesanan == "N" or "n":
        print("END")
        exit()
    else:
        print("Input tidak valid")
        print("Mohon melakukan input ulang")
        return pemesanan()
pemesanan()

def tiket():
    Tiket = input("Jenis tiket yang anda pilih adalah : ")
    if Tiket == "VVIP":
        Jumlah_tiket = int(input("Berapa jumlah tiket yang akan dibeli? "))
        Total_Bayar = 5000000 * Jumlah_tiket
        print("Total Bayar adalah ", Total_Bayar)
    elif Tiket == "VIP":
        Jumlah_tiket = int(input("Berapa jumlah tiket yang akan dibeli? "))
        Total_Bayar = 4000000 * Jumlah_tiket
        print("Total Bayar adalah ", Total_Bayar)
    elif Tiket == "A":
        Jumlah_tiket = int(input("Berapa jumlah tiket yang akan dibeli? "))
        Total_Bayar = 3000000 * Jumlah_tiket
        print("Total Bayar adalah ", Total_Bayar)
    elif Tiket == "B":
        Jumlah_tiket = int(input("Berapa jumlah tiket yang akan dibeli? "))
        Total_Bayar = 2500000 * Jumlah_tiket
        print("Total Bayar adalah ", Total_Bayar)
    elif Tiket == "VIP":
        Jumlah_tiket = int(input("Berapa jumlah tiket yang akan dibeli? "))
        Total_Bayar = 2000000 * Jumlah_tiket
        print("Total Bayar adalah ", Total_Bayar)
    else:
        print("Input tidak valid")
        print("Mohon melakukan input ulang")
        return tiket()
def tiket():
    Tiket = input("Jenis tiket yang anda pilih adalah : ")
    if Tiket == "VVIP":
        Jumlah_tiket = int(input("Berapa jumlah tiket yang akan dibeli? "))
        Total_Bayar = 5000000 * Jumlah_tiket
        print("Total Bayar adalah ", Total_Bayar)
    elif Tiket == "VIP":
        Jumlah_tiket = int(input("Berapa jumlah tiket yang akan dibeli? "))
        Total_Bayar = 4000000 * Jumlah_tiket
        print("Total Bayar adalah ", Total_Bayar)
    elif Tiket == "A":
        Jumlah_tiket = int(input("Berapa jumlah tiket yang akan dibeli? "))
        Total_Bayar = 3000000 * Jumlah_tiket
        print("Total Bayar adalah ", Total_Bayar)
    elif Tiket == "B":
        Jumlah_tiket = int(input("Berapa jumlah tiket yang akan dibeli? "))
        Total_Bayar = 2500000 * Jumlah_tiket
        print("Total Bayar adalah ", Total_Bayar)
    elif Tiket == "VIP":
        Jumlah_tiket = int(input("Berapa jumlah tiket yang akan dibeli? "))
        Total_Bayar = 2000000 * Jumlah_tiket
        print("Total Bayar adalah ", Total_Bayar)
    else:
        print("Input tidak valid")
        print("Mohon melakukan input ulang")
        return tiket()
tiket()
def pembayaran():
    print("Anda dapat membayar dengan metode tunai/OVO/Gopay/Shopeepay/Credit Card/Debit")
    Metode_Pembayaran = input("Metode pembayaran apa yang akan anda gunakan? ")
    if Metode_Pembayaran == "tunai":
        Uang_Pembayaran = int(input("Nominal yang dikeluarkan? "))
        Kembalian = (Uang_Pembayaran - (Total_Bayar))
        print("Jumlah kembalian adalah ", Kembalian)
        print("Terimakasih telah melakukan pembayaran")
    elif Metode_Pembayaran == "OVO":
        Nominal_Bayar = int(input("Nominal yang anda keluarkan adalah :"))
        if Nominal_Bayar == tiket:
            print("Terima kasih telah melakukan pembayaran")
        else:
            return Nominal_Bayar()
    elif Metode_Pembayaran == "Gopay":
        Nominal_Bayar = int(input("Nominal yang anda keluarkan adalah :"))
        print("Terima kasih telah melakukan pembayaran")
    elif Metode_Pembayaran == "Shopeepay":
        Nominal_Bayar = int(input("Nominal yang anda keluarkan adalah :"))
        print("Terima kasih telah melakukan pembayaran")
    elif Metode_Pembayaran == "Credit Card":
        Nominal_Bayar = int(input("Nominal yang anda keluarkan adalah :"))
        print("Terima kasih telah melakukan pembayaran")
    elif Metode_Pembayaran == "Debit/Credit":
        Nominal_Bayar = int(input("Nominal yang anda keluarkan adalah :"))
        print("Terima kasih telah melakukan pembayaran")
    else:
        print("Input tidak valid")
        print("Mohon melakukan input ulang")
        return pembayaran()
pembayaran()
def transaksi_lain():
    Transaksi_Lagi = input("Apakah anda ingin melakukan transaksi lagi? ")
    if Transaksi_Lagi == "Y":
        return pemesanan()
    elif Transaksi_Lagi == "N":
        print("Selesai")
        exit()
    else:        
        print("Input tidak valid")
        print("Mohon melakukan input ulang")
        return transaksi_lain()
transaksi_lain()