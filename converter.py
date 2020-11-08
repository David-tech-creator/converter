def currency_converter(euro):
    if euro < 0:
        print("Beware, this is a negative value!")
    msg_1 = " Euro equals "
    msg_2 = " Chf "
    result = euro*1.08
    return str(euro) + msg_1 + str(result) + msg_2


print(currency_converter(-12))