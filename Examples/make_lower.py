lower_alpha = "abcdefghijklmnopqrstuvwxyz"
upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def make_lower(string_word):
    new_word = ""
    for i in string_word:
        if upper_alpha.__contains__(i):
            new_word += lower_alpha[upper_alpha.index(i)]
        else:
            new_word += i

    print(new_word)

make_lower("APPLe")