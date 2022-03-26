from collections import defaultdict


def cost_by_item_type(items_count: int, offer_lookup: dict):
    items_cost = 0
    remaining_count = items_count

    offer_amounts = list(offer_lookup.keys())
    offer_amounts.sort(reverse=True)

    for offer_units in offer_amounts:
        offer_collection_price = offer_lookup[offer_units]
        
        speacials_count = remaining_count // offer_units
        remaining_count = remaining_count % offer_units

        items_cost += speacials_count*offer_collection_price
    
    assert remaining_count == 0
    return items_cost




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
    sku_type_priority = ['E','B', 'A', 'C', 'D' ]

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
            checkout_cost += cost_by_item_type(sku_count, {1: 50, 3: 130, 5:200})
        elif sku_item_type == 'B':
            checkout_cost += cost_by_item_type(sku_count, {1: 30, 2: 45})
        elif sku_item_type == 'C':
            checkout_cost += 20*sku_count
        elif sku_item_type == 'D':
            checkout_cost += 15*sku_count
        elif sku_item_type == 'E':
            checkout_cost += 40*sku_count
            
            # if elidgble for free B, then reduce only if already buying B
            free_b_count = sku_count // 2
            sku_counter['B'] = 0 if sku_counter['B'] < free_b_count else sku_counter['B'] - free_b_count

        elif sku_item_type == 'F':
            pass


    return checkout_cost




