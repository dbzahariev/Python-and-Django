fruits = {"banana", "apple", "kiwi", "cherry", "lemon", "grapes"}
vegetables = {"tomato", "cucumber", "pepper", "carrot"}

target = input()
result = "unknown"
if target in fruits:
    result = "fruit"
elif target in vegetables:
    result = "vegetable"
print(result)
