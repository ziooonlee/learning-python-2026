def main():

    fruits = {
        "Apple": 130,
        "Avocado": 50,
        "Sweet Cherries": 100,
}

    item = input("Item:" ).title()

    if item in fruits:
        print(f"Calories:" , fruits[item])
 
    
main()