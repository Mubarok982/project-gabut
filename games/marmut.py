import random 
import main
def start():
    while True:
        bentuk_goa = "|_|"              
        bentuk_goa = "|_|"
        goa_kosong = [bentuk_goa] * 8
        goa = goa_kosong.copy()

        marmutpy_posisi = random.randint(1, 8)
        goa[marmutpy_posisi - 1] = "|0_0|"
        goa_kosong =  "   ".join(goa_kosong)
        goa =  "   ".join(goa)
        
        print(f'Halo Coba Perhatikan Goa Di Bawah Ini\n\n{goa_kosong}\n')

        pilihan_user = int(input ("Menurut kamu marmutnya ada di goa nomer berapa? [1/2/3/4/5//6/7/8]:"))
        print (f"goa pilihan kamu adalah: {pilihan_user}")
        
        if pilihan_user == marmutpy_posisi:
            print (f"{goa} \nSELAMAT  KAMU BENAR!, POSISI MARMUT ADA DI GOA NOMER: {marmutpy_posisi} DAN PILIHANMU ADALAH {pilihan_user} KAMU DAPET MARMUT!")         
        else:
            print (f"{goa} \nKAMU KALAH! POSISI MARMUT BUKAN DI GOA NOMER {pilihan_user} TAPI ADA DI GOA NOMOR {marmutpy_posisi}") 
        
        play_again = input("\n\n apakah ingin melanjutkan lagi? [y/n]")
        if play_again == "n":
            main.menu()
  
if __name__ == "__main__":
    start()
