vowels = ['a', 'e', 'i', 'o', 'u']
text = "Cupcake ipsum dolor sit amet. I love caramels topping soufflé I love. Powder oat cake cupcake muffin " \
       "fruitcake topping. Pudding macaroon lollipop gummi bears sesame snaps chocolate cake sweet. Cupcake oat cake " \
       "candy carrot cake chocolate bar sweet roll danish. Gummi bears topping sugar plum cheesecake sweet roll " \
       "pastry pie."

total_vowels = 0
for vowel in vowels:
    total_vowels += text.count(vowel)

print(total_vowels)

