# code a knapsack question to find the most efficient combination of coins to satisy the given amount

def knapsack(coins, amount):
    point_of_ref=amount
    sorted(coins, reverse=True)
    print(coins)
    result = []
    i=-1
    while(point_of_ref>0) and i>=-len(coins):
        if coins[i]< point_of_ref:
            result.append(coins[i])
            point_of_ref-=coins[i]
        else:
            i-=1
    
    return result

# test cases
coins=[1,2,5,10]
amount=150
print(knapsack(coins, amount)) 