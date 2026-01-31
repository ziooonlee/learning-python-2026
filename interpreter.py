math = input("Expression: " ).split(" ")

y = math[1]
x = int(math[0])
z = int(math[2])

if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z
print(result)