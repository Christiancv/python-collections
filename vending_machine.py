sodas = ["Pepsi", "Coke", "Sprite"]
chips = ["Doritos","Fritos"]
candy = ["Snickers", "M&Ms", "Twizzlers"]

while True:
    choice = input("Would you like s SODA, rg
            snack = sodas.pop()
        elif choice == 'chips':
            snack = chips.pop()
        elif choice == 'candy':
            snack = candy.pop()
        else:
            print("Sorry, I didn't understand that.")
            continue
    except IndexError:
        print("We're all out of {}! Sorry".format(choice))
    else:
        print("Here's your {}: {}".format(choice, snack))

