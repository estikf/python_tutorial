with open('data1.txt', 'r') as my_file:
    print(my_file.read())
# Datanın hepsi 2. satırdaki kodda okunacağından .read(5) yazılan kod çalışmayacaktır.  
    print(my_file.read(5))
    my_file.seek(0)
# Bu kod ile okunma sırasını dosyanın başına gönderiyoruz.
    print(my_file.read(5))
# Okuma sırasını dosyanın başına gönderdiğimiz için 7. satırdaki kod çalışmaya başlıyor. Aksi taksirde
#   çalışmayacaktı.
    my_file.seek(6)
# Bu kod ile Data'da 6. karaktere geldik.
    print(my_file.read(5))
# Bu kod ile Data'da 6'dan 11'e kadar okumuş olduk.
    print(my_file.tell())
# .tell metodu bize Data'nın hangi karakterinde olduğumuzu gösteriyor.
my_file = open('data1.txt', 'w')
courses = ['Python', 'Java', 'C#', 'Ruby']
# Bir liste oluşturduk.
for course in courses:
    my_file.write(f'{course}\n')
# \n koyarak kelimeleri satır satır yazdırdık.
with open('data2.txt', 'r') as my_file2:
    file_content = my_file2
    file_content = [element.strip('\n')for element in file_content if '\n' in element]
# Alt alt sıralanmış verileri tek bir satırda yazdırmak istediğimizde sonunda \n olarak ekleyerek yazdırıyordu.
# Bundan kurtulmak için satır 24'teki kodu kullandık.    
    print(file_content)
with open('data2.txt', 'r') as my_file2:
    with open('data3.txt', 'w') as my_file3:
        for line in my_file2:
            my_file3.write(line)

# Üstteki 4 kod sayesinde data2.txt dosyasındaki verileri okuduk. 
# Ardından data3.txt dosyasını oluşturup kopyaladık.