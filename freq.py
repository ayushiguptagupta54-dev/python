todays_oreders = [
    "biryani", "dosa", "pov", "biryani", "idly", "burger"
    "dosa", "burger"
]

def count_orders(orders):
     freq = {}
     for dish in orders:
        if dish in freq:
            freq[dish] = freq[dish] + 1
        else:
            freq[dish] = 1

     return freq

result = count_orders(todays_oreders)
print(result)

