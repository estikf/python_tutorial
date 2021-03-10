x = 5
try:
    print(x)
    print("2"+2)
except NameError:
    print("Bu değişken tanımlanmadı")
except ZeroDivisionError:
    print("0'a bölmeye çalıştın.")
except:
    print("Bir hata oluştu.")
finally:
    print("Her türlü çalışırım. Command executed.")