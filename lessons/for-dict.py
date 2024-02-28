"""Practice with Dictionaries and for Loops!"""

in_stock: dict[str, bool] = {"carrots": True, "beets": False, "apples": True}

for key in in_stock:
    if in_stock[key]:
        print(key)