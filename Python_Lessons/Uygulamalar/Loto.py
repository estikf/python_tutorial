while True:    
    import random

    String = """    Süper Loto için 1
    Sayısal Loto için 2, 
    Çıkış için 3'e basınız. """
    def main():
        global z
        Giris = input(String)
        if Giris == '1':
            z = 54
            Loto(z)
            Numara()

        if Giris == '2':
            z = 49
            Loto(z)
            Numara()

        if Giris == '3':
            exit()

    def Loto(z):
        sayilar = [x for x in range(1,z)]
        Liste = list() 
        for n in range(6):
            x = random.choice(sayilar)
            Liste.append(x)
            sayilar.remove(x)
        return(Liste)

    def Numara():
        Sayi = 0
        for r in range(6):
            Sayi += 1
            print(f'Kolon {Sayi}: {Loto(z)}')
    main()