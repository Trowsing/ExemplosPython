def main():
    value = get_value()
    coins = get_coins_list()
    necessary_coins, remainder = get_necessary_coins(value, coins)
    for coins in necessary_coins:
        coins_var, cents_var = get_cents_variables(coins)
        print(f"You need {coins[0]} {coins_var} of {coins[1]} {cents_var}")
    if remainder != 0:
        print(f"It was not possible to allocate {remainder} cents with your coins :(")


def get_necessary_coins(value, coins):
    coins.sort()
    new_coins = []
    for coin in reversed(coins):
        necessary, remainder = divmod(value, coin)
        if necessary >= 1:
            new_coins.append((necessary, coin))
            value = remainder
    return new_coins, value


def get_value():
    try:
        value = int(input("Insert an integer amount to get its value in coins: "))
        if isinstance(value, int):
            if value <= 0:
                raise InvalidValue
            return value
        raise InvalidValue
    except InvalidValue:
        print("Invalid value!")
        get_value()


def get_coins_list():
    try:
        coins = input("Insert all avalible coins delimited by spaces: ").split(" ")
        if isinstance(coins, list):
            coins = [int(i) for i in coins]
            return coins
        raise InvalidCoinsList
    except (InvalidCoinsList, ValueError):
        print("Invalid coins input!")
        get_coins_list()


def get_cents_variables(coins):
    if coins[0] > 1:
        coins_var = "coins"
    else:
        coins_var = "coin"
    if coins[1] > 1:
        cents_var = "cents"
    else:
        cents_var = "cent"
    return coins_var, cents_var


class InvalidValue(Exception):
    """Invalid value input"""


class InvalidCoinsList(Exception):
    """Invalid coins list input"""


if __name__ == "__main__":
    main()
