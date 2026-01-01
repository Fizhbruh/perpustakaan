import os 
import csv
daftar_peminjaman = []

riwayat = []

daftar = [
    ["BK001", "Funiculi Funicula"],
    ["BK002", "Seporsi Mie Ayam Sebelum Mati"],
    ["BK003", "Cara Membuat Web"]
]

daftar_member = [
    ["AG001", "Hafizh Febrian Wicaksono", "081214312092"],
    ["AG002", "Daniel Afandi", "081217616862"],
    ["AG003", "Raehan Tegar Setiawan", "085123563298"]
]

def tambah_member():
    while True:
        print("\n=== TAMBAH MEMBER ===")
        kode = input("Masukkan kode member  : ")
        nama = input("Masukkan nama member : ")
        no = int(input("Masukkan nomor telpon     : "))

        daftar_member.append([kode, nama, no])
        print("\n Member berhasil ditambahkan!")
        menambahkan= input("ingin menambahkan lagi?(YA/NO) :").upper()
        if menambahkan == "YA":
            continue
        else:
            main_menu()

def data_anggota():
    data = daftar_member
    print("=== DAFTAR BUKU ===")
    print(f"{'Kode member':<20}{'nama member':<30}{'no telpon':<10}")
    print("-" * 40)
    for kode, nama, no_telp in data:
        print(f"{kode:<20}{nama:<30}{no_telp:<10}")
    print()
    lanjut= input("apakah ingin menambah member?(YA/NO) :").upper()
    if lanjut == "YA":
        tambah_member()
    else:
        main_menu()
  
def peminjaman():
    while True:
        from datetime import datetime, timedelta
        data1 = daftar_member
        data2 = daftar
        member = input("Masukkan Kode member: ").upper()
        for kode, nama, notelp in data1:
            if kode == member:
                kode
                nama
                notelp
                break
        if member ==  kode:
            print("===== Biodata Peminjam =====")
            print("Kode Member :", kode)
            print("Nama Member :", nama)
            print("No Telp     :", notelp)
        else:
            print("Kode member tidak tersedia! Silakan input ulang / mendaftar member.")
            main_menu()
            break
        buku = input("Masukan Kode buku:").upper()
        for kode_buku, judul in data2:
            if kode_buku == buku:
                kode_buku
                judul
                break
        if buku == kode_buku:
            print("===== Keterangan Buku Yang Dipinjam =====")
            print("Kode buku :", kode_buku)
            print("Judul buku :", judul)
        else:
            print("Buku tidak tersedia! Silakan input ulang!")
        sekarang = datetime.now().date()
        tgl_pinjam = sekarang
        print("Tanggal pinjam :", tgl_pinjam)
        tgl_kembali = sekarang + timedelta(days=7)
        print("Tanggal harus kembali :", tgl_kembali)
        print("Peminjaman berhasil")
        daftar_peminjaman.append([kode, nama,kode_buku, judul, tgl_kembali])
        main_menu()

def pengembalian():
    import datetime
    no_anggota = input("Kode member : ").upper()
    kode_buku = input("Kode buku   : ").upper()
    data_ditemukan = None
    for data in daftar_peminjaman:
        kode, nama, kode_buku1, judul, tgl_kembali = data
        if no_anggota == kode and kode_buku == kode_buku1:
            data_ditemukan = data
            break
    if data_ditemukan is None:
        print("Peminjaman tidak ditemukan!")
        main_menu()
        return
    print("Peminjaman ditemukan!")
    print("Nama :", nama)
    print("Judul Buku :", judul)
    tgl_input = input("Masukan tanggal dikembalikan (dd-mm-yyyy): ")
    tgl_pengembalian = datetime.datetime.strptime(tgl_input, "%d-%m-%Y").date()

    selisih = (tgl_pengembalian - tgl_kembali).days
    print(selisih)
    terlambat = selisih if selisih > 0 else 0
    harga = 20000
    denda = terlambat * 10000
    total = harga + denda

    print("=" * 40)
    print("Terlambat :", terlambat, "hari")
    print("Harga     :", harga)
    print("Denda     :", denda)
    print("Total     :", total)
    riwayat.append([kode,nama,kode_buku1,judul,tgl_pengembalian,denda,total])
    daftar_peminjaman.remove(data_ditemukan)
    print("Buku berhasil dikembalikan")
    with open("riwayat_perpus.csv", "a", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([
            "Kode Anggota",
            "Nama",
            "Kode Buku",
            "Judul",
            "Tanggal Dikembalikan",
            "Denda",
            "Total"
        ])
        for kode, nama, kode_buku, judul, tgl_kembali, denda, total in riwayat:
            if hasattr(tgl_kembali, "strftime"):
                tgl = tgl_kembali.strftime("%d-%m-%Y")
            else:
                tgl = tgl_kembali

            writer.writerow([
                kode,
                nama,
                kode_buku,
                judul,
                tgl,
                denda,
                total
            ])

    print("\nLaporan CSV berhasil disimpan ke 'riwayat_perpus.csv'")
    os.startfile("riwayat_perpus.csv")
    main_menu()

def tambah_buku():
    while True:
        print("\n=== TAMBAH BUKU ===")
        kode = input("Masukkan kode buku  : ")
        judul = input("Masukkan judul buku : ")
        daftar.append([kode, judul])
        print("\n Buku berhasil ditambahkan!")
        menambahkan= input("ingin menambahkan lagi?(YA/NO) :").upper()
        if menambahkan == "YA":
            continue
        else:
            main_menu()

def tampilkan_riwayat():
    print("\n=== RIWAYAT PEMINJAMAN ===")
    print("-" * 131)
    print(f"{'Kode Anggota':<15}{'Nama Peminjam':<30}{'Kode Buku':<15}{'Judul Buku':<30}{'Tgl Dikembalikan':<18}{'Denda':<12}{'Total Biaya':<12}")
    print("-" * 131)
    for kode, nama, kode_buku, judul, tgl_kembali, denda, total in riwayat:
        if hasattr(tgl_kembali, "strftime"):
            tgl = tgl_kembali.strftime('%d-%m-%Y')
        else:
            tgl = str(tgl_kembali)
        print(f"{kode:<15}{nama:<30}{kode_buku:<15}{judul:<30}{tgl:<18}{denda:<12,.0f}{total:<12,.0f}")
    main_menu()

def tampilkan_buku():
    data = daftar
    print("=== DAFTAR BUKU ===")
    print(f"{'Kode':<8}{'Judul Buku':<30}")
    print("-" * 40)
    for kode, judul in data:
        print(f"{kode:<8}{judul:<30}")
    print()
    lanjut= input("apakah ingin menambah buku?(YA/NO) :").upper()
    if lanjut == "YA":
        tambah_buku()
    else:
        main_menu()

def tampilkan_peminjaman():
    print("=== DAFTAR PEMINJAMAN AKTIF ===")
    print(f"{'Kode Anggota':<15}{'Nama':<30}{'Kode Buku':<15}{'Judul Buku':<25}{'Tenggat'}")
    print("-" * 95)
    for kode, nama, kode_buku, judul, waktu in daftar_peminjaman:
        print(f"{kode:<15}{nama:<30}{kode_buku:<15}{judul:<25}{waktu.strftime('%d-%m-%Y')}")
    print()
    main_menu()

def main_menu():
    print("="*40)
    print("1. daftar buku")
    print("2. data anggota") 
    print("3. peminjaman")
    print("4. daftar peminjaman")
    print("5. pengembalian")
    print("6. riwayat peminjaman")
    print("7. exit")
    print("choice : [1/2/3/4/exit] :")

    pilihan= input("your choice:")

    if pilihan == "1":
        print("="*40)
        print("daftar buku")
        print("="*40)
        tampilkan_buku()
    elif pilihan == "2":
        print("="*40)
        print("pendataan anggota")
        print("="*40)
        data_anggota()
    elif pilihan == "3":
        peminjaman()
    elif pilihan == "4":
        tampilkan_peminjaman()
    elif pilihan == "5":
        pengembalian()
    elif pilihan == "6":
        tampilkan_riwayat()
    else:
        print("exit")
        get_login()

def get_login():
    while True:
        print("="*40)
        print("login admin perpustakaan")
        print("="*40)
        username = input("username :")
        password = input("password :")

        if username == "admin" and password == "12345":
            print("loading...\n\n")
            print("="*40)
            print("welcome to libarary!!!")
            main_menu()
            break
        else:
            print("login failed, please try again...")
            continue
get_login()