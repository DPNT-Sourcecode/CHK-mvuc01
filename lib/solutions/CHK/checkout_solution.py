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
        "K": 70,
        "L": 90,
        "M": 15,
        "N": 40,
        "O": 10,
        "P": 50,
        "Q": 30,
        "R": 50,
        "S": 20,
        "T": 20,
        "U": 40,
        "V": 50,
        "W": 20,
        "X": 17,
        "Y": 20,
        "Z": 21,
    }

 
    total = 0
    items_in_skus = defaultdict(int)
    for item in skus:
        if item not in prices:
            return -1

        items_in_skus[item] += 1
    
    total, skus_minus_special = check_offers(items_in_skus, prices)
    for item in skus_minus_special.keys():
        total += prices[item]*skus_minus_special[item]
    return total

def check_offers(items_in_skus, prices):
    bulk_buy = {
        "A": [[5,200], [3,130]],
        "B": [[2,45]],
        "H": [[10,80], [5,45]],
        "K": [[2,120]],
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
    any_three_items = ["S","T", "X","Y","Z",]


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
    total+=check_any_three(items_in_skus, any_three_items, prices)

    return total, items_in_skus


def check_any_three(skus, any_three_items, prices):
     #[[sku, prices[sku]] for sku in any_three_items]
    any_three = [["S", 21],["T", 20],["Y", 20],["Z", 20],["X", 17]]
    total = 0
    sum_of_offers = 0
    for sku, _ in any_three:
        if sku not in skus:
            skus[sku] = 0
        sum_of_offers += skus[sku]

    # sum_of_offerings = sum(skus[item[0]] for item in any_three)
    target = sum_of_offers % 3
    # any_three.sort(key=lambda x: x[1], reverse=True) # sort by price
    to_process = sum_of_offers - target # should be a multiple of 3
    total += to_process * 15 # 45/3 is 15 each
    
    for sku, _ in any_three:
        while to_process > 0:
            if to_process >= skus[sku]:
                to_process -= skus[sku]
                skus[sku] = 0
                continue
            else:
                skus[sku] -= to_process
                to_process = 0
                break

    return total


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



