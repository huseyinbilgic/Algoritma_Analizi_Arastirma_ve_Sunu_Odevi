

#Regular expression

#örnek olarak
#abc*xy ---abcxy --abxy  --abcccxy
#ab*.   --abg  --ag


from numpy import ndarray
#total complexity O(n^2+n)
def esleme(kelime, desen):
    a = len(kelime)
    b = len(desen)

    kd = ndarray(shape=(a+1, b+1), dtype=bool)#kelime ve desen için 2 boyutlu dizi

    
    for i in range(a+1):#complexity => O(n)
        for j in range(b+1):
            kd[i][j]=False
    kd[0][0] = True
    
    print(kd)
    print("-----------------------------------")
    for i in range(2, b+1):#Bir deseni tanımlayabilmek için 2 boyutlu diziye False atadık.
        if desen[i-1] == "*":
            kd[0][i] = kd[0][i - 2]
    for i in range(1, a+1):#complexity=>O(n)
        #Desendeki * veya . karakterlerini tarayarak kelimenin desene uygun olup olmadığı çözülür.
        for j in range(1, b+1):#complexity =>O(n)
            x = kelime[i - 1]
            y = desen[j-1]
            if (x == y or y == '.'):
                kd[i][j] = kd[i - 1][j - 1]
            elif (y == '*'):
                if (kd[i][j - 2]):
                    kd[i][j] = True
                elif(x == desen[j - 2] or desen[j - 2] == '.'):
                    kd[i][j] = kd[i - 1][j]
    print(kd)
    return kd[a][b]


text = input("Kelime gir: ")
pattern = input("Deseni gir: ")
if esleme(text, pattern):
    print("Kelime desene uygundur.")
else:
    print("Kelime desene uygun değildir.")
