from random import choice

def ran_pass(len_pass):
    symbol = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ''
    for i in range(len_pass):
        password += choice(symbol) # что это такое?
    return password
