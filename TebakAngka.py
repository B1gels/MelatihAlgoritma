import random

angka = random.randrange(10)
playerChange = 5

while True:
    if playerChange == 0:
        print("Anda gagal")
        break

    try:
        user_choice = int(input("\ntebak angka dari 1 - 10 : "))

    except : 
        print('masukkan angka yang valid')
        continue



    if user_choice < 0 or user_choice > 10:
        print("diluar batas yang ditentukan")
    elif user_choice < angka :
        print("\nangka yang dimasukkan terlalu kecil")
        playerChange -= 1
        print(f"kesempatan anda sisa {playerChange}")
    elif user_choice > angka :
        print("\nangka yang dimasukkan terlalu besar")
        playerChange -= 1
        print(f"kesempatan anda sisa {playerChange}")
    elif user_choice == angka:
        print("\n","="*35)
        print("\n\tselamat anda menang\n")
        print("="*35)
        break