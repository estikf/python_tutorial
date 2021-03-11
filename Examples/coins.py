
BASE_8 = "01234567"
COMP_202_numbers = "0C2OMPIN"

# ilk iki karakter 0c veya 0C değilse false, geri kalan 8 karakter uymuyorsa false
def is_202(text):
    if (text[0:2].lower() == "0c") and len(text) == 10:
        for ch in text[2:]:
            if ch.lower() not in COMP_202_numbers.lower():      # 0cCPOM2PPP
                return False
        return True
    else:
        return False

def base202_to_10(amt_in_base202):
    # önce girilen textin coin olup olmadığına bak
    if is_202(amt_in_base202) is True:
    
        # eğer doğruysa çevirme işlemlerine başla
        base_10_number = 0
        coin_part = amt_in_base202[2:]
        for i in range(len(str(coin_part))):      
            value = COMP_202_numbers.index(coin_part[i])                # value (1)
            power = len(coin_part) - (i+1)                              # power 0
            base_10_number += (value * 8 ** power)                      # value * 8 * power
        return base_10_number

    # girilen text coin değilse
    else:
        return "Please enter a valid coin."

def base10_to_202(amt_in_base10):
    octal_prefix = "0c"
    octal_rest = oct(amt_in_base10)[2:]
    if len(octal_rest) < 8:
        octal_prefix += "0"* (8-len(octal_rest))
    for i in octal_rest:
        octal_prefix += COMP_202_numbers[int(i)]
    
    return octal_prefix

def get_nth_base202_amount_list(text):
    i = 0
    coins = []
    while "0c" in text[i:].lower():                                                                 # i = 0
        coin_starting_index = text[i:].lower().index("0c")                                          # 66
        coin = (text[coin_starting_index + i : coin_starting_index + i + 10])               # text[66:74] 
        i = i + coin_starting_index + 9
        if is_202(coin):                                                     # i = 0 +  74
            coins.append(coin)
    return coins

def get_nth_base202_amount(text,n):
    coins_list = get_nth_base202_amount_list(text)
    if n+1 <= len(coins_list):
        return coins_list[n]
    else:
        return "''"

def get_total_dollar_amount(text):
    coins_list = get_nth_base202_amount_list(text)
    total_dollar_amount = 0
    for i in coins_list:
        if is_202(i):
            dollar_amount = base202_to_10(i)
            total_dollar_amount += int(dollar_amount)
    return total_dollar_amount

def reduce_amounts(text, limit):
    total_dollar_amount = get_total_dollar_amount(text)
    if total_dollar_amount <= limit:
        return base10_to_202(total_dollar_amount)
    else:
        reduction = (total_dollar_amount - limit) / total_dollar_amount
        for coin in get_nth_base202_amount_list(text):
            coin_in_base_10 = base202_to_10(coin) * (1-reduction)
            coin_in_base_202 = base10_to_202(int(coin_in_base_10))
            print(coin_in_base_202)

"""print(get_nth_base202_amount("ALPCAN FURKAN 0cCOMP2022 0c0c220COMP URKAN FURKAN FURKAN 0cCOMP202C 0cPOMP2P2C , ,- -343# 0CCOMP202CP", 5))

print(get_total_dollar_amount("BANKING TRANSACTIONS....PLANET ORION......FEBRUARY 15, 3019.......0cCCMMPP22........FEBRUARY 16, 3019..........0cOCOCOCOC........FEBRUARY 17, 3019..........0C24242412"))
"""
reduce_amounts("0cCCMMPP22 0cOCOCOCOC", 9000000)