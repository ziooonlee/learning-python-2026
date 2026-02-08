def camel_to_snake(camel_case_input):
    snake_case_output = ""
    for char in camel_case_input:
        if char.isupper():
            snake_case_output += "_" + char.lower()
        else:
            snake_case_output += char
    if snake_case_output.startswith("_"):
        return snake_case_output[1:]
    else:
        return snake_case_output
    
camel_case_input = input("camelCase: ")
print(f"snake_case {camel_to_snake(camel_case_input)}")