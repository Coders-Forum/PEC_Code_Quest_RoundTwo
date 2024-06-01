def calculate_cake_weight(budget):
    # Calculate the weight of cake in kg
    effective_cost = budget / 1.2
    weight_in_kg = (effective_cost - 50) / 500
    
    # Truncate to integer
    weight_in_kg = int(weight_in_kg)
    
    # Ensure the weight is not negative
    if weight_in_kg < 0:
        weight_in_kg = 0
    
    return weight_in_kg

# Read input
budget = int(input().strip())

# Calculate and print the weight of the cake
print(calculate_cake_weight(budget))
