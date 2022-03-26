from collections import defaultdict


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    """
    Given a string of sku codes, delimited by space character
    return the total cost.

    :param skus: str of sku values
    
    """
    assert isinstance(skus, str), f"skus paramter should be of type str not {type(skus)}"
    sku_list = []
    sku_counter = defaultdict(int)
    checkout_cost = 0

    # process input string and bin values
    sku_list = skus.split(" ")
    for sku_item in sku_list:
        sku_counter[sku_item] += 1

    for sku_item_type, sku_count in sku_counter.items():
        if sku_item_type == 'A':
            pass
        elif sku_item_type == 'B':
            pass
        elif sku_item_type == 'C':
            checkout_cost += 20*sku_count
        elif sku_item_type == 'D':
            checkout_cost += 15*sku_count
    

