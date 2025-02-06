from collections import defaultdict
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
        "F": 10,
        "G": 20,
        "H": 10,
        "I": 35,
        "J": 60,
        "K": 80,
        "L": 90,
        "M": 15,
        "N": 40,
        "O": 10,
        "P": 50,
        "Q": 30,
        "R": 50,
        "S": 30,
        "T": 20,
        "U": 40,
        "V": 50,
        "W": 20,
        "X": 90,
        "Y": 10,
        "Z": 50
    }

 
    total = 0
    items_in_skus = defaultdict(int)
    for item in skus:
        if item not in prices:
            return -1

        items_in_skus[item] += 1
    
    total, skus_minus_special = check_offers(items_in_skus)
    for item in skus_minus_special.keys():
        total += prices[item]*skus_minus_special[item]
    return total

def check_offers(items_in_skus):
    bulk_buy = {
        "A": [[5,200], [3,130]],
        "B": [[2,45]],
        "H": [[10,80], [5,45]],
        "K": [[2,150]],
        "P": [[5,200]],
        "Q": [[3,80]],
        "V": [[3,130],[2,90]],
    }

    bogof = {
        "F": 2,
        "U": 3
    }
    bogaf = {
        "E": [2, "B"],
        "N": [3, "M"],
        "R": [3, "Q"]
    }
    total = 0
    for item in items_in_skus:
        if item in bogaf:
            buy_x_get_y(item, bogaf[item], items_in_skus)
        if item in bogof:
            buy_x_get_one(item, bogof[item], items_in_skus)
    for item in items_in_skus:
        if item in bulk_buy:
            for schema in bulk_buy[item]:
                number, cost = schema
                total += x_for_y(item, number, cost, items_in_skus)

    return total, items_in_skus





        # while items_in_skus["A"] >= 5:
        #     total += 200
        #     items_in_skus["A"] -= 5
        # while items_in_skus["A"] >= 3:
        #     total+=130
        #     items_in_skus["A"] -= 3
        # tmp = items_in_skus["E"]
        # while tmp >= 2 and items_in_skus["B"]>0:
        #     items_in_skus["B"] -=1
        #     tmp-=2
        # while items_in_skus["B"] >=2:
        #     total += 45
        #     items_in_skus["B"] -= 2
        # if items_in_skus["F"] > 2:
        #     # get 1/3 of F's removed(rounded down)
        #     discount = items_in_skus["F"] // 3
        #     items_in_skus["F"] -= discount

def x_for_y(item, number, price, skus):
    total = 0
    while skus[item] >= number:
        total +=price
        skus[item] -= number
    return total

def buy_x_get_one(x, number, skus):
    if skus[x] > number:
        discount = skus[x] // (number+1)
        skus[x] -= discount

def buy_x_get_y(x ,offer, skus):
    number, y = offer
    tmp = skus[x]
    if y not in skus.keys():
        return
    while tmp >= number and skus[y] > 0:
        skus[y] -=1
        tmp-=number



