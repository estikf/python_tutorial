with open(r"C:\Users\Furkan\Desktop\Python_Tutorials\Examples\Python_Kaynaklar.txt","r") as f:
    for x in f:
        print(x.upper())

with open("my_data.txt","w",encoding="utf-8") as f2:
    for i in range(10):
        f2.writelines("Nasılsın2")