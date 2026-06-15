# """
# g2 total = g1 total - cho left + choc enter
# g2 = 12 - 2 + 1
# 11
# """
def best_choclates(prices, window_size):
    current_total = sum(prices[0:window_size])
    best_total =  current_total

    print(f"window 1 : {prices[0:window_size]} = (current_total)")

    for i in range(window_size, len(prices)):
        left_chocolate = prices[i - window_size]
        rigth_chocolate = prices[i]

        current_total = current_total - left_chocolate + right_chocolate 
        
        window = prices[i - window-size + 1 : i + 1]
        print(f"window: {window} = {current_total}")

        if current_total>best_total:
            best_total = current_total

    return best_total

prices = [2,4,5,6,7,8,9]
answer = best_chocolates(prices, 6)
print("best total", answer)



