SUN_1_SET = True
SUN_2_SET = False
SOLAR_OBSERVATION_FEE_MULTIPLIER = 0.05
COMP202COIN_FLAT_FEE = 10
COMP202COIN_DOLLAR_EXCHANGE_RATE = 0.05
DOLLAR_COMP202COIN_EXCHANGE_RATE = 0.01
COMP202_SUPPLY = "32"

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
    if (SUN_1_SET is False) or (SUN_2_SET is False):
        return 0
    else:
        return int(amount_of_comp202coin, 16) * SOLAR_OBSERVATION_FEE_MULTIPLIER
    
def get_flat_fee():
    return COMP202COIN_FLAT_FEE

def convert_COMP202COIN_to_dollars(amount_of_comp202coin):
    base_10_number = int(amount_of_comp202coin, 16)

    """base_10_number = 0
    hex_numbers = "0123456789ABCDEF"
    
    for i,d in enumerate(str(amount_of_comp202coin).upper()):      
        value = hex_numbers.index(d)                            # value (0 - 15)
        power = len(amount_of_comp202coin) - (i+1)              # power 
        base_10_number += (value * 16 ** power)                 # value * 16 * power"""

    amount_of_dollar = (                                        # amount of dollar formula
        (base_10_number * COMP202COIN_DOLLAR_EXCHANGE_RATE) 
        - (get_solar_observation_fee(amount_of_comp202coin))
        - get_flat_fee()
        )

    return amount_of_dollar

def convert_dollar_to_COMP202COIN(amount_of_dollars):
    actual_money = int(amount_of_dollars * DOLLAR_COMP202COIN_EXCHANGE_RATE)    # dollar multiplied by exchange rate
    result = hex(actual_money)  # convert dollars to COMP202COIN
    return result

def get_excess_dollars_after_conversion(amount_of_dollars):

    excess_money = int(str(amount_of_dollars % 100))

    if excess_money < int(COMP202_SUPPLY, 16):
        amount_of_coins = convert_dollar_to_COMP202COIN(amount_of_dollars)

        print(f"You have deposited {amount_of_dollars} dollars. You will receive {amount_of_coins} coins ,and {excess_money} dollars will be returned to you.")
    else:
        print(f"Your transactions cannot be completed due to insufficient funds.")

def operate_machine():
        user_choice = input(display_welcome_menu())

        if user_choice == "1":
            amount_of_dollars = int(input("Enter the amount of dollar to convert: "))
            get_excess_dollars_after_conversion(amount_of_dollars)

        elif user_choice == "2":
            amount_of_coins = str(input("Enter the amount of COMP202COIN to convert: "))
            amount_of_dollars = convert_COMP202COIN_to_dollars(amount_of_coins)
            print(f"You have deposited {str(amount_of_coins).upper()} COMP202COIN. You will receive {amount_of_dollars} dollars.")

        elif user_choice == "3":
            print("Program terminated.")

        else:
            print("Please enter a valid choice.")

operate_machine()