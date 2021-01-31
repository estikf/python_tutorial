def display_welcome_menu():
    # İki seçenek olacak, 
    # A. Quantity Mode
    # B. Price Mode
    pass

def get_fair_quantity(big_pizza, small_pizza):
    
    # Shop'un bize vereceği doğru pizza sayısını hesapla
    # Inputun sırası önemli değil biz ayarlayacağız.
    if big_pizza > small_pizza:
        pass
    else:
        pass

def get_fair_price(large_pizza_dia, large_pizza_price, small_pizza_dia, small_pizza_quantity):

    # Alanları oranlayıp küçük pizza fiyatı bulunacak.
    pass

def run_pizza_calculator():
    display_welcome_menu()

    girdi = input()

    if girdi == "A":
        print("You selected Quantity Mode")
        big_pizza = input("Rastgele bir pizza çapı giriniz: ")
        small_pizza = input("Rastgele bir pizza çapı giriniz: ")

        get_fair_quantity(big_pizza, small_pizza)
    
    elif girdi == "B":

        print("You selected Price Mode")
        x = input()
        y = input()
        z = input()
        k = input()
        get_fair_price(x,y,z,k)

    else:
        print("This mode is not supported!")

run_pizza_calculator()