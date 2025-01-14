# membuat fungsi yang mengurutkan bilangan dari yang terkecil

angka = [50,80,90,20,10]
print(angka) 


def buubleSort(angka):
    for i in range(len(angka)-1,-1,-1):
        for j in range(i):
            if angka[j] > angka[j+1]:
                temp = angka[j]
                angka[j] = angka[j+1]
                angka[j+1] = temp

        print(angka)

buubleSort(angka)
print(angka)
    

