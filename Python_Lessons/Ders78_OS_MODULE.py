import os

# os.name, kullanılan işletim sistemini verir.

# os.getcwd(), şu anda çalışılan klasörün yolunu verir.

# os.chdir(), şu anda çalışılan klasörün adresini değiştirir.
# raw string ile girilmelidir ki adres çalışsın.

# os.listdir(), çalışılan ortamda bulunan dosyalar ve klasörler görünür.

# os.mkdir(), çalışılan ortamda dosya oluşturur.

# os.mkdirs('x/x/x/...'), iç içe geçmiş klasörden oluşturulabilir.

# os.remove('test.txt'), girilen dosyayı siler.

# os.rmdir('test), test adlı dosyayı siler. Ancak dosyanın içinin boş olması gerekir.

# os.removedirs('2020/01/20'), 2020, 01 ve 20 isimli dosyaları siler.

# os.rename('text.txt', 'test.xls'), varolan dosyanın ismini değiştir.

# os.walk(), üç elemanlı tuple döner. Dosyaların haritasını çıkarır.

# os.stat()

path = r'C:\Users\Furkan\Desktop\Python Dersleri\python_lessons'

for paths, dirs, files in os.walk(path):
    print(f'{paths}, {dirs}, {files}')





