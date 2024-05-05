# solve knapsack problem using backtracking 

def knapsack(items, capacity):
    def backtrack(index, current_weight, current_value):
        if current_weight > capacity:
            return 0
        if index == len(items):
            return current_value
        # Exclude the current item
        value_without = backtrack(index + 1, current_weight, current_value)
        # Include the current item
        value_with = 0
        if current_weight + items[index][1] <= capacity:
            value_with = backtrack(index + 1, current_weight + items[index][1], current_value + items[index][0])
        return max(value_with, value_without)

    return backtrack(0, 0, 0)

# Example usage
items = [(value1, weight1), (value2, weight2), ...]  # List of tuples (value, weight)
capacity = 50  # Total capacity of the knapsack
print(knapsack(items, capacity))