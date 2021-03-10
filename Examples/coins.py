
BASE_8 = "01234567"
COMP_202_numbers = "0C2OMPIN"

# ilk iki karakter 0c veya 0C değilse false, geri kalan 8 karakter uymuyorsa false
def is_202(text):
    if text[0:2].lower() == "0c":
        for ch in text[2:]:
            if ch not in COMP_202_numbers:
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
            value = COMP_202_numbers.index(coin_part[i])                # value (0 - 7)
            power = len(coin_part) - (i+1)                              # power 
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

def get_nth_base202_amount(text,n):
    i = 0
    coins = []
    while "0c" in text[i:].lower():
        coin_starting_index = text[i:].lower().index("0c")                                  # 66
        coin = (text[coin_starting_index + i : coin_starting_index + i + 10])               # text[66:74]
        i = i + coin_starting_index + 8                                                     # i = 0 +  74
        if is_202(coin):
            coins.append(coin)
    return coins[n]

print(get_nth_base202_amount("BANKING TRANSACTIONS... .PLANET ORION......FEBRUARY \
15, 3019.......0cCCMMPP22........FEBRUARY 16, 3019..........0cOCOCOCOC      0C24242412",0))