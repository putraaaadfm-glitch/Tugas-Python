# RANCANGAN FUNGSI

def hitung_biaya_berat(berat):
    """menghitung biaya berdasarkan berat paket (Fungsi non-void)"""
    if berat <= 2:
        return 10000
    else:
        return 10000 + (berat - 2) * 4000

def hitung_biaya_jarak(jarak):
    """menghitung biaya berdasarkan jarak paket (Fungsi non-void)"""
    if jarak <= 20:
        return 0
    else:
        return 5000
    
def hitung_potongan(total_biaya, status_anggota):
    """menghitung potongan harga jika pelanggan adalah member (Fungsi non-void)"""
    if status_anggota.lower() == "ya":
        return int(total_biaya * 0.10)
    return 0

def cetak_struk_dan_hitung_total(daftar_pesanan):
    """mencetak struk untuk setiap pelanggan dan menghitung total pendapatan (Fungsi void)"""
    total_pendapatan_hari_ini = 0

    print("-" * 60)
    print(f"{'Struk Pengiriman Toko Daring':^60}")
    print("=" * 60)

    for pesanan in daftar_pesanan:
        nama = pesanan['nama']
        berat = pesanan['berat']
        jarak = pesanan['jarak']
        anggota = pesanan['anggota']

        # memanggil fungsi untuk menghitung biaya

        biaya_berat = hitung_biaya_berat(berat)
        biaya_jarak = hitung_biaya_jarak(jarak)
        total_biaya = biaya_berat + biaya_jarak
        potongan = hitung_potongan(total_biaya, anggota)
        ongkir_bayar = total_biaya - potongan

        # akumulasi total pendapatan hari ini
        total_pendapatan_hari_ini += ongkir_bayar

        # cetak struk untuk setiap pelanggan

        print(f"Nama Pelanggan: {nama}")
        print(f"Berat Paket: {berat} kg | {jarak} km | Anggota: {anggota}")
        print(f"Biaya Berat: Rp {biaya_berat:,}")
        print(f"Biaya Jarak: Rp {biaya_jarak:,}")
        if potongan > 0:
            print(f"Potongan Harga (10%): -Rp {potongan:,}")
        print(f"Ongkos Kirim: Rp {ongkir_bayar:,}")
        print("-" * 60)

    print(f"Total Pendapatan Ongkir Hari Ini ; Rp {total_pendapatan_hari_ini:,}")
    print("=" * 60)

# DATA INPUT

data_pesanan = [
    {"nama": "Rina", "berat": 1, "jarak": 10, "anggota": "tidak"},
    {"nama": "Sari", "berat": 5, "jarak": 25, "anggota": "tidak"},
    {"nama": "Tono", "berat": 5, "jarak": 25, "anggota": "ya"},
    {"nama": "Umar", "berat": 2, "jarak": 30, "anggota": "ya"},
    {"nama": "Vina", "berat": 8, "jarak": 15, "anggota": "tidak"}
]

# menjalankan program utama

if __name__ == "__main__":
    cetak_struk_dan_hitung_total(data_pesanan)