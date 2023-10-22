# My first large program...I'm sure this can be condensed
# Still needs to be completed 10/20/2023 

# Create a shopping cart
# Have shopper be able to select between a basket or cart
# Have shopper be able to add item(s) from basket or cart
# Give shopper option to remove any items from basket or cart
# Have shopper check out


import sys
print()
name = input("What's your name: ")
print()

def welcome(text):
    global name
    left_margin = (80 - len(text)) // 2
    print(' ' * left_margin, text)


welcome(name + ", Welcome to International Foods!")
welcome("You will have to choose between a basket or a cart.")
welcome("Based on what you chose, you will only be able to fit ")
welcome(" so many items in your selection.  So choose wisely because")
welcome(" you will not be able to change carts!")

print()

the_cart = []
proceed = ["Y", "y", "Yes", "yes", "YES"]
stop = ["N", "n", "No", "no", "NO"]
basket_or_cart = ["Basket", "Cart"]
option = ""
basket_or_cart_selection = option.lower()


def cart_option():
    global basket_or_cart
    global option
    global basket_or_cart_selection
    option = input("Please select a Basket or Cart: ")
    basket_or_cart_selection = option.lower()
    if basket_or_cart_selection == "basket":
        print("You grabbed a " + basket_or_cart_selection + ".  Let's head in!")
    elif basket_or_cart_selection == "cart":
        print("You grabbed a " + basket_or_cart_selection + ".  Let's head in!")
    elif basket_or_cart_selection not in basket_or_cart:
        answer = input("Would you like to go back and get a basket or cart? Y/N ")
        answer = answer.lower()
        if answer in proceed:
            print("Let's go grocery shopping!")
            cart_option()
            print("Now that you've selected a cart, we can continue to shop.")
        else:
            print("I guess you're going home")
        sys.exit()


print()


vegetables = []


def vegetable_items():
    print()
    print("Let's add some vegetables!")
    global proceed
    global stop
    global vegetables
    while proceed not in stop:
        add = input("What would you like to add? ")
        print("You've added " + add + " to your " + basket_or_cart_selection + ".")
        vegetables.append(add)
        answer = input("Would you like to add more vegetables? Y/N ")
        if answer in stop:
            break
    print()
    print("These are the vegetables in your " + basket_or_cart_selection + ".")
    for i, veggies in enumerate(vegetables):
        i += 1
        print(i, veggies, sep=": ")


print()


fruit = []


def fruit_items():
    print()
    print("Now, let's add some fruit!")
    global proceed
    global stop
    global fruit
    while proceed not in stop:
        add = input("What would you like to add? ")
        print("You've added " + add + " to your " + basket_or_cart_selection + ".")
        fruit.append(add)
        answer = input("Would you like to add more? Y/N ")
        if answer in stop:
            break
    print()
    print("These are the fruits in your " + basket_or_cart_selection + ".")
    for i, fruits in enumerate(fruit):
        i += 1
        print(i, fruits, sep=": ")


print()


dairy = []


def dairy_items():
    print()
    print("Now let's add some dairy!")
    global proceed
    global stop
    global dairy
    while proceed not in stop:
        add = input("What would you like to add? ")
        print("You've added " + add + " to your " + basket_or_cart_selection + ".")
        dairy.append(add)
        answer = input("Would you like to add more? Y/N ")
        if answer in stop:
            break
    print()
    print("These are the dairy items in your " + basket_or_cart_selection + ".")
    for i, dairy_list in enumerate(dairy):
        i += 1
        print(i, dairy_list, sep=": ")


print()


meat = []


def meat_items():
    print()
    print("Now let's add some meats!")
    global proceed
    global stop
    global meat
    while proceed not in stop:
        add = input("What would you like to add? ")
        print("You've added " + add + " to your " + basket_or_cart_selection + ".")
        meat.append(add)
        answer = input("Would you like to add more? Y/N ")
        if answer in stop:
            break
    print()
    print("These are the meats in your " + basket_or_cart_selection + ".")
    for i, meats in enumerate(meat):
        i += 1
        print(i, meats, sep=": ")


print()


additional = []


def additional_items():
    print()
    print("Here is where we add other important items.")
    global proceed
    global stop
    global additional
    while proceed not in stop:
        add = input("What other item(s) would you like to add? ")
        print("You've added " + add + " to your " + basket_or_cart_selection + ".")
        additional.append(add)
        answer = input("Would you like to add anything else? Y/N ")
        if answer in stop:
            break
    print()
    print("These are the additional item(s) you added: ")
    for i, added_to_cart in enumerate(additional):
        i += 1
        print(i, added_to_cart, sep=": ")


cart_option()
vegetable_items()
fruit_items()
dairy_items()
meat_items()
additional_items()


print()
print(name + ", below is everything you have added to your " + basket_or_cart_selection + ".")
print("Vegetable(s): " + str(vegetables))
print("Fruit(s): " + str(fruit))
print("Dairy: " + str(dairy))
print("Meat(s): " + str(meat))
print("Additional Item(s): " + str(additional))
print()


cart_list = vegetables + fruit + dairy + meat + additional
decision = input("Do you want to remove anything from your " + basket_or_cart_selection + "? Y/N ")
print()

while decision != "N" or decision != "n":
    #print("Below are all your items in your " + basket_or_cart_selection + ".")
    #print(cart_list)
    if decision == "Y" or decision == "y":
        selection = input("What item would you like to remove? ")
        cart_list.remove(selection)
        print(cart_list)
        selection = input("Would you like to remove more? Y/N ")
        if selection == "Y" or selection == "y":
            print(cart_list)
            selection = input("Select another item from your cart.")
            cart_list.remove(selection)
            selection = input("Continue removing items? Y/N ")
            if selection == "N" or selection == "n":
                break
            else:
                continue
        elif selection == "N" or selection == "n":
            print("Done removing item(s).")
            print()
            print("Here is your updated " + basket_or_cart_selection + ".")
            break
    else:
        print("You did not choose to remove any items.")
        print()
        print("Here are the items in your " + basket_or_cart_selection + ".")
        break

print()

for i, cart in enumerate(cart_list):
    i += 1
    print(i, cart, sep=": ")
print()
print("Since you\'re happy with what's in your " + basket_or_cart_selection + ", it\'s time to cash out!")








