text = input("Input:" )

def remove_vowels_loop(text):
    vowels="aeiouAEIOU"
    result=""
    for char in text:
        if char not in vowels:
            result += char
    return result

print (f"Output: {remove_vowels_loop(text)}")