def count_items(items):
    frequency = {}

    for item in items:
        item = item.lower()
        frequency[item] = frequency.get(item, 0) + 1

    return frequency


fruits = [
    "Apple", "Banana", "Mango", "apple",
    "Orange", "banana", "Grapes", "Mango",
    "APPLE", "Orange", "Pineapple", "Grapes"
]

print(count_items(fruits))