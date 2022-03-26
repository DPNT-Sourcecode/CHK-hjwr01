

class SkuItem():
    def __init__(self, id, lookup, other_offers=None) -> None:
        self._id = id
        self._lookup = lookup
        self._unrelated_offers = other_offers if other_offers is not None else {}

    def _calc_free_unrealted_items(self, count):
        res = {}
        for other_id, other_count in self._unrelated_offers.items():
            if other_id == self._id:
                continue
            # count how many free there should be
            res[other_id] = count//other_count
        return res
    
    def calculate_cost(self, items_count: int) -> int:
        items_cost = 0

        if self._id in self._unrelated_offers:
            # check how many free Fs by checking groups of (2+1)
            offer_counts = items_count // (self._unrelated_offers[self._id] + 1)
            # apply cost with reduced effective count
            items_cost += self._lookup[1]*(items_count - offer_counts)
        else:
            remaining_count = items_count
            offer_amounts = list(self._lookup.keys())
            offer_amounts.sort(reverse=True)

            for offer_units in offer_amounts:
                offer_collection_price = self._lookup[offer_units]
                
                speacials_count = remaining_count // offer_units
                remaining_count = remaining_count % offer_units

                items_cost += speacials_count*offer_collection_price
            
            assert remaining_count == 0
        print(f"items_cost {self._id}", items_cost)
        return items_cost, self._calc_free_unrealted_items(items_count)
