import tkinter as tk
from tkinter import ttk, messagebox

# =========================================================================
# ANGGOTA 1 (KETUA): PONDASI OOP
# =========================================================================
class Kuliner:
    def __init__(self, nama, harga, kategori):
        self.nama = nama
        self.harga = int(harga)
        self.kategori = kategori

class WarungMakan(Kuliner):
    def __init__(self, nama, harga, kategori, nama_warung, lokasi, rating):
        super().__init__(nama, harga, kategori)
        self.nama_warung = nama_warung
        self.lokasi = lokasi  
        self.rating = float(rating)

# =========================================================================
# ANGGOTA 2: SILAKAN TARUH CLASS LINKED LIST KAMU DI BAWAH SINI
# =========================================================================
# TODO: Anggota 2 ketik di sini...


# =========================================================================
# ANGGOTA 3: SILAKAN TARUH CLASS BST & BINARY SEARCH DI BAWAH SINI
# =========================================================================
# TODO: Anggota 3 ketik di sini...


# =========================================================================
# ANGGOTA 4: SILAKAN TARUH CLASS QUEUE & MERGE SORT DI BAWAH SINI
# =========================================================================
# TODO: Anggota 4 ketik di sini...


# =========================================================================
# TAMPILAN UTAMA APLIKASI (GUI TKINTER)
# =========================================================================
class AplikasiRekomendasiAnakKost:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Rekomendasi Makanan Anak Kost Unila")
        self.root.geometry("600x400")
        
        tk.Label(root, text="Sistem Rekomendasi Kuliner Unila", font=("Arial", 16, "bold")).pack(pady=10)
        
        # Tombol simulasi untuk testing awal
        tk.Button(root, text="Cek Koneksi Sistem", command=self.cek_sistem, bg="lightgreen").pack(pady=20)

    def cek_sistem(self):
        messagebox.showinfo("Berhasil", "Pondasi aplikasi dari Ketua berhasil berjalan!")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiRekomendasiAnakKost(root)
    root.mainloop()
