def change_conversion(change):
    """
    extracting the equalent notes from user required amount bu using the vending machine
    """
    coins = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    for i in range(len(coins)):
        notes = change // coins[i]
        amount = notes * coins[i]
        change = change - amount
        if notes != 0:
            print(coins[i], "*", notes)
            return coins[i]*notes


if __name__ == '__main__':
    change_conversion(500)
