from collections import defaultdict
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15
    }
    special_prices = {
        "A": [3, 130],
        "B": [2, 45]
    }    
    total = 0
    items_in_skus = defaultdict(int)
    for item in skus:
        if item not in prices:
            return -1
        items_in_skus[item] += 1
    
    for item in items_in_skus.keys():
        if item in special_prices:
            while items_in_skus[item] > special_prices[item][0]:
                total += special_prices[item][1]
                items_in_skus[item] -= special_prices[item][0]
        total += prices[item]*items_in_skus[item]
    return total
