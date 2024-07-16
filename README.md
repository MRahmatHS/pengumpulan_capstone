Nama : M.Rahmat Hidayat Syachrudin
StudentID: JCDS2504005
ClassCode : JCDS - 2504

# Program Manajemen Inventaris Obat PBF [PEDAGANG BESAR FARMASI] PT. PURWA

Program ini adalah sistem manajemen inventaris untuk PBF [PEDAGANG BESAR FARMASI] PT. PURWA, yang memungkinkan pengguna untuk menambahkan, memperbarui, menghapus, dan menjual item obat dalam inventaris. Program ini diperuntukan untuk admin/APJ (apoteker penanggung jawab) serta petugas TTK (tenagakerja teknis kefarmasian) dalam mengatur inventaris produk yg di jual di PBF.

## Fitur
1. **Menampilkan Inventaris Obat**
   - Lihat semua item dalam inventaris.
   - Lihat item berdasarkan nomor batch.
   - Lihat item berdasarkan zat aktif.
2. **Tambah Item**
   - Tambah item baru ke inventaris dengan detail lengkap.
3. **Perbarui Item**
   - Perbarui stok atau harga satuan item yang sudah ada dalam inventaris.
4. **Hapus Item**
   - Hapus item dari inventaris berdasarkan nomor batch.
5. **Jual Item**
   - Jual item dari inventaris dengan memasukkan nomor batch dan jumlah yang akan dijual.
6. **Keluar**
   - Keluar dari program.

## Struktur Program

- **`tampilkan_menu`**: Menampilkan menu utama.
- **`showItemMenu`**: Menampilkan submenu untuk menampilkan inventaris.
- **`createItemMenu`**: Menampilkan submenu untuk menambah item.
- **`updateItemMenu`**: Menampilkan submenu untuk memperbarui item.
- **`Sub_updateItemMenu`**: Menampilkan submenu untuk memilih detail item yang ingin diperbarui.
- **`deleteItemMenu`**: Menampilkan submenu untuk menghapus item.
- **`sellItemMenu`**: Menampilkan submenu untuk menjual item.
- **`exitMenu`**: Menampilkan pesan keluar.
- **`batch_duplikat`**: Menampilkan pesan jika nomor batch duplikat.
- **`validasi_input_batch`**: Validasi input nomor batch.
- **`validasi_input_int`**: Validasi input integer.
- **`validasi_input_tanggal`**: Validasi input tanggal.
- **`tampilkan_tabel_item`**: Menampilkan tabel item baru.
- **`validate_iya_tidak`**: Validasi input 'ya' atau 'tidak'.
- **`tabel_inventaris`**: Menampilkan tabel inventaris.
- **`tampilkan_inventaris`**: Fungsi utama untuk menampilkan inventaris.
- **`tambah_item`**: Fungsi utama untuk menambah item.
- **`tampilkan_tabel_perbarui_item`**: Menampilkan tabel detail item yang akan diperbarui.
- **`konfirmasi_update_items`**: Konfirmasi perubahan item.
- **`perbarui_item`**: Fungsi utama untuk memperbarui item.
- **`hapus_item`**: Fungsi utama untuk menghapus item.
- **`tampilkan_tabel_penjualan`**: Menampilkan tabel detail item yang akan dijual.
- **`jual_item`**: Fungsi utama untuk menjual item.
- **`main`**: Fungsi utama untuk menjalankan program.

## Cara Penggunaan
1. **Menjalankan Program**
   - Jalankan program dengan menjalankan `main` function.
2. **Menampilkan Inventaris**
   - Pilih opsi 1 pada menu utama untuk melihat inventaris obat.
   - Pilih submenu sesuai kebutuhan untuk melihat semua item, berdasarkan nomor batch, atau zat aktif.
3. **Tambah Item**
   - Pilih opsi 2 pada menu utama untuk menambah item baru ke inventaris.
   - Masukkan detail item sesuai prompt yang diberikan.
4. **Perbarui Item**
   - Pilih opsi 3 pada menu utama untuk memperbarui item yang ada dalam inventaris.
   - Masukkan nomor batch item yang ingin diperbarui, kemudian pilih detail yang ingin diubah (stok atau harga satuan).
5. **Hapus Item**
   - Pilih opsi 4 pada menu utama untuk menghapus item dari inventaris.
   - Masukkan nomor batch item yang ingin dihapus.
6. **Jual Item**
   - Pilih opsi 5 pada menu utama untuk menjual item dari inventaris.
   - Masukkan nomor batch dan jumlah item yang akan dijual.
7. **Keluar dari Program**
   - Pilih opsi 6 pada menu utama untuk keluar dari program.

Program ini menggunakan modul `PrettyTable` untuk menampilkan tabel dengan rapi. 

