def func1(username, age):
    print(f'Merhaba {username} {age} yaşındasınız')
func1(str(input('Adınızı Giriniz.')), int(input('Yaşınızı Giriniz.')))

def func2():
    return 5 + 10
def func3():
    print(6+10)

result1 = print(f'Sonuç1: {func2()}')
result2 = print(f'Sonuç2: {func3()}')

