SUN_1_SET = False
SUN_2_SET = True
SOLAR_OBSERVATION_FEE_MULTIPLIER = 0.05
COMP202COIN_FLAT_FEE = 10
COMP202COIN_DOLLAR_EXCHANGE_RATE = 0.05
DOLLAR_COMP202COIN_EXCHANGE_RATE = 0.01
COMP202_SUPPLY = "128"

def display_welcome_menu():
    
    display_string = """
        | Welcome to the Orion IX COMP202COIN virtual exchange machine. |
        | Available options:                                            |
        | 1. Convert dollars into COMP202COIN                           |
        | 2. Convert COMP202COIN into dollars                           |
        | 3. Exit program
    """
    return display_string

def get_solar_observation_fee(amount_of_comp202coin):
    if (SUN_1_SET is True) or (SUN_2_SET is True):
        return 0
    else:
        return amount_of_comp202coin * SOLAR_OBSERVATION_FEE_MULTIPLIER
    
def get_flat_fee():
    return COMP202COIN_FLAT_FEE

def convert_COMP202COIN_to_dollars(amount_of_comp202coin):
    base_10_number = 0
    hex_numbers = "0123456789ABCDEF"
    
    for i,d in enumerate(str(amount_of_comp202coin).upper()):      
        value = hex_numbers.index(d)                            # value (0 - 15)
        power = len(amount_of_comp202coin) - (i+1)              # power 
        base_10_number += (value * 16 ** power)                 # value * 16 * power

    amount_of_dollar = (                                        # amount of dollar formula
        (base_10_number * COMP202COIN_DOLLAR_EXCHANGE_RATE) 
        - (get_solar_observation_fee(amount_of_comp202coin) * base_10_number)
        - COMP202COIN_FLAT_FEE
        )
    if amount_of_dollar > 0:
        return amount_of_dollar
    else:
        return 0

def convert_dollar_to_COMP202COIN(amount_of_dollars):
    actual_money = int(amount_of_dollars * DOLLAR_COMP202COIN_EXCHANGE_RATE)    # dollar multiplied by exchange rate
    result = hex(actual_money)  # convert dollars to COMP202COIN
    return result

def get_excess_dollars_after_conversion(amount_of_dollars):
    
    coins = convert_dollar_to_COMP202COIN(amount_of_dollars)
    excess_money = int(str(amount_of_dollars % 100)[-2:])
    if coins < COMP202_SUPPLY:
        return excess_money
    else:
        return amount_of_dollars

def operate_machine():
    while True:
        user_choice = input(display_welcome_menu())

        if user_choice == "1":
            amount_of_dollars = int(input("Enter the amount of dollar to convert: "))
            
            if amount_of_dollars < int(COMP202_SUPPLY, 16):
                amount_of_coins = convert_dollar_to_COMP202COIN(amount_of_dollars)
                excess_money = get_excess_dollars_after_conversion(amount_of_dollars)
                print(f"You have deposited {amount_of_dollars}. You will receive {amount_of_coins},and {excess_money} dollars will be returned to you.")
            else:
                print(f"Your transactions cannot be completed due to insufficient funds.")

        elif user_choice == "2":
            amount_of_coins = str(input("Enter the amount of COMP202COIN to convert: "))
            amount_of_dollars = convert_COMP202COIN_to_dollars(amount_of_coins)
            print(f"You have deposited {str(amount_of_coins).upper()} COMP202COIN. You will receive {amount_of_dollars} dollars.")

        elif user_choice == "3":
            print("Program terminated.")
            break
        else:
            print("Please enter a valid choice.")

operate_machine()