import tkinter as tk
from datetime import datetime, date

def hitung_umur():
    try:
        tanggal_lahir = int(tanggal_entry.get())
        bulan_lahir = int(bulan_entry.get())
        tahun_lahir = int(tahun_entry.get())

        tanggal_lahir_date = date(tahun_lahir, bulan_lahir, tanggal_lahir)

        tanggal_hari_ini = date.today()

        umur_tahun = tanggal_hari_ini.year - tanggal_lahir_date.year
        umur_bulan = tanggal_hari_ini.month - tanggal_lahir_date.month
        umur_hari = tanggal_hari_ini.day - tanggal_lahir_date.day

        if umur_hari < 0:
            umur_bulan -= 1
            umur_hari += (tanggal_hari_ini - tanggal_lahir_date.replace(year=tanggal_hari_ini.year, month=tanggal_hari_ini.month, day=1)).days
        if umur_bulan < 0:
            umur_tahun -= 1
            umur_bulan += 12

        result_label.config(text=f"Umur Anda: {umur_tahun} tahun, {umur_bulan} bulan, dan {umur_hari} hari")
    except ValueError:
        result_label.config(text="Format tanggal tidak valid. Harap masukkan tanggal dalam format DD-MM-YYYY.")
    except Exception as e:
        result_label.config(text=f"Terjadi kesalahan: {str(e)}")

window = tk.Tk()
window.title("Penghitung Umur")
window.geometry("500x300")

label_tanggal = tk.Label(window, text="Masukkan Tanggal Lahir:")
label_tanggal.pack(pady=10)

tanggal_label = tk.Label(window, text="Tanggal (DD):")
tanggal_label.pack()
tanggal_entry = tk.Entry(window)
tanggal_entry.pack()

bulan_label = tk.Label(window, text="Bulan (MM):")
bulan_label.pack()
bulan_entry = tk.Entry(window)
bulan_entry.pack()

tahun_label = tk.Label(window, text="Tahun (YYYY):")
tahun_label.pack()
tahun_entry = tk.Entry(window)
tahun_entry.pack()

tombol_hitung = tk.Button(window, text="Hitung Umur", command=hitung_umur)
tombol_hitung.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
