text = "Cupcake ipsum dolor sit amet. I love caramels topping soufflé I love. Powder oat cake cupcake muffin " \
       "fruitcake topping. Pudding macaroon lollipop gummi bears sesame snaps chocolate cake sweet. Cupcake oat cake " \
       "candy carrot cake chocolate bar sweet roll danish. Gummi bears topping sugar plum cheesecake sweet roll " \
       "pastry pie."

fourth = 4
third = 3

for index, char in enumerate(text):
    if (index + 1) % third == 0:
        print(char.upper(), end="")
    elif (index + 1) % fourth == 0:
        print(f"{char}!", end="")
    else:
        print(char, end="")
