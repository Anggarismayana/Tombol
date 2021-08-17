# ini cuma shortcut buat bantu para nub !
# Angga Rismayana
import os
from time import sleep
from threading import Thread as td


a =' \033[1;32m ' #Hijau
b ='  \033[1;31m' #merah
c ='\033[1;33m' #kuning

class Terkey:
  def __init__(self):
    pass

  # Banner
  def banner(self):
      os.system('clear')
      print(f'{c}≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈»')
      print(f'{a}       - Tolls Tombol Termux -                           ')
      print(f'{a}                              ')
      print(f'By     : Angga Rismayana ')
      print(f'Team   : MAFIA TEKNOLOGI ')
      print(f'Github : https://github.com/Anggarismayana' )
      print(f'                               ')
      print(f'{c}≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈»')
      print("".join([i for i in "\n"*2]))

  # Loading animation
  def animate(self,params):
    self.banner()
    print(f"{a}Memasang Tombol..!!")
    t = td(target=self.setup,args=(params,))
    t.start()
    while t.is_alive():
          for i in "-\|/-\|/":
              print(f'\r{a}Harap Tunggu{a}{i} ',end="",flush=True)
              sleep(0.1)
    self.banner()
    print(f"Tombol Terpasang !\n\n{c}Terimakasih sudah pakai Tolls ini\nsemoga bermanfaat ^_^  !")

  # Of course, like it name, paginate !
  def paginate(self,data,n):
    n_data = round(len(data)/n) + 1
    new_data_part = []
    batas = 0
    for i in range(n_data):
      new_data = []
      for x in range(batas,n+batas):
        try:
          new_data.append(data[x])
        except:
          pass
        batas += 1
      if new_data: new_data_part.append(new_data)
    return new_data_part

  # setting up the selected keys
  def setup(self,keys):
      keys = f"extra-keys = {keys}"
      try:
          os.mkdir('/data/data/com.termux/files/home/.termux')
      except:
          pass
      open('/data/data/com.termux/files/home/.termux/termux.properties','w').write(keys)
      os.system('termux-reload-settings')

  # If you choose default keys, this function will be executed.
  def standar(self):
    key = "[['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
    return key

  def about(self):
    self.banner()
    print(f"""
   {c}Hai.. !


  Bagaimana cara menghubungi saya ??

  My Instagram : rismayanaangga_04

  Kalian boleh Dm untuk tanya-tanya tolls ini :) 
  Terimakasih sudah menggunakan Tolls ini  ^_^
    """
    )
  # And if you select custom keys,
  def custom(self):
    index = 1
    lastindex = 0
    keys = ["CTRL","ALT","FN","SPACE","ESC","TAB","HOME","END","PGUP","PGDN","INS","DEL","BKSP","UP","LEFT","RIGHT","DOWN","ENTER","BACKSLASH","QUOTE","APOSTROPHE","F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12","KEYBOARD","DRAWER"]
    print(f"{a} --+ {c}Default Key Lists {a}+--".center(62))
    print()
    for i in self.paginate([*enumerate(keys)],4):
      for x in i:
        en = " " * (15 - len(". ".join([str(x[0]+1),x[1]])))
        print(f"{a}{x[0]+1}.{c} {x[1]}",end=en)
      print()
    print(f"{c}\nMasukkan nomor kunci yang kamu pilih \ndan pisahkan dengan koma (,) {a}contoh: 1,2,3,4{c}\natau kamu dapat menambahkan kunci kustom sendiri \nyang kamu Suka {a}1,2,3,(,),*,<,>{c} etc.")

    selected_keys = []
    user_select = input(f"\n{a}Input {c}: ")
    ranges = [str(i+1) for i in range(len(keys))]
    for i in user_select.split(","):
      if i.isdigit() and i in ranges:
        selected_keys.append(keys[int(i)-1])
      else:
        selected_keys.append(i)
    return selected_keys

  # Main
  def start(self):
    self.banner()
    print(f"    {a}[ {c}PILIH MENU {a}]")
    print(f"""
  {a}1.{c} Pasang Otomatis
  {a}2.{c} Pasang Sendiri
  {a}3.{c} Tentang Tolls Ini
    """
    )
    menu = input(f"  {c}>{a} ")
    if menu == "1":
      self.banner()
      key = self.standar()
      self.animate(key)
    elif menu == "2":
      self.banner()
      key = self.custom()
      keys = self.paginate(key,7)
      print(f"{c}\nSelected keys: {c}{','.join(key)}{c}\nAre you sure ?")
      try:
        input(f"{c}Press enter to continue or CTRL + C to cancel ")
        self.animate(keys)
      except:
        exit(f"{b}Canceled!{c}")
    elif menu == "3":
      self.about()
    else:
      pass
if __name__=='__main__':
  terkey = Terkey()
  terkey.start()
