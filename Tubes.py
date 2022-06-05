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
            Tidak_punya_akun = input("Apakah anda memang tidak memiliki akun?(Y/N) ")
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

pemesanan_ulang = True
while (pemesanan_ulang == True):
    print("Tampilan menu")
    #muncul gambar tabel
    input_valid = False
    while (input_valid == False) :
        Pemesanan = input("Apakah anda ingin melakukan pemesanan? (Y/N) ")
        if Pemesanan == "Y":
            input_valid = True
            pemesanan_ulang = False
            print("Menampilkan gambar seat kursi penonton")
            print("Menampilkan tabel harga dan sisa kursi")
        elif Pemesanan == "N":
            input_valid = True
            print("END")
            exit()
        else:
            input_valid = False
            print("Input tidak valid")
            print("Mohon melakukan input ulang")
    input_valid = False
    while (input_valid == False) :
        Tiket = input("Jenis tiket yang anda pilih adalah : ")
        if Tiket == "VVIP":
            input_valid = True
            Jumlah_tiket = int(input("Berapa jumlah tiket yang akan dibeli? "))
            Total_Bayar = 5000000 * Jumlah_tiket
            print("Total Bayar adalah ", Total_Bayar)
        elif Tiket == "VIP":
            input_valid = True
            Jumlah_tiket = int(input("Berapa jumlah tiket yang akan dibeli? "))
            Total_Bayar = 4000000 * Jumlah_tiket
            print("Total Bayar adalah ", Total_Bayar)
        elif Tiket == "A":
            input_valid = True
            Jumlah_tiket = int(input("Berapa jumlah tiket yang akan dibeli? "))
            Total_Bayar = 3000000 * Jumlah_tiket
            print("Total Bayar adalah ", Total_Bayar)
        elif Tiket == "B":
            input_valid = True
            Jumlah_tiket = int(input("Berapa jumlah tiket yang akan dibeli? "))
            Total_Bayar = 2500000 * Jumlah_tiket
            print("Total Bayar adalah ", Total_Bayar)
        elif Tiket == "VIP":
            input_valid = True
            Jumlah_tiket = int(input("Berapa jumlah tiket yang akan dibeli? "))
            Total_Bayar = 2000000 * Jumlah_tiket
            print("Total Bayar adalah ", Total_Bayar)
        else:
            input_valid = False
            print("Input tidak valid")
            print("Mohon melakukan input ulang")

    input_valid = False
    while (input_valid == False) :
        Metode_Pembayaran = input("Metode pembayaran apa yang akan anda gunakan? ")
        if Metode_Pembayaran == "tunai":
            input_valid = True
            Uang_Pembayaran = int(input("Nominal yang dikeluarkan? "))
            Kembalian = (Uang_Pembayaran - Total_Bayar)
            print("Jumlah kembalian adalah ", Kembalian)
            print("Terimakasih telah melakukan pembayaran")
        elif Metode_Pembayaran == "OVO":
            input_valid = True
            Nominal_Bayar = int(input("Nominal yang anda keluarkan adalah :"))
            print("Terimakasih telah melakukan pembayaran")
        elif Metode_Pembayaran == "Gopay":
            input_valid = True
            Nominal_Bayar = int(input("Nominal yang anda keluarkan adalah :"))
            print("Terimakasih telah melakukan pembayaran") 
        elif Metode_Pembayaran == "Shopeepay":
            input_valid = True
            Nominal_Bayar = int(input("Nominal yang anda keluarkan adalah :"))
            print("Terimakasih telah melakukan pembayaran")
        elif Metode_Pembayaran == "Credit Card":
            input_valid = True
            Nominal_Bayar = int(input("Nominal yang anda keluarkan adalah :"))
            print("Terimakasih telah melakukan pembayaran")
        elif Metode_Pembayaran == "Debit":
            input_valid = True
            Nominal_Bayar = int(input("Nominal yang anda keluarkan adalah :"))
            print("Terimakasih telah melakukan pembayaran")
        else:
            input_valid = False
            print("Input tidak valid")
            print("Mohon melakukan input ulang")

    input_valid = False
    while (input_valid == False):
        Transaksi_Lagi = input("Apakah anda ingin melakukan transaksi lagi? ")
        if Transaksi_Lagi == "Y":
            input_valid = True
            pemesanan_ulang = True
        elif Transaksi_Lagi == "N":
            input_valid = True
            print("Selesai")
            exit()
        else:
            input_valid = False
            print("Input tidak valid")
            print("Mohon melakukan input ulang")


