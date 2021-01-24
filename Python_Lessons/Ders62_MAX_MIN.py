# MIN ve MAX

nums = [1, 5, 3, 9, 32, 41]
string = 'cumhuriyet'

print(max(nums))
print(min(nums))
print(max(string))
print(min(string))

# SORT : Küçükten büyüğe doğru sıralar.

nums2 = [10, 1, 5, 43, 36, 23, 67, 0]
nums2.sort()
print(nums2)

""" sort metodu listeyi sıralı olarak kaydeder. Hafızada öyle kalır."""

# SORTED : Küçükten büyüğe doğru sıralar. reverse=True dersek büyükten küçüğe doğru sıralar.

nums3 = [10, 1, 5, 43, 36, 23, 67, 0]
print(sorted(nums3))
print(sorted(nums3, reverse=True))

""" sorted fonksiyonunu kullandıktan sonra listemiz eski haline geri döner."""

isimler = ['Ahmet', 'Mehmet', 'Rıza', 'Abdurrezzak', 'Cem', 'Furkan']
print(sorted(isimler, key=len))
print(sorted(isimler, key=len, reverse=True))
print(isimler)

# REVERSED

nums3 = [10, 1, 5, 43, 36, 23, 67, 0]

for num in reversed(nums3):
    print(num)
print(nums3)