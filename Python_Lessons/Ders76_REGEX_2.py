import re

sample_text = 'arin arinaarinksdjalkd231kjaq91981 19adasd838' 
sample_text2 = 'ARİN'

# .findall metodu geri dönüş olarak string listesi bulur.


result = re.findall(r'\d{3}', sample_text)
print(result)
print(result[0])
print(type(result[0]))

# .finditer metodu match listeleri içeren bir iterator döner.

result2 = re.finditer(r'\d{3}', sample_text)
for x in result2:
    print(x)

# .fullmatch metodunda aranan ifadeyle sample ifade birebir aynı olmalı
# re.ignorecase ile büyük küçük harf karmaşasını giderdik.
result3 = re.fullmatch(r'arin', sample_text2, flags=re.IGNORECASE)
print(result3)
print(result3.group())
