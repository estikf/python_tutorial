def convert_dollar_to_COMP202COIN(amount_of_dollars):
    actual_money = int(amount_of_dollars * 0.01)    # dollar multiplied by exchange rate
    result = hex(actual_money)  # convert dollars to COMP202COIN
    return result

def get_excess_dollars_after_conversion(amount_of_dollars):
    
    coins = convert_dollar_to_COMP202COIN(amount_of_dollars)
    
    excess_money = int(str(amount_of_dollars % 100))
    if excess < "64":
        print(excess_money)
    else:
        print(amount_of_dollars)

print(int("64",16))