valid_coins = ["5", "10", "25"]
amount_due = 50
while amount_due>0:
    print(f"Amount Due: {amount_due}")
    user_input = input(f"Insert Coin: ")
    if user_input in valid_coins:
        amount_due -= int(user_input)
        print(f"Amount due:{amount_due}")
    if amount_due<= 0:
        break