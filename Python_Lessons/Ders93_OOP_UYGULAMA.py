# 1: setattr özelliğini kullanarak dinamik olarak özellik ekleyelim.

"""class Student:
    pass
    
    def __str__(self):
        return f'Öğrenci ismi: {self.name}'
student1 = Student()
setattr(student1,'name', 'Ahmet')
print(student1)"""

# 2: Student classını kullanarak init metoduyla tekrar oluşturalım, herhangi bir nesne
# özelliğini güncelleyelim, del metoduyla nesne özelliğini silelim sonra dellattr kullanalım

"""class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student('Ahmet', 23)
print(student1.name)

student1.name = 'Rıza'
print(student1.name)

del student1.name
print(student1.name)

delattr(student1.name)
print(student1.name)"""

# 3: Biz herhangi bir nesneyi silmek isteyip del metodu kullanırsak, o nesne hafızadan silinmez.
# sadece o nesneyi tutan referansı silmiş oluruz.

# 4: self parametresi yerine selvi parametresini kullanırsak nasıl olur?
# ilk parametre olarak ne kullanırsak çalışır ancak genel olarak self yazılır.

"""class Student():
    def __init__(selvi, name, age):
        selvi.name = name
        selvi.age = age"""

# 5: dunder mro metoduna örnek yapalım
# mro = method resolution order

class A():
	pass

class B(A):
	pass

class C(B):
	pass

class D(C):
	pass

class E(D, C):
	pass

print(E.__mro__)

# bu şekilde method uygulama sıralarını görebiliriz. 
# methodlar E, D, C, B, A şeklinde gidiyor.

