# try except bloğunda eğer kodumuz try kısmını başarılı bulursa except kodunu okumaz ve atlar.

try:
    print(int(12/0))

# Exceptionlar özelden genele göre sıralanmalıdır. 
# Örneğin except Exception kodunu en başa alırsak sıralama hatası alırz.


except KeyError:
    print('Key Error')
except ZeroDivisionError:
    print('Bir sayı sıfıra bölünemez')
except Exception:
    print('Bir hata oluştu.')

# Herhangi bir hatayla karşılaşmazsa kullanıcıya geri bildirim olarak else ile bir mesaj gösterilebilir.

else:
    print('işlem başarıyla tamamlandı.')

# Finally key wordu ise her türlü çalışmaktadır.

finally:
    print('Her türlü çalışırım.')


