deretAngka = int(input("masukkan berapa deret angka : "))

mylist = [0,1]

def febanacciSequence(deretAngka):
    for i in range(deretAngka-2):
        result = mylist[i] + mylist[i+1]
        mylist.append(result)
    
    print(mylist)


febanacciSequence(deretAngka)



