from cgitb import text
import csv
from datetime import datetime
from ctypes import resize
from functools import total_ordering
from os import times
import tkinter
import tkinter.messagebox
from tkinter import *
import tkinter as tk
from tkinter.tix import TEXT
from turtle import update, width
from typing import Literal
from PIL import ImageTk, Image
from numpy import False_
import pandas as pd
from tempfile import NamedTemporaryFile
from fpdf import FPDF
from datetime import datetime
import random
print("")
print("--------------------------------------------------------------------------------")
print("          Selamat Datang di Pemesanan Tiket Konser Musik Ariana Grande          ")
print("--------------------------------------------------------------------------------")
print("")

# Login pembeli
def login():
    global namapembeli, nohp, time_stamp, timess
    print("================================================================================")
    namapembeli = input("Nama Lengkap = ")
    input_valid = False
    while (input_valid == False):
        nohp = input("Nomor HP     = ")
        if nohp.isnumeric() == False:
            print("No HP tidak valid")
            input_valid = False
        else:
            input_valid = True
    time_stamp = datetime.now().strftime("%d/%m/%Y")
    timess = datetime.now().strftime("%H:%M")
    print("================================================================================")
    with open('data_akun.csv', 'r') as auth:
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
            if Tidak_punya_akun == "Y" or Tidak_punya_akun == "y":
                print("Data anda akan disimpan dalam database sebagai akun anda")
                print("Mohon lakukan kembali validasi data")
                with open("data_akun.csv", "a") as csvfile:
                    newdata = csv.writer(csvfile, delimiter= ",")
                    newdata.writerow([namapembeli, nohp])
                input_valid = True
                login()
            elif Tidak_punya_akun == "N" or Tidak_punya_akun == "n":
                print("")
                print("Input invalid")
                input_valid = True
                login()
            else: 
                input_valid = False
login()

# Bagian Pemesanan
def pemesanan():
    global notrans
    print("")
    notrans = str(random.random())
    Pemesanan = input("Apakah anda ingin melakukan pemesanan? (Y/N) ")
    if Pemesanan == "Y" or Pemesanan == 'y': 
        print("--------------------------------------------------------------------------------")
        print("                                  Tampilan Menu                                 ")
        print("--------------------------------------------------------------------------------")
        #Menampilkan Gambar Stage
        window = Tk()
        text = Text(window)
        image = Image.open("stage.png")
        img = ImageTk.PhotoImage(image)
        poster = Label(window,image = img)
        poster.image = img
        poster.grid(column=0,row=0,sticky = "NW")
        wrapper = LabelFrame(window)
        wrapper.grid(column=0,row=1)
        window.geometry("730x480")
        window.resizable(False,False)
        window.mainloop()

        # Menampilkan Tabel
        print("")
        print("----------------------------")
        updt = pd.read_csv("tabeltiket.csv")
        print(updt.to_string(index=False))
        print("----------------------------")
    elif Pemesanan == "N" or Pemesanan == 'n':
        print("--------------------------------------------------------------------------------")
        print("                                    Terima kasih                                ")
        print("--------------------------------------------------------------------------------")
        exit()
    else:
        print("")
        print("Input tidak valid")
        print("Mohon melakukan input ulang")
        return pemesanan()
    def tiket():
        global Total_Bayar, jenis, jumlah
        jenis = input("Jenis tiket yang anda pilih adalah (VVIP, VIP, A, B, C) = ")
        if jenis == "VVIP" or jenis == "vvip" or jenis == "VIP" or jenis == "vip" or jenis == "A" or jenis == "a" or jenis == "B" or jenis == "b" or jenis == "C" or jenis == "c":
            input_valid = False
            while (input_valid == False):
                updt = pd.read_csv("tabeltiket.csv")
                jumlah = input("Jumlah = ")
                if jumlah.isnumeric() == True:
                    jumlah = int(jumlah)
                    if jenis == "VVIP" or jenis == "vvip":
                        if jumlah > updt.loc[0, 'Kuota']:
                            print("Sisa kursi tidak mencukupi")
                            print("Sisa kursi yang tersedia =", updt.loc[0, 'Kuota'])
                            input_valid = False
                        else:
                            input_valid = True
                    elif jenis == "VIP" or jenis == "vip":
                        if jumlah > updt.loc[1, 'Kuota']:
                            print("Sisa kursi tidak mencukupi")
                            print("Sisa kursi yang tersedia =", updt.loc[1, 'Kuota'])
                            input_valid = False
                        else:
                            input_valid = True
                    elif jenis == "A" or jenis == "a":
                        if jumlah > updt.loc[2, 'Kuota']:
                            print("Sisa kursi tidak mencukupi")
                            print("Sisa kursi yang tersedia =", updt.loc[2, 'Kuota'])
                            input_valid = False
                        else:
                            input_valid = True        
                    elif jenis == "B" or jenis == "b":
                        if jumlah > updt.loc[3, 'Kuota']:
                            print("Sisa kursi tidak mencukupi")
                            print("Sisa kursi yang tersedia =", updt.loc[3, 'Kuota'])
                            input_valid = False
                        else:
                            input_valid = True
                    elif jenis == "C" or jenis == "c":
                        if jumlah > updt.loc[4, 'Kuota']:
                            print("Sisa kursi tidak mencukupi")
                            print("Sisa kursi yang tersedia =", updt.loc[4, 'Kuota'])
                            input_valid = False
                        else:
                            input_valid = True
                else:
                    input_valid = False
        else:
            tiket()
        print("------------------------------------------------------")
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        fields = ['Jenis', 'Harga', 'Kuota']
        with open('tabeltiket.csv', 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=fields)
            writer = csv.DictWriter(tempfile, fieldnames=fields)
            for row in reader:
                updt = pd.read_csv("tabeltiket.csv")
                if jenis == "VVIP" or jenis == "vvip":
                    Total_Bayar = 5000000 * jumlah
                    kuota = updt.loc[0, 'Kuota'] - jumlah
                    updt.loc[0, 'Kuota'] = kuota
                elif jenis == "VIP" or jenis == "vip":
                    Total_Bayar = 4000000 * jumlah
                    kuota = updt.loc[1, 'Kuota'] - jumlah
                    updt.loc[1, 'Kuota'] = kuota
                elif jenis == "A" or jenis == "a":
                    Total_Bayar = 3000000 * jumlah
                    kuota = updt.loc[2, 'Kuota'] - jumlah
                    updt.loc[2, 'Kuota'] = kuota
                elif jenis == "B" or jenis == "b":
                    Total_Bayar = 2500000 * jumlah
                    kuota = updt.loc[3, 'Kuota'] - jumlah
                    updt.loc[3, 'Kuota'] = kuota
                else:
                    Total_Bayar = 2000000 * jumlah
                    kuota = updt.loc[4, 'Kuota'] - jumlah
                    updt.loc[4, 'Kuota'] = kuota
            updt.to_csv("tabeltiket.csv", index=False)
            print("")
            print("------------------------------------------------------")
            print("Total Bayar = Rp", Total_Bayar)
            print("------------------------------------------------------")
        #Pemilihan Metode Pembayaran
        def pembayaran():
            global Metode_Pembayaran, status
            print("")
            print("Anda dapat membayar dengan metode (Tunai / OVO / Gopay / Shopeepay / Credit / Debit)")
            Metode_Pembayaran = input("Metode pembayaran apa yang akan anda gunakan? ")
            if Metode_Pembayaran == "Tunai" or Metode_Pembayaran == "tunai" or Metode_Pembayaran == "TUNAI":
                print("")
                print("------------------------------------------------------")
                input_valid = False
                while (input_valid == False):
                    Uang_Pembayaran = input("Nominal yang anda keluarkan adalah : Rp ")
                    if Uang_Pembayaran.isnumeric() == True:
                        Uang_Pembayaran = int(Uang_Pembayaran)
                        if Uang_Pembayaran < Total_Bayar:
                            print("Uang tidak cukup")
                            print("Tagihan = Rp", Total_Bayar)
                            print("------------------------------------------------------")
                            input_valid = False
                        else:
                            Kembalian = (Uang_Pembayaran - Total_Bayar)
                            print("Jumlah kembalian adalah Rp", Kembalian)
                            print("------------------------------------------------------")
                            print("")
                            print("------------------------------------------------------")
                            print("Terimakasih telah melakukan pembayaran")
                            print("------------------------------------------------------")
                            input_valid = True
                    else:
                        input_valid = False
            elif Metode_Pembayaran == "OVO" or Metode_Pembayaran == "ovo"  or Metode_Pembayaran == "Gopay" or Metode_Pembayaran == "gopay" or Metode_Pembayaran == "GOPAY" or Metode_Pembayaran == "Shopeepay" or Metode_Pembayaran == "shopeepay" or Metode_Pembayaran == "SHOPEEPAY"  or Metode_Pembayaran == "Credit" or Metode_Pembayaran == "credit" or Metode_Pembayaran == "CREDIT"  or Metode_Pembayaran == "Debit" or Metode_Pembayaran == "debit" or Metode_Pembayaran == "DEBIT":
                input_valid = False
                while (input_valid == False):
                    input_valid = False
                    while (input_valid == False):
                        Nominal_Bayar = input("Nominal yang anda bayarkan adalah : Rp ")
                        if Nominal_Bayar.isnumeric() == True:
                            Nominal_Bayar = int(Nominal_Bayar)
                            input_valid = True
                        else: 
                            input_valid = False
                    if Metode_Pembayaran == "OVO" or Metode_Pembayaran == "ovo":
                        print("")
                        if Nominal_Bayar == Total_Bayar:
                            print("")
                            print("--------------------------------------------------------------------------------")
                            print("                    Terima kasih telah melakukan pembayaran                     ")
                            print("--------------------------------------------------------------------------------")
                            input_valid = True
                        else:
                            print("---------------------------------------------------")
                            print("Nominal yang anda input tidak sesuai dengan tagihan")
                            print("Tagihan yang harus anda bayar = Rp", Total_Bayar)
                            input_valid = False
                    elif Metode_Pembayaran == "Gopay" or Metode_Pembayaran == "gopay" or Metode_Pembayaran == "GOPAY":
                        print("")
                        if Nominal_Bayar == Total_Bayar:
                            print("--------------------------------------------------------------------------------")
                            print("                    Terima kasih telah melakukan pembayaran                     ")
                            print("--------------------------------------------------------------------------------")
                            input_valid = True
                        else:
                            print("---------------------------------------------------")
                            print("Nominal yang anda input tidak sesuai dengan tagihan")
                            print("Tagihan yang harus anda bayar = Rp ", Total_Bayar)
                            input_valid = False
                    elif Metode_Pembayaran == "Shopeepay" or Metode_Pembayaran == "shopeepay" or Metode_Pembayaran == "SHOPEEPAY":
                        print("")
                        if Nominal_Bayar == Total_Bayar:
                            print("--------------------------------------------------------------------------------")
                            print("                    Terima kasih telah melakukan pembayaran                     ")
                            print("--------------------------------------------------------------------------------")
                            input_valid = True
                        else:
                            print("---------------------------------------------------")
                            print("Nominal yang anda input tidak sesuai dengan tagihan")
                            print("Tagihan yang harus anda bayar = Rp", Total_Bayar)
                            input_valid = False
                    elif Metode_Pembayaran == "Credit" or Metode_Pembayaran == "credit" or Metode_Pembayaran == "CREDIT":
                        print("")
                        if Nominal_Bayar == Total_Bayar:
                            print("--------------------------------------------------------------------------------")
                            print("                    Terima kasih telah melakukan pembayaran                     ")
                            print("--------------------------------------------------------------------------------")
                            input_valid = True
                        else:
                            print("---------------------------------------------------")
                            print("Nominal yang anda input tidak sesuai dengan tagihan")
                            print("Tagihan yang harus anda bayar = Rp", Total_Bayar)
                            input_valid = False
                    elif Metode_Pembayaran == "Debit" or Metode_Pembayaran == "debit" or Metode_Pembayaran == "DEBIT":
                        print("")
                        if Nominal_Bayar == Total_Bayar:
                            print("--------------------------------------------------------------------------------")
                            print("                    Terima kasih telah melakukan pembayaran                     ")
                            print("--------------------------------------------------------------------------------")
                            input_valid = True
                        else:
                            print("---------------------------------------------------")
                            print("Nominal yang anda input tidak sesuai dengan tagihan")
                            print("Tagihan yang harus anda bayar = Rp", Total_Bayar)
                            input_valid = False
            else:
                print("")
                print("Input tidak valid")
                print("Mohon melakukan input ulang")
                return pembayaran()
            status = "Berhasil"
            #Menyimpan rekapan transaksi pada CSV
            def simpan():
                with open('rekap_transaksi.csv', 'a') as csvfile:
                    rekap = csv.writer(csvfile, delimiter= ",") 
                    rekap.writerow([time_stamp, timess, notrans, namapembeli, nohp, jenis, jumlah, Total_Bayar, Metode_Pembayaran,status])
                    print("")
                    print("--------------------------------------------------------------------------------")
                    print("                         Berikut Struk Transaksi Anda                           ")
                    print("--------------------------------------------------------------------------------")

                    #Menampilkan Struk Pembayaran
                    screen = Tk()
                    screen.title("Konfirmasi Pembayaran")
                    screen.config(background="white")

                    screen.geometry('1000x700')
                    screen.resizable(False,False)

                    kertas=PhotoImage(file='kotaktiket.png')
                    Label(screen,image=kertas,background="white").place(x=320,y=40)

                    poster=PhotoImage(file='poster.png')
                    Label(screen,image=poster).place(x=540,y=140)

                    jdl=Label(screen,text='Detail Tranksaksi Tiket', font=("Calibri", 18, "bold"), background="white")
                    jdl.place(x=380,y=60)

                    tpgrid=Label(screen,text='__________________________________________________________________', background="white")
                    tpgrid.place(x=335,y=90)

                    acr=Label(screen,text="ARIANA GRANDE MUSIC CONCERT", font=('Calibri', 12, 'bold'), background="white")
                    acr.place(x=380,y=110)

                    nm=Label(screen,text='NAMA PEMBELI', font=("Calibri", 11), background="white")
                    nm.place(x=340,y=140)

                    nmpmb=Label(screen,text=namapembeli, font=("Calibri", 12,"bold"), background="white")
                    nmpmb.place(x=340,y=170)

                    tgl=Label(screen,text='TANGGAL', font=("Calibri", 11), background="white")
                    tgl.place(x=340,y=200)

                    tglacr=Label(screen,text=time_stamp, font=('Calibri', 12, 'bold'), background="white")
                    tglacr.place(x=340,y=230)

                    wkt=Label(screen,text="WAKTU", font=("Calibri", 11), background="white")
                    wkt.place(x=340,y=260)

                    jam=Label(screen,text=timess, font=("Calibri", 12, 'bold'), background="white")
                    jam.place(x=340,y=290)

                    jns=Label(screen,text='JENIS SEAT', font=("Calibri", 11,), background="white")
                    jns.place(x=340,y=320)

                    jnsseat=Label(screen,text=jenis, font=("Calibri", 12, "bold"), background="white")
                    jnsseat.place(x=340,y=350)

                    jmlh=Label(screen,text='JUMLAH', font=("Calibri", 11), background="white")
                    jmlh.place(x=340,y=380)

                    byk=Label(screen,text=jumlah, font=("Calibri", 12, "bold"), background="white")
                    byk.place(x=340,y=410)

                    topgrid=Label(screen,text='__________________________________________________________________', background="white")
                    topgrid.place(x=335,y=440)

                    tb=Label(screen,text='Total Bayar', font=('Calibri', 14, 'bold'), background="white")
                    tb.place(x=340,y=470)

                    ttlbyr=Label(screen,text="Rp         %d " %Total_Bayar, font=('Calibri', 15, 'bold'), background="white")
                    ttlbyr.place(x=520,y=470)

                    botgrid=Label(screen,text='__________________________________________________________________', background="white")
                    botgrid.place(x=335,y=500)

                    snk=Label(screen,text='* Pemesanan Tidak Dapat Dikembalikan Jika Sudah Melakukan Transaksi', font=('Calibri', 7), background="white", fg='red')
                    snk.place(x=340,y=530)

                    Cetak_button=PhotoImage(file="cetakbutton.png")
                    cetak=Button(image=Cetak_button, borderwidth=0, cursor="hand2", command=lambda:destroyscreen(), bd=0, font=("Calibri"), background="white")
                    cetak.place(x=430,y=600)
                    def destroyscreen():
                         screen.destroy()

                    screen.mainloop()

                    class PDF(FPDF):
                        def header(self):
                            # Logo
                            self.image('background.jpeg', 60, 40, 80)
                            self.image('fotopenyanyi.jpg', 135, 30, 50)
                            #font
                            self.set_font('helvetica', 'B', 20)
                            #warna frame, background, font
                            self.set_draw_color(0,80,180)
                                
                            # Helvetica bold 15
                            self.set_font('helvetica', 'B', 20)
                            # Title
                            self.cell(0, 0, '____________________________________', border=False, ln=1, align ='C')
                            self.cell(0, 0, 'TIKET KONSER ARIANA GRANDE', border=False, ln=1, align ='C')
                            # Line break
                            self.ln(0)

                    pdf = PDF('P','mm', (200, 110))
                    pdf.alias_nb_pages()
                    pdf.add_page()
                    pdf.set_font('Arial', 'b', 12)
                    pdf.cell(5, 30, ' ', 0, 1)
                    pdf.cell(103, 7, 'BUKTI PEMBELIAN', border=True, ln=1)
                    pdf.cell(5, 7, ' ', 0, 1)
                    pdf.cell(5, 7, 'Tanggal : 21 Agustus 2017', 0, 1)
                    pdf.cell(5, 7, 'Waktu : 20.00', 0, 1)
                    pdf.cell(5, 7, 'Seat : %s' %jenis, 0, 1)
                    pdf.cell(5, 7, 'Jumlah Tiket : %s' %jumlah, 0, 1)
                    pdf.output('tiket_%s.pdf' %notrans, 'F')
                #Konfirmasi Untuk Transaksi Lain
                def transaksi_lain():
                    print("")
                    Transaksi_Lagi = input("Apakah anda ingin melakukan transaksi lagi? (Y/N) ")
                    if Transaksi_Lagi == "Y" or Transaksi_Lagi == "y":
                        return pemesanan()
                    elif Transaksi_Lagi == "N"  or Transaksi_Lagi == "n":
                        print("")
                        print("--------------------------------------------------------------------------------")
                        print("                     Terima kasih telah melakukan transaksi                     ")
                        print("--------------------------------------------------------------------------------")
                        print("")
                        exit()
                    else:
                        print("")        
                        print("Input tidak valid")
                        print("Mohon melakukan input ulang")
                        return transaksi_lain()
                transaksi_lain()
            simpan()
        pembayaran()
    tiket()
pemesanan() 