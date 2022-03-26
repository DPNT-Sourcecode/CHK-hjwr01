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
    sku_counter = defaultdict(int)
    checkout_cost = 0
    sku_type_priority = ['C', 'D', 'B', 'A', 'E']

    # edge case wher no items
    if not skus:
        return 0

    # process input string and bin values
    for sku_item in skus:
        # check if illegal item type
        if sku_item not in sku_type_priority:
            return -1
        sku_counter[sku_item] += 1

    
    # go through each bin and find associated cost for each item type
    for sku_item_type in sku_type_priority:
        sku_count = sku_counter[sku_item_type]
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



