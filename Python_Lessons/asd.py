base_url = 'http://quotes.toscrape.com/page/2/'

x = 2
list1 = list(base_url)
list2 = []
for a in range(10):
    x += 1
    b = str(x)
    list1[32] = b
    base_url = ''.join(list1)
    list2.append(base_url)

print(list2)