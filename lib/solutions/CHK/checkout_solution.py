from collections import defaultdict
from .sku_item import SkuItem

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


def prepare_sku_items():
    return {
        # these must go first
        "E": SkuItem("E", {1: 40}, {"B": 2}),
        "R": SkuItem("R", {1: 50}, {"Q": 3}),
        "N": SkuItem("N", {1: 40}, {"M": 3}),

        # these are lower priority
        "A": SkuItem("A", {1: 50, 3: 130, 5:200}),
        "B": SkuItem("B", {1: 30, 2: 45}),
        "C": SkuItem("C", {1: 20}),
        "D": SkuItem("D", {1: 15}),
        
        "F": SkuItem("F", {1: 10}, {"F": 2}),
        "G": SkuItem("G", {1: 20}),
        "H": SkuItem("H", {1: 10, 5: 45, 10:80}),
        "I": SkuItem("I", {1: 35}),
        "J": SkuItem("J", {1: 60}),
        "K": SkuItem("K", {1: 80, 2: 150}),
        "L": SkuItem("L", {1: 90}),
        "M": SkuItem("M", {1: 15}),
        
        "O": SkuItem("O", {1: 10}),
        "P": SkuItem("P", {1: 50, 5: 200}),
        "Q": SkuItem("Q", {1: 30, 3: 80}),
        
        "S": SkuItem("S", {1: 20}),
        "T": SkuItem("T", {1: 20}),
        "U": SkuItem("U", {1: 40}, {"U": 3}),
        "V": SkuItem("V", {1: 50, 2: 90, 3:130}),
        "W": SkuItem("W", {1: 20}),
        "X": SkuItem("X", {1: 17}),
        "Y": SkuItem("Y", {1: 20}),
        "Z": SkuItem("Z", {1: 21}),
    }


def calculate_group_discount_offer_cost(sku_counter: dict,) -> int:
    # we want to benfit the customer, so order by priority of price
    # hard coded atm - TODO make not hard coded..
    total_cost = 0
    members = ["Z", "Y", "S", "T", "X"]

    total_count = sum([sku_counter[sku] for sku in members])
    total_speacials = total_count // 3
    total_cost += 45*total_speacials

    # calcualte remaining cost by priority
    remainer_count = total_count % 3
    for item_type in members:



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
    sku_items = prepare_sku_items()
    

    # edge case wher no items
    if not skus:
        return 0

    # process input string and bin values
    for sku_item in skus:
        # check if illegal item type
        if sku_item not in sku_items.keys():
            return -1
        sku_counter[sku_item] += 1

    
    # go through each bin and find associated cost for each item type
    for sku_item_type in sku_items.keys():
        sku_count = sku_counter[sku_item_type]
        cost_item_type, unrelated_free_items = sku_items[sku_item_type].calculate_cost(sku_count)
        checkout_cost += cost_item_type
        for item_t, item_c in unrelated_free_items.items():
            sku_counter[item_t] = 0 if sku_counter[item_t] < item_c else sku_counter[item_t] - item_c

    return checkout_cost
