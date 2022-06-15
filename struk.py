from tkinter import *

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

nmpmb=Label(screen,text='Btara Aryanda', font=("Calibri", 11,"bold"), background="white")
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