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
            # find number speacial offer collections and add to total
            speacials_count = sku_count // 3
            checkout_cost += speacials_count*130

            # find remainder normal cost items and add to total
            normal_count = sku_count % 3
            checkout_cost += normal_count*50

        elif sku_item_type == 'B':
            # find number speacial offer collections and add to total
            speacials_count = sku_count // 2
            checkout_cost += speacials_count*45

            # find remainder normal cost items and add to total
            normal_count = sku_count % 2
            checkout_cost += normal_count*30
        elif sku_item_type == 'C':
            checkout_cost += 20*sku_count
        elif sku_item_type == 'D':
            checkout_cost += 15*sku_count
        else:
            # ERROR
            return -1

    return checkout_cost
