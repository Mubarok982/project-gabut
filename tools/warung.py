import main 
def start():
    while True: 
        print("ini warung apps")
        harga = int(input("harga: "))
        
        if harga == 0:
            main.menu()

if __name__ == "__main__":
    start()