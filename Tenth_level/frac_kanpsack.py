def fractional_knapsack(items, capacity):
    """
    items: list of (value, weight) tuples
    capacity: total weight the knapsack can hold
    returns: max total value (float)
    """
    items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)
    #sort descending order
    
    total_value = 0.0
    remaining = capacity
    
    for value, weight in items:
        if remaining <= 0: #filled
            break
        if weight <= remaining: #if not filled and less amount, add
            total_value += value
            remaining -= weight
        else:
            fraction = remaining / weight #if the amount is more, fraction of it
            #needs to be added.
            total_value += value * fraction
            remaining = 0#added everything so made it 0
    
    return total_value

items = [
    (10, 2),   # value=10, weight=2 -> ratio=5
    (5, 3),    # ratio=1.67
    (15, 5),   # ratio=3
    (7, 7),    # ratio=1
    (6, 1),    # ratio=6
    (18, 4),   # ratio=4.5
    (3, 1),    # ratio=3
]
capacity = 15

print(fractional_knapsack(items, capacity))