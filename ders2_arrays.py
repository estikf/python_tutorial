# List

thislist = ["apple", "banana", 1, "orange", False, "melon", "mango"]

"""thislist[0] = "Alp"
thislist[1:5] = ["Furkan"]


if "Furkan" in thislist:
  print("Bu eleman vardır")
else:
    print("Bu eleman yoktur")


thislist.insert(0,"Furkan")
thislist.append("Alp")
thislist.extend(("Karpuz", "kavun"))
thislist.remove("cherry")
thislist.pop(0)
del thislist[0]"""



"""i = 0

while i<len(thislist):
    print(thislist[i])
    i = i + 1"""

# List Comprehension
 
my_list_2 = [x for x in range(10)]
my_list_2.sort()

# Tuple (Immutable - Unchangeable)

"""my_tuple = tuple(thislist)
print(my_tuple)

my_second_tuple = (1,2,3,4,5,6)
my_second_list = list(my_second_tuple)
my_second_list[0] = "Furkan"
print(my_second_list)
my_second_tuple = tuple(my_second_list)
print(my_second_tuple)


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

print(fruits.index("mango"))"""

# Set (Unordered - Random - We can remove an item - We can update)

thisset = {"apple", "banana", "cherry"}
"""tropical = {"pineapple", "mango", "papaya"}

thisset.add("Karpuz")
thisset.update(tropical)
thisset.update({"name":"furkan"})
thisset.remove("Alp")
thisset.discard("Alp")
mylist = list(thisset)
mylist.pop()
print(mylist)
"""

"""x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)"""

# Dictionary

"""my_dict = {
    "name":"Furkan",
    "surname":"Estik",
    "body":
            {
                "head":False,
                "arm":True,
                "foot":
                {
                    "right_foot_finger":5,
                    "left_foot_finger":{1,2,3,4,5}
                }
            }
    }
print(type(my_dict["body"]["foot"]["left_foot_finger"]))
my_dict["body"]["foot"]
my_dict.update({"name":"Furkan"})
print(my_dict)

for x, y in my_dict.keys():
  print(f"Key: {x}, Value: {y}")"""


# If - Else - Elif - For - While

"""sayi_listesi = [x for x in range(10)]

for i in sayi_listesi:
    if (i==5):
        pass
    elif (i==7):
        break
    print(i)
        
x=0
while x<10:
    print(x)
    x += 1"""

"""kullanici_input = set()


for i in range(10):
    kullanici_input.add(input("Bir input giriniz: "))

print(kullanici_input)"""


"""adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for i in adj:
    for x in fruits:
        print(f"{i} {x}")
"""

my_dict = {
    "name":"Furkan",
    "surname":"Estik"}

for i in my_dict:
    my_dict[i]="A"