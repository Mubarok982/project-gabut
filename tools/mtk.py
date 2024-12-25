import main 
def start():
    def hitung_kecepatan():
        print("Hitung Kecepatan Ready!")
        jarak = int(input("Masukan jarak: "))
        waktu = int(input("Masukan waktu: "))
        kecepatan = jarak * waktu
        print("Kecepatan: ", kecepatan, "\n")


    def luas_segitiga():
        print("Hitung Segitiga Ready!")
        alas = int(input("Masukan alas: "))
        tinggi = int(input("Masukan tinggi: "))
        luas  = 0.5 * (alas * tinggi)
        print("Luas Segitiga: ", luas, "\n")


    def luas_balok():
        print("Hitung Segitiga Ready!")
        panjang = int(input("Masukan panjang: "))
        lebar = int(input("Masukan lebar: "))
        tinggi = int(input("Masukan tinggi: "))
        luas = (2 * panjang * lebar) + (2 * panjang * tinggi) + (2 * lebar * tinggi)
        print("Luas Balok: ", luas, "\n")


    def luas_bola():
        print("Hitung Bola Ready!")
        r = float(input("Masukan jari-jari: "))
        luas = 4 * 3.14 * (r**2)
        print("Luas Bola: ", luas, "\n")

    def luas_persegi():
        print("Hitung Persegi Ready!")
        sisi = int(input("Masukan panjang sisi: "))
        luas = (sisi * 2)
        print("Luas Persegi: ", luas, "\n")

    def luas_persegi_panjang():
        print("Hitung Persegi Panjang Ready!")
        panjang_sisi  = int(input("Masukan panjang sisi: "))
        lebar_sisi = int(input("Masukan lebar sisi: "))
        luas = (panjang_sisi * lebar_sisi)
        print("Luas Persegi Panjang: ", luas, "\n")

    def luas_jajar_genjang():
        print("Hitung Jajar Genjang Ready!")
        alas  = int(input("Masukan panjang alas: "))
        tinggi = int(input("Masukan tinggi: "))
        luas = (alas * tinggi)
        print("Luas Jajar Genjang: ", luas, "\n")

    def luas_belah_ketupat():
        print("Hitung Belah Ketupat Ready!")
        Diagonal_1  = int(input("Masukan Diagonal 1: "))
        Diagonal_2 = int(input("Masukan Diagonal 2: "))
        luas =0.5 * (Diagonal_1 * Diagonal_2)
        print("Luas Belah ketupat: ", luas, "\n")

    def luas_layang_layang():
        print("Hitung Belah Ketupat Ready!")
        Diagonal_1  = int(input("Masukan Diagonal 1: "))
        Diagonal_2 = int(input("Masukan Diagonal 2: "))
        luas =0.5 * (Diagonal_1 * Diagonal_2)
        print("Luas Layang-layang: ", luas, "\n")

    def luas_Lingkaran():
        print("Hitung Lingkaran Ready!")
        r = int(input("Masukan Jari-jari: "))
        luas = 3.14 * (r**2)
        print("Luas Lingkaran: ", luas, "\n")


    def luas_Trapesium():
        print("Hitung Trapesium Ready!")
        a = int(input("Masukan a: "))
        b = int(input("Masukan b: "))
        tinggi = int(input("masukan tinggi: "))
        luas = 0.5 * (a * b) * tinggi
        print("Luas Trapesium: ", luas, "\n")

    def luas_setengah_Lingkaran():
        print("Hitung Setengah Lingkaran Ready!")
        r = int(input("Masukan Jari-jari: "))
        luas = 0.5 * 3.14 * (r**2)
        print("Luas Setengah Lingkaran: ", luas, "\n")

    def luas_Poligon_Reguler():
        print("Hitung Poligon Reguler Ready!")
        n = int(input("Masukan n: "))
        s = int(input("Masukan s: "))
        a = int(input("Masukan a: "))
        luas = 0.5 * n * s * a
        print("Luas Poligon Reguler: ", luas, "\n")

    #luas Bangun Tiga Dimensi
    def luas_Permukaan_Kubus():
        print("Hitung Permukaan Kubus Ready!")
        panjang_sisi = int(input("Masukan Panjang Sisi: "))
        luas = 6 * panjang_sisi
        print("Luas Permukaan Kubus: ", luas, "\n")

    def luas_Permukaan_Balok():
        print("Hitung Permukaan Balok Ready!")
        p = int(input("Masukan Panjang: "))
        l = int(input("Masukan Lebar: "))
        t = int(input("Masukan Tinggi: "))
        luas = 2 * (p * l) + (p * t) + (l * t)
        print("Luas Permukaan Balok: ", luas, "\n")

    def luas_Permukaan_prisma_segitiga():
        print("Hitung Permukaan Prisma Segitiga Ready!")
        L_alas = int(input("Masukan Luas Alas: "))
        K_alas = int(input("Masukan Keliling Alas: "))
        t = int(input("Masukan Tinggi: "))
        luas = (2 * L_alas) + (K_alas * t)
        print("Luas Permukaan Prisma Segitiga: ", luas, "\n")

    def luas_Permukaan_limas_segitiga():
        print("Hitung Permukaan Limas Segitiga Ready!")
        L_alas = int(input("Masukan Luas Alas: "))
        L_Segitiga = int(input("Masukan Luas Segitiga: "))
        luas = L_alas + (L_Segitiga * 3)
        print("Luas Permukaan limas Segitiga: ", luas, "\n")

    def luas_Permukaan_limas_segiempat():
        print("Hitung Permukaan Limas Segiempat Ready!")
        L_alas = int(input("Masukan Luas Alas: "))
        L_Segitiga = int(input("Masukan Luas Segitiga: "))
        luas = L_alas + (L_Segitiga * 4)
        print("Luas Permukaan limas Segiempat: ", luas, "\n")

    def luas_Permukaan_tabung():
        print("Hitung Permukaan Tabung Ready!")
        r = int(input("Masukan Jari-jari: "))
        tinggi = int(input("Masukan Tinggi: "))
        luas = 2 * 3.14 * r * (r * tinggi)
        print("Luas Permukaan Tabung: ", luas, "\n")

    def luas_Permukaan_kerucut():
        print("Hitung Permukaan Kerucut Ready!")
        r = int(input("Masukan Jari-jari: "))
        s = int(input("Masukan s: "))
        luas = 3.14 * r * (r + s)
        print("Luas Permukaan Kerucut: ", luas, "\n")

    def luas_permukaan_setengah_bola():
        print("Hitung Setengah Bola Ready!")
        r = float(input("Masukan jari-jari: "))
        luas = 3 * 3.14 * (r**2)
        print("Luas Setengah Bola: ", luas, "\n")


    def luas_permukaan_silinder_tanpa_tutup():
        print("Hitung Silinder Tanpa Tutup Ready!")
        r = float(input("Masukan Jari-Jari: "))
        t = float(input("Masukan Tinggi: "))
        luas = 3.14 * r * ((2 * r) + t)
        print("Luas Silinder Tanpa Tutup: ", luas, "\n")

    while True:
        userInput = int(input(
            "pilih rumus yang akan di pakai : \n\n1.Hitung Kecepatan"
                                            "\n2.Luas Segitiga"
                                            "\n3.Luas Balok"
                                            "\n4.Luas Bola"
                                            "\n5.Luas Persegi"
                                            "\n6.Luas Persegi Panjang"
                                            "\n7.Luas Jajar Genjang"
                                            "\n8.Luas Belah Ketupat"
                                            "\n9.Luas Layang-Layang"
                                            "\n10.Luas Lingkaran"
                                            "\n11.Luas Trapesium"
                                            "\n12.Luas Setengan Lingkaran"
                                            "\n13.Poligon Reguler"
                                            "\n14.Luas Permukaan Kubus"
                                            "\n15.Luas Permukaan Balok"
                                            "\n16.Luas Permukaan Prisma Segitiga"
                                            "\n17.Luas Permukaan Limas Segitiga"
                                            "\n18.Luas Permukaan Limas Segiempat"
                                            "\n19.Luas Permukaan Tabung"
                                            "\n20.Luas Permukaan Kerucut"
                                            "\n21.Luas Permukaan Setengah Bola"
                                            "\n22.Luas Permukaan Silinder Tanpa Tutup"
                                            "\n\n0.keluar"
                                            "\n\npilih nomer barapa: "))

        if(userInput == 1):
            hitung_kecepatan()
        elif(userInput == 2):
            luas_segitiga()
        elif (userInput == 3):
            luas_balok()
        elif (userInput == 4):
            luas_bola()
        elif (userInput == 5):
            luas_persegi()
        elif (userInput == 6):
            luas_persegi_panjang()
        elif (userInput == 7):
            luas_jajar_genjang()
        elif (userInput == 8):
            luas_belah_ketupat()
        elif (userInput == 9):
            luas_layang_layang()
        elif (userInput == 10):
            luas_Lingkaran()
        elif (userInput == 11):
            luas_Trapesium()
        elif (userInput == 12):
            luas_setengah_Lingkaran()
        elif (userInput == 13):
            luas_Poligon_Reguler()
        elif (userInput == 14):
            luas_Permukaan_Kubus()
        elif (userInput == 15):
            luas_Permukaan_Balok()
        elif (userInput == 16):
            luas_Permukaan_prisma_segitiga()
        elif (userInput == 17):
            luas_Permukaan_limas_segitiga()
        elif (userInput == 18):
            luas_Permukaan_limas_segiempat()
        elif (userInput == 19):
            luas_Permukaan_tabung()
        elif (userInput == 20):
            luas_Permukaan_kerucut()
        elif (userInput == 21):
            luas_permukaan_setengah_bola()
        elif (userInput == 22):
            luas_permukaan_silinder_tanpa_tutup()
        else:
            main.menu()

if __name__ == "__main__":
    start()
