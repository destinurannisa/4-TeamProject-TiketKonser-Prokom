import csv
from openpyxl import load_workbook
import PySimpleGUI as sg
from datetime import datetime
from ctypes import resize
import tkinter
import tkinter.messagebox
from tkinter import *
import tkinter as tk
from turtle import width
from PIL import ImageTk, Image
import pandas as pd

#Login pembeli
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

#Bagian Pemesanan
def pemesanan():
    Pemesanan = input("Apakah anda ingin melakukan pemesanan? (Y/N) ")
    if Pemesanan == "Y" or "y": 

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

        print("Menampilkan tabel harga dan sisa kursi")
    elif Pemesanan == "N" or "n":
        print("END")
        exit()
    else:
        print("Input tidak valid")
        print("Mohon melakukan input ulang")
        return pemesanan()
pemesanan()

#Pemilihan Jenis Tiket
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

#Proses Pembayaran Tiket
def tiket():
    global Total_Bayar
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

#Pemilihan Metode Pembayaran
def pembayaran():
    print("Anda dapat membayar dengan metode tunai/OVO/Gopay/Shopeepay/Credit Card/Debit")
    Metode_Pembayaran = input("Metode pembayaran apa yang akan anda gunakan? ")
    if Metode_Pembayaran == "tunai":
        Uang_Pembayaran = int(input("Nominal yang dikeluarkan? "))
        Kembalian = (Uang_Pembayaran - Total_Bayar)
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

#Konfirmasi Untuk Transaksi Lain
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

nmpmb=Label(screen,text='....', font=("Calibri", 11,"bold"), background="white")
nmpmb.place(x=340,y=170)

tgl=Label(screen,text='TANGGAL', font=("Calibri", 11), background="white")
tgl.place(x=340,y=200)

tglacr=Label(screen,text='SELASA, 21 AGUSTUS 2017', font=('Calibri', 11, 'bold'), background="white")
tglacr.place(x=340,y=230)

wkt=Label(screen,text="WAKTU", font=("Calibri", 11), background="white")
wkt.place(x=340,y=260)

jam=Label(screen,text='20:00', font=("Calibri", 11, 'bold'), background="white")
jam.place(x=340,y=290)

jns=Label(screen,text='JENIS SEAT', font=("Calibri", 11,), background="white")
jns.place(x=340,y=320)

jnsseat=Label(screen,text='VVIP', font=("Calibri", 11, "bold"), background="white")
jnsseat.place(x=340,y=350)

jmlh=Label(screen,text='JUMLAH', font=("Calibri", 11), background="white")
jmlh.place(x=340,y=380)

byk=Label(screen,text='3', font=("Calibri", 11, "bold"), background="white")
byk.place(x=340,y=410)

topgrid=Label(screen,text='__________________________________________________________________', background="white")
topgrid.place(x=335,y=440)

tb=Label(screen,text='Total Bayar', font=('Calibri', 14, 'bold'), background="white")
tb.place(x=340,y=470)

botgrid=Label(screen,text='__________________________________________________________________', background="white")
botgrid.place(x=335,y=500)

snk=Label(screen,text='* Pemesanan Tidak Dapat Dikembalikan Jika Sudah Melakukan Transaksi', font=('Calibri', 7), background="white", fg='red')
snk.place(x=340,y=530)

Cetak_button=PhotoImage(file="cetakbutton.png")
cetak=Button(image=Cetak_button, borderwidth=0, cursor="hand2", bd=0, font=("Calibri"), background="white")
cetak.place(x=430,y=600)

screen.mainloop()