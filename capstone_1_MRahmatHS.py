from prettytable import PrettyTable
import datetime 

inventaris = [
    {"nama": "Paracetamol 500 mg Tablet", 
     "nomor_batch": "pct0802", 
     "zat_aktif": "paracetamol", 
     "pabrik": "PT. MersiPharma", 
     "stok": 1000, 
     "harga": 500,
     "expired_date": '2026-08-02'},
     
    {"nama": "Proris 400 mg Tablet", 
     "nomor_batch": "prot0902", 
     "zat_aktif": "ibuprofen", 
     "pabrik": "PT. Pharos", 
     "stok": 1000, 
     "harga": 4000,
     "expired_date": '2026-09-02'},

    {"nama": "Nexium 40 mg Tablet", 
     "nomor_batch": "nex4090", 
     "zat_aktif": "esomeprazole", 
     "pabrik": "PT. AstraZeneca", 
     "stok": 336, 
     "harga": 60000,
     "expired_date": '2029-11-12'},

    {"nama": "Proris 100 mg/5 ml Suspensi 60 ml", 
     "nomor_batch": "pros0902", 
     "zat_aktif": "ibuprofen", 
     "pabrik": "PT. Pharos", 
     "stok": 60, 
     "harga": 20000,
     "expired_date": '2026-09-02'},

    {"nama": "Ibuprofen 200 mg Tablet", 
     "nomor_batch": "ibdex0210", 
     "zat_aktif": "ibuprofen", 
     "pabrik": "PT. DexaMedica", 
     "stok": 500, 
     "harga": 2000,
     "expired_date": '2026-10-02'},

    {"nama": "Aspirin 80 mg Tablet", 
     "nomor_batch": "asb0208", 
     "zat_aktif": "aspirin", 
     "pabrik": "PT.Bayer", 
     "stok": 200, 
     "harga": 10000,
     "expired_date": '2026-08-02'}
]

def tampilkan_menu():
    print('''
================= PBF PT. PURWA ======================
                      
Silahkan pilih menu:
1. Menampilkan Inventaris Obat
2. Tambah Item 
3. Perbarui Item
4. Hapus Item
5. Jual Item
6. Keluar
======================================================
    ''')

def showItemMenu ():
    print('''
====== Submenu Menampilkan Inventaris Obat ===========
                      
Silahkan pilih submenu:
1. Lihat Semua Inventaris
2. Lihat Item Berdasarkan Nomor Batch
3. Lihat Item Berdasarkan Zat Aktif
4. Kembali ke Menu Sebelumnya
======================================================
        ''')

def createItemMenu (): 
    print('''
============== Submenu Tambah Item ===================
                      
Silahkan pilih submenu:
1. Tambah Item Baru
2. Kembali ke Menu Sebelumnya
======================================================
        ''')
    
def updateItemMenu ():
    print('''
============== Submenu Perbarui Item =================
                      
Silahkan pilih submenu:
1. Perbarui Detail Item
2. Kembali ke Menu Sebelumnya
======================================================
        ''')

def Sub_updateItemMenu ():
    print('''
======== Pilih Detail yang Ingin Diperbarui ==========
1. Stok
2. Harga Satuan
3. Kembali ke Menu Sebelumnya
======================================================
                            ''')
    
def deleteItemMenu ():
    print('''
============== Submenu Hapus Item ====================
                      
Silahkan pilih submenu:
1. Hapus Item
2. Kembali ke Menu Sebelumnya
======================================================
        ''')

def sellItemMenu ():  
    print('''
============== Submenu Jual Item =====================
                      
Silahkan pilih submenu:
1. Jual Item
2. Kembali ke Menu Sebelumnya
======================================================
        ''')
    
def exitMenu ():
    print('''
======================================================
             KELUAR DARI PROGRAM
                PBF PT. PURWA
                TERIMAKASIH 
======================================================
                  ''') 
    
def batch_duplikat():
    print('''
======================================================
        Nomor batch sudah ada di Inventaris
    Pastikan Nomor Batch sama dengan di Fisik Produk
        yang ingin ditambahkan ke Inventaris 
======================================================
          ''')

def validasi_input_batch(batch_item_baru, inventaris): # Fungsi memeriksa apakah nomor batch yang dimasukkan sudah ada di dalam inventaris atau tidak.
    while True:
        try:
            nomor_batch = input(batch_item_baru).strip().lower()
            batch_ada = False
            for item in inventaris:
                if item['nomor_batch'].lower() == nomor_batch:
                    batch_ada = True
                    batch_duplikat()
                    return None  # Kembali ke submenu jika batch ada yang sama
            if not batch_ada:
                return nomor_batch  # Nomor batch valid, kembalikan nomor batch
        except Exception as e:
            print(f"Terjadi kesalahan: {e}. Silakan coba lagi.")
          
def validasi_input_int(nilai_yg_di_input):
    while True:
        try:
            nilai = int(input(nilai_yg_di_input))
            if nilai <= 0:
                print("Nilai tidak boleh negatif/kosong. Harap masukkan nilai yang Benar.")
            else:
                return nilai
        except ValueError:
            print("Input tidak valid.") # Jika input bukan integer, minta input ulang

def validasi_input_tanggal(tanggal): 
    while True:
        try:
            date_input = input(tanggal)
            date_obj = datetime.datetime.strptime(date_input, "%Y%m%d")
            return date_obj.date()
        except ValueError:
            print("Format tanggal tidak valid. Gunakan format YYYYMMDD.")

def tampilkan_tabel_item(nama, nomor_batch, zat_aktif, pabrik, stok, harga, expired_date):
    tabel = PrettyTable()
    tabel.field_names = ["Nama", "Nomor Batch", "Zat Aktif", "Pabrik", "Stok", "Harga Satuan","Expired Date (YYYY/MM/DD)"]
    tabel.add_row([nama, nomor_batch, zat_aktif, pabrik, stok, harga, expired_date])
    print("\nDetail item baru:")
    print(tabel)

def validate_iya_tidak(prompt): # Fungsi untuk memvalidasi input 'ya' atau 'tidak'.
    while True:
        konfirmasi = input(prompt).strip().lower()
        if konfirmasi in ['ya', 'tidak']:
            return konfirmasi
        else:
            print('''
===Input tidak valid. Harap masukkan 'ya' atau 'tidak'===
                  ''')

def tabel_inventaris():
    for i in range(len(inventaris) - 1):
        for j in range(i + 1, len(inventaris)):
            if inventaris[i]['nama'].lower() > inventaris[j]['nama'].lower():
                inventaris[i], inventaris[j] = inventaris[j], inventaris[i]
            
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama", "Nomor Batch", "Zat Aktif", "Pabrik", "Stok", "Harga Satuan", "Expired Date (YYYY/MM/DD)"]
    for idx in range(len(inventaris)):
        item = inventaris[idx]
        tabel.add_row([idx + 1, item['nama'], item['nomor_batch'], item['zat_aktif'],
                        item['pabrik'], item['stok'], item['harga'], item['expired_date']])
    print("\nInventaris Saat Ini:")
    print(tabel)

def tampilkan_inventaris():
    while True:
        showItemMenu()
        pilihan = input("Masukkan Angka Submenu yang ingin dijalankan: ")
        if pilihan == '1':
            if inventaris:
                tabel_inventaris()
            else:
                print("Pemberitahuan: Inventaris tidak tersedia") 
        elif pilihan == '2':
            nomor_batch = input("Masukkan Nomor Batch item yang ingin dilihat: ").strip().lower() #strip dan lower untuk menghandle jika spasi lebih dan kapital
            tabel = PrettyTable()
            tabel.field_names = ["No", "Nama", "Nomor Batch", "Zat Aktif", "Pabrik", "Stok", "Harga Satuan","Expired Date (YYYY/MM/DD)"]
            for idx in range(len(inventaris)):
                item = inventaris[idx]
                if item['nomor_batch'].lower() == nomor_batch:
                    tabel.add_row([idx + 1, item['nama'], item['nomor_batch'],
                                   item['zat_aktif'], item['pabrik'], item['stok'], item['harga'], item['expired_date']])
            if tabel._rows:
                print("\nDetail Item:")
                print(tabel)
            else:
                print(f"Item dengan nomor batch {nomor_batch} tidak ditemukan.")
        elif pilihan == '3':
            zat_aktif = input("Masukkan Zat Aktif item yang ingin dilihat: ").strip().lower() 
            tabel = PrettyTable()
            tabel.field_names = ["No", "Nama", "Nomor Batch", "Zat Aktif", "Pabrik", "Stok", "Harga Satuan","Expired Date (YYYY/MM/DD)"]
            for idx in range(len(inventaris)):
                item = inventaris[idx]
                if item['zat_aktif'].lower() == zat_aktif:
                    tabel.add_row([idx + 1, item['nama'], item['nomor_batch'],
                                   item['zat_aktif'], item['pabrik'], item['stok'], item['harga'], item['expired_date']])
            if tabel._rows:
                print("\nDetail Item:")
                print(tabel)
            else:
                print(f"Zat Aktif {zat_aktif} tidak ditemukan.")
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def tambah_item():
    while True:
        createItemMenu()
        pilihan = input("Masukkan Angka Submenu yang ingin dijalankan: ")
        if pilihan == '1':
            nomor_batch = validasi_input_batch("Masukkan nomor batch: ", inventaris)
            if nomor_batch is None:
                return
            nama = input("Masukkan nama item: ").strip()
            zat_aktif = input("Masukkan zat aktif: ").strip()
            pabrik = input("Masukkan pabrik: ").strip()
            stok = validasi_input_int("Masukkan jumlah stok: ")
            harga = validasi_input_int("Masukkan harga satuan item: ")
            expired_date = validasi_input_tanggal("Masukkan Expired Date (YYYYMMDD): ").strftime("%Y-%m-%d") 

            tampilkan_tabel_item(nama, nomor_batch, zat_aktif, pabrik, stok, harga, expired_date)
            konfirmasi = validate_iya_tidak("Apakah detail ini benar? (ya/tidak): ")
            if konfirmasi == 'ya':
                inventaris.append({"nama": nama, "nomor_batch": nomor_batch, "zat_aktif": zat_aktif,
                                    "pabrik": pabrik, "stok": stok, "harga": harga, "expired_date": expired_date})
                print(f"Item {nama} berhasil ditambahkan.")
            else:
                print("Penambahan dibatalkan.")
        elif pilihan == '2':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def tampilkan_tabel_perbarui_item(item):
    tabel = PrettyTable()
    tabel.field_names = ["Nama", "Nomor Batch", "Zat Aktif", "Pabrik", "Stok", "Harga Satuan", "Expired Date"]
    tabel.add_row([item['nama'], item['nomor_batch'], item['zat_aktif'], item['pabrik'], item['stok'], item['harga'], item['expired_date']])
    print("\nDetail item saat ini:")
    print(tabel)

def konfirmasi_update_items (perubahan, item): # konfirmasi perubahan di dalam items
    konfirmasi = validate_iya_tidak("Apakah ini item yang ingin diperbarui? (ya/tidak): ")

    if konfirmasi == 'ya':
        for _key, _value in perubahan.items(): # _key untuk menyatakan key yg akan di ubah // _values menyatakan values yang dirubah untuk update items
            item[_key] = _value
        print("Perubahan telah disimpan.")
    elif konfirmasi == 'tidak':
        print("Pembaruan dibatalkan.")
    else:
        print("Pilihan tidak valid.")

def perbarui_item():
    while True:
        updateItemMenu()
        pilihan = input("Masukkan Angka Submenu yang ingin dijalankan: ")
        if pilihan == '1':
            tabel_inventaris()
            nomor_batch = input("Masukkan nomor batch item yang akan diperbarui: ").strip().lower()
            for item in inventaris:
                if item['nomor_batch'].lower() == nomor_batch:
                    tampilkan_tabel_perbarui_item(item)
                    konfirmasi = validate_iya_tidak("Apakah ini item yang ingin diperbarui? (ya/tidak): ")
                    if konfirmasi == 'ya':
                        perubahan = {}
                        while True:
                            Sub_updateItemMenu()
                            sub_pilihan = input("Masukkan Angka Submenu yang ingin dijalankan: ")
                            if  sub_pilihan == '1':
                                perubahan["stok"] = validasi_input_int("Masukkan jumlah stok baru: ")
                                konfirmasi_update_items(perubahan, item)
                            elif sub_pilihan == '2':
                                perubahan["harga"] = validasi_input_int("Masukkan Harga Satuan baru: ")
                                konfirmasi_update_items(perubahan, item)
                            elif sub_pilihan == '3':
                                break
                            else:
                                print("Pilihan tidak valid. Silakan coba lagi.")
                    else:
                        print("Pembaruan dibatalkan.")
                    return
            print(f"Item dengan nomor batch {nomor_batch} tidak ditemukan.")
        elif pilihan == '2':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def hapus_item():
    while True:
        deleteItemMenu()
        pilihan = input("Masukkan Angka Submenu yang ingin dijalankan: ")
        if pilihan == '1':
            tabel_inventaris()
            nomor_batch = input("Masukkan nomor batch item yang akan dihapus: ").strip().lower()
            for item in inventaris:
                if item['nomor_batch'].lower() == nomor_batch:
                    tampilkan_tabel_perbarui_item(item)
                    konfirmasi = validate_iya_tidak("Apakah ini item yang ingin dihapus? (ya/tidak): ")
                    if konfirmasi == 'ya':
                        inventaris.remove(item)
                        print(f"Item dengan nomor batch {nomor_batch} berhasil dihapus.")
                    else:
                        print("Penghapusan dibatalkan.")
                    return
            print(f"Item dengan nomor batch {nomor_batch} tidak ditemukan.")
        elif pilihan == '2':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def tampilkan_tabel_penjualan(item_jual):
    tabel = PrettyTable()
    tabel.field_names = ["Nama", "Nomor Batch", "Jumlah", "Harga Satuan", "Total Harga"]
    total_penjualan = 0
    for item in item_jual:
        total_harga = item['jumlah'] * item['harga']
        tabel.add_row([item['nama'], item['nomor_batch'], item['jumlah'], item['harga'], total_harga])
        total_penjualan += total_harga
    print("\nDetail Item yang akan dijual:")
    print(tabel)
    print(f"Total Penjualan: {total_penjualan}")

def jual_item():
    item_jual = []
    while True:
        sellItemMenu()
        pilihan = input("Masukkan Angka Submenu yang ingin dijalankan: ")
        if pilihan == '1':
            tabel_inventaris()
            while True:
                batch_item = input("Masukkan Batch item yang akan dijual: ").strip().lower()
                item_ditemukan = False
                for item in inventaris:
                    if item['nomor_batch'].lower() == batch_item:
                        item_ditemukan = True
                        stok_awal = item['stok']  # Catat stok awal
                        while True:
                            jumlah = validasi_input_int("Masukkan jumlah yang akan dijual: ")
                            if stok_awal >= jumlah:
                                stok_awal -= jumlah
                                item_jual.append({
                                    'nama': item['nama'],
                                    'nomor_batch': item['nomor_batch'],
                                    'jumlah': jumlah,
                                    'harga': item['harga']
                                })
                                print(f"Berhasil menambahkan {jumlah} dari {batch_item} ke daftar penjualan. Stok sementara {item['nama']} saat ini: {stok_awal}")
                                lagi = validate_iya_tidak("Apakah Anda ingin menjual item lain? (ya/tidak): ")
                                if lagi == 'tidak':
                                    tampilkan_tabel_penjualan(item_jual)
                                    konfirmasi = validate_iya_tidak("Apakah detail penjualan sudah benar? (ya/tidak): ")
                                    if konfirmasi == 'ya':
                                        # Jika konfirmasi penjualan, baru update stok inventaris
                                        for jual in item_jual: 
                                            for item in inventaris:
                                                if item['nomor_batch'] == jual['nomor_batch']:
                                                    item['stok'] -= jual['jumlah']
                                        print("Penjualan berhasil dilakukan.")
                                        return
                                    else:
                                        print("Penjualan dibatalkan.")
                                        return
                                break
                            else:
                                print(f"Stok tidak mencukupi untuk menjual {jumlah} dari {batch_item}. Stok sementara {item['nama']} saat ini: {stok_awal}")
                                ulang = validate_iya_tidak("Apakah Anda ingin menginput jumlah yang lain? (ya/tidak): ")
                                if ulang == 'tidak':
                                    break
                        break
                if not item_ditemukan:
                    print(f"Item {batch_item} tidak ditemukan.\nPastikan Nomor Batch benar")
                    ulang = validate_iya_tidak("Apakah Anda ingin mencoba lagi? (ya/tidak): ")
                    if ulang == 'tidak':
                        break
        elif pilihan == '2':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Masukkan Angka Menu yang ingin dijalankan: ")
        if pilihan == '1':
            tampilkan_inventaris()
        elif pilihan == '2':
            tambah_item()
        elif pilihan == '3':
            perbarui_item()
        elif pilihan == '4':
            hapus_item()
        elif pilihan == '5':
            jual_item()
        elif pilihan == '6':
            exitMenu ()   
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
