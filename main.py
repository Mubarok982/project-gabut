
from libs import welcome_message, exit_program
from games import marmut
from tools import warung
from tools import mtk


def options():
  user_options = int(input(f'menu program:\n1. Games MarmutPY\n2. Warung Tools\n3. Rumus MTK\n4. keluar program\n\nsilahkan pilih: '))
  return user_options

def menu():
    welcome_message()
    user_optins = options()
    if user_optins == 1:
      marmut.start()
    elif user_optins == 2:
      warung.start()
    elif user_optins == 3:
      mtk.start()
    elif user_optins == 4:
      exit_program()
    else:
      print('hanya boleh pilih yang tersedia di menu!')
    
if __name__ == "__main__":
    menu()