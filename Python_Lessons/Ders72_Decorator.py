name = input('isminizi giriniz.')
age = input('Yaşınızı giriniz.')
gender = input('Cinsiyetinizi giriniz.')
def dec1(func):
    def wrapper(*args, **kwargs):
        print(((((int((len (name)) + (len(age)) + (len(gender)))) + 36))*'-'))
        print(((((int((len (name)) + (len(age)) + (len(gender)))) + 36))*'-'))
        func(*args, **kwargs)
        print(((((int((len (name)) + (len(age)) + (len(gender)))) + 36))*'-'))
        print(((((int((len (name)) + (len(age)) + (len(gender)))) + 36))*'-'))
    return wrapper

@dec1
def function(name, age, gender):
    print(f'İsminiz: {name}, Yaşınız: {age}, Cinsiyetiniz: {gender}')

function(name,age,gender)