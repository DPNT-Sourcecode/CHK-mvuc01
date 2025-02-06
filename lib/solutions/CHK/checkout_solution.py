from collections import defaultdict
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    def check_offers():
        total = 0
        total += check_offer_a()
        check_offer_e()
        total += check_offer_b()
        return total

    def check_offer_a():
        total=0
        while items_in_skus["A"] >= 5:
            total += 200
            items_in_skus["A"] -= 5
        while items_in_skus["A"] >= 3:
            total+=130
            items_in_skus["A"] -= 3
        return total
    
    def check_offer_e():
        tmp = items_in_skus["E"]
        while tmp >= 2 and items_in_skus["B"]>0:
            items_in_skus["B"] -=1
            tmp-=2

    def check_offer_b():
        total=0
        while items_in_skus["B"] >=2:
            total += 45
            items_in_skus["B"] -= 2
        return total
    
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
    
    total = check_offers(0)
    for item in items_in_skus.keys():
        total += prices[item]*items_in_skus[item]
    return total

            


