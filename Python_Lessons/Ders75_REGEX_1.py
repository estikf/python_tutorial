import re

# compile metodu girilen ifadeyi regex ifadesine dönüştürür.
 
pattern = re.compile('furkan')

sample_text = 'lak33-444sdfurkanşarinlskd9furkan123891023 kajsdasd333123'

# arin ifadesini sample text içinde arıyoruz.
# search metodu ilk eşleşen nesneyi gösterir.

result = pattern.search(sample_text)
print(result)

# match olan ifadeyi göstermek için .group metodu kullanılır.

print(result.group())

# Aşağıdaki ifade daha kısa görünebilir ancak her çalıştırdığımızda sıfırdan compile etmiş olacağız.

result2 = re.search('furkan', sample_text)
print(result2)
print(result2.group())

result3 = re.search('\d{2}-\d{3}', sample_text)
print(result3)
print(result3.group())

# match metodunun eşleşmesi için ifadenin örnek stringin başında yer alması gerekir.

result4 = re.match('\d{2}-\d{3}', sample_text)
print(result4)

result5 = re.match('a', 'arin') #MATCH, çünkü ifade başta yer alıyor.
print(result5)

result6 = re.search('a', 'arin') #MATCH, çünkü ifade sample içinde yer alıyor.
print(result6)

result7 = re.match('n', 'arin')  #NONE, çünkü ifade sample'ın başında yer almıyor.
print(result7)

result8 = re.search('x', 'arin') #NONE, çünkü ifade sample'da bulunmuyor.
print(result8)

result9 = re.match('n', 'arin') #NONE, çünkü ifade sample'ın başında yer almıyor.
print(result9)
