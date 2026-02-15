#Task-1
shopping_list = [
    {"item": "Milk", "price": 50},
    {"item": "Bread", "price": 30},
    {"item": "Eggs", "price": 60},
    {"item": "Rice", "price": 120}
]
shopping_list.append({"item":"Butter","price":80})
shopping_list.pop(0)
print("No of items:",len(shopping_list))

#Task-2
total_cost=0
expensive_item=""
expensive_item_cost=0
for items in shopping_list:
    total_cost+=items["price"]
    if items["price"]>expensive_item_cost:
        expensive_item=items["item"]
        expensive_item_cost=items["price"]
print(f"Expensive Item Name:{expensive_item}")
print(f"Expensive item cost:{expensive_item_cost}")
print(f"Total Items cost:{total_cost}")

#Task-3
avg=total_cost/len(shopping_list)
summary={
    "total_items":len(shopping_list),
    "total_cost":total_cost,
    "Average_price":round(avg,2)
}
print(summary)
