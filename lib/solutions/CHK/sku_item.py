

class SkuItem():
    def __init__(self, id, lookup) -> None:
        self.id = id
        self.lookup = lookup

        self._depends = {}

    
    def cost_by_item_type(self, items_count: int) -> int:
        items_cost = 0
        remaining_count = items_count

        offer_amounts = list(self.lookup.keys())
        offer_amounts.sort(reverse=True)

        for offer_units in offer_amounts:
            offer_collection_price = self.lookup[offer_units]
            
            speacials_count = remaining_count // offer_units
            remaining_count = remaining_count % offer_units

            items_cost += speacials_count*offer_collection_price
        
        assert remaining_count == 0
        return items_cost