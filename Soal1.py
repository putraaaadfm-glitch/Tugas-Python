
# 1. Fungsi Non-Void untuk menghitung nilai akhir
def hitung_nilai_akhir(tugas, uts, uas):
    akhir = (0.30 * tugas) + (0.30 * uts) + (0.40 * uas)
    return akhir


# 2. Fungsi Non-Void untuk menentukan nilai huruf
def tentukan_huruf(nilai_akhir):
    if nilai_akhir >= 85:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 55:
        return "C"
    elif nilai_akhir >= 40:
        return "D"
    else:
        return "E"


# 3. Fungsi Non-Void untuk menentukan status kelulusan
def tentukan_status(huruf):
    if huruf == "A" or huruf == "B" or huruf == "C":
        return "Lulus"
    else:
        return "Tidak Lulus"


# 4. Fungsi Void untuk mencetak baris data mahasiswa
def cetak_baris(nama, akhir, huruf, status):
    print(f"{nama:<10} {akhir:<13.1f} {huruf:<13} {status:<15}")


# Fungsi Utama (Main)
def main():

    # Header Tabel
    print("-" * 55)
    print(f"{'Nama':<10} {'Nilai Akhir':<13} {'Nilai Huruf':<13} {'Keterangan':<15}")
    print("-" * 55)

    # Variabel penghitung akumulasi nilai dan kelulusan
    total_nilai_kelas = 0
    jumlah_lulus = 0

    # --- 1. MAHASISWA: ANDI ---
    na_andi = hitung_nilai_akhir(80, 70, 90)
    nh_andi = tentukan_huruf(na_andi)
    st_andi = tentukan_status(nh_andi)
    cetak_baris("Andi", na_andi, nh_andi, st_andi)
    total_nilai_kelas += na_andi
    if st_andi == "Lulus":
        jumlah_lulus += 1

    # --- 2. MAHASISWA: BUNGA ---
    na_bunga = hitung_nilai_akhir(90, 85, 88)
    nh_bunga = tentukan_huruf(na_bunga)
    st_bunga = tentukan_status(nh_bunga)
    cetak_baris("Bunga", na_bunga, nh_bunga, st_bunga)
    total_nilai_kelas += na_bunga
    if st_bunga == "Lulus":
        jumlah_lulus += 1

    # --- 3. MAHASISWA: CITRA ---
    na_citra = hitung_nilai_akhir(60, 45, 50)
    nh_citra = tentukan_huruf(na_citra)
    st_citra = tentukan_status(nh_citra)
    cetak_baris("Citra", na_citra, nh_citra, st_citra)
    total_nilai_kelas += na_citra
    if st_citra == "Lulus":
        jumlah_lulus += 1

    # --- 4. MAHASISWA: DIMAS ---
    na_dimas = hitung_nilai_akhir(75, 80, 65)
    nh_dimas = tentukan_huruf(na_dimas)
    st_dimas = tentukan_status(nh_dimas)
    cetak_baris("Dimas", na_dimas, nh_dimas, st_dimas)
    total_nilai_kelas += na_dimas
    if st_dimas == "Lulus":
        jumlah_lulus += 1

    # --- 5. MAHASISWA: EKA ---
    na_eka = hitung_nilai_akhir(30, 40, 35)
    nh_eka = tentukan_huruf(na_eka)
    st_eka = tentukan_status(nh_eka)
    cetak_baris("Eka", na_eka, nh_eka, st_eka)
    total_nilai_kelas += na_eka
    if st_eka == "Lulus":
        jumlah_lulus += 1

    print("-" * 55)

    # Menghitung rata-rata nilai kelas
    rata_rata = total_nilai_kelas / 5

    # Menampilkan ringkasan akhir kelas
    print(f"Rata-rata Nilai Akhir Kelas : {rata_rata:.2f}")
    print(f"Banyaknya Mahasiswa Lulus  : {jumlah_lulus}")


# Menjalankan program
main()
