
kata = input("masukkan sebuah kalimat : ")


def palindromeChecker(kata):
    if kata.lower() == kata[::-1].lower():
        return True
    else:
        return False
    
checker = palindromeChecker(kata)

print(checker)
