my_flag = True
message = ''
while my_flag:
    message = input('Bir mesaj giriniz: ')
    if message == 'quit':
        break
    else:
        print(message)

