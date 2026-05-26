shopping_list = [
    {"item": "Milk", "price": 50},
    {"item": "Bread", "price": 30},
    {"item": "Eggs", "price": 60},
    {"item": "Rice", "price": 120}
]

# Task 1
shopping_list.append({"item": "Butter", "price": 80})

shopping_list.pop(0)

print("Number of items:", len(shopping_list))

# Task 2
total_cost = sum(item["price"] for item in shopping_list)

most_expensive = max(shopping_list, key=lambda x: x["price"])

print("Most Expensive Item:", most_expensive["item"])
print("Price:", most_expensive["price"])

print("Total Cost:", total_cost)

# Task 3
summary = {
    "total_items": len(shopping_list),
    "total_cost": total_cost,
    "average_price": round(total_cost / len(shopping_list), 2)
}

print("Summary Dictionary:", summary)