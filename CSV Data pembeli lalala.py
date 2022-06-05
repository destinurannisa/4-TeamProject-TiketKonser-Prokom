import csv

def login():
    namapembeli = input("Nama Pembeli = ")
    nohp = input("No HP = ")
    with open('datapembeli.csv', 'r') as auth:
        reader = csv.reader(auth)
        next(reader)
        for row in reader:
            if ([namapembeli,nohp] == row) :
                print("Anda sudah memiliki akun")
                print("Data Pengguna Telah Tervalidasi")
                return False
        print("Data anda tidak ditemukan dalam database")
        input_valid = False
        while (input_valid == False):
            Tidak_punya_akun = input("Apakah anda memang tidak memiliki akun?(Y/N)  ")
            if Tidak_punya_akun == "Y":
                print("Data anda akan disimpan dalam database sebagai akun anda")
                print("Mohon lakukan kembali validasi data")
                with open('datapembeli.csv', 'a') as csvfile:
                    databaru = csv.writer(csvfile, delimiter= ",") 
                    databaru.writerow([namapembeli, nohp])
                input_valid = True
                login()
            elif Tidak_punya_akun == "N" :
                print("Input invalid")
                input_valid = True
                login()
            else:
                input_valid = False
login()

                    

               
