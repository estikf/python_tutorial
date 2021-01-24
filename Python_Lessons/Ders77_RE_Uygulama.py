#   ÖRNEK 1:
#   Kullanıcının 234 34-58 şablonunda tel no girdiğini kontrol et.
#   Girilen telefon numarasını gösterelim, yanlış girileni belirletelim.

"""import re

telefon = input('Lütfen telefon numaranızı XXX XX-XX formatında giriniz: ')
def phone_checker(telefon):
    pattern = re.compile(r'^[0-9]{3}\s+[0-9]{2}-[0-9]{2}$')
    result = pattern.search(telefon)
    if result:
        return f'Girdiğiniz telefon numarası : {result.group()}'
    return f'Lütfen telefon numaranızı düzgün giriniz'

print(phone_checker(telefon))"""

#   ÖRNEK 2:
#   test stringinden rakamları liste içerisinde çıkaralım.

"""
import re
test_string = 'asdlaksşdl99384934 23092 alskd2394 aklsd9933 alskd9329'
result = re.findall(r'\d+', test_string)
print(result)
"""

#   ÖRNEK 3.
#   (^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$) email regex yapısını VERBOSE ile gruplayın.

import re

# VERBOSE yaparak bunları gruplandırabiliriz. Kodun okunabilirliği artar ve data düzeni sağlar.
# VERBOSE yazmazsak grupları göremeyiz.

pattern = re.compile(r'''
    (^[a-zA-Z0-9_.+-]+)      # 1. Grup email Adı
    @                       # @ işareti
    ([a-zA-Z0-9-]+)           # 2. Grup Domain Adı
    \.                      # nokta işareti
    ([a-zA-Z0-9-.]+$)        # 3. Grıp Uzantı Adı
''', re.VERBOSE)

result = re.search(pattern, 'arin.yazilim@gmail.com')
print(result.group())
print(result.groups())
print(result.groups()[0])
