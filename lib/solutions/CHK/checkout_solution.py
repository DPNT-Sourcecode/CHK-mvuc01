from collections import defaultdict
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40
    }
    # special_prices = {
    #     "A": [3, 130],
    #     "B": [2, 45]
    # }    
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
        total = 0
        while items_in_skus["A"] >= 5:
            total += 200
            items_in_skus["A"] -= 5
        while items_in_skus["A"] >= 3:
            total+=130
            items_in_skus["A"] -= 3
        tmp = items_in_skus["E"]
        while tmp >= 2 and items_in_skus["B"]>0:
            items_in_skus["B"] -=1
            tmp-=2
        while items_in_skus["B"] >=2:
            total += 45
            items_in_skus["B"] -= 2
        return total, items_in_skus
            