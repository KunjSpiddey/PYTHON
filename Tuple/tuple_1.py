# Create an empty tuple
tup = ()


# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sister = ("Monica" , "Phoebe" , "Rachel" , "Jenice")
brother = ("Chandler" , "Joey" , "Ross", "Gunther")


# Join brothers and sisters tuples and assign it to siblings
siblings = sister + brother


# How many siblings do you have?
print(len(siblings))


# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = ("Severus Snape" , "Lily") + siblings
print(family_members)


# Unpack siblings and parents from family_members
Father, Mother, *Siblings = family_members
print("Father: " + Father + " \nMother: " + Mother + " \nSiblings: " + str(Siblings))


# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
Fruits = ("Mango", "Apple", "Kiwi", "Starfruit", "Melon")
Vegetables = ("Potato", "Tomato", "Bottle-Guard", "Zucchini")
Animal_Products = ("Milk", "Cheese", "Butter", "Yogurt")


food_stuf_tp = Fruits + Vegetables + Animal_Products
print(food_stuf_tp)


# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_staff_lt = list(food_stuf_tp)


# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(food_stuf_tp[len(food_stuf_tp) // 2])
print(food_staff_lt[len(food_staff_lt) // 2])


# Slice out the first three items and the last three items from food_staff_lt list
print(food_staff_lt[:3])
print(food_staff_lt[-3:])


# Delete the food_staff_tp tuple completely
del food_stuf_tp
# print(food_stuf_tp) ---> execution will stop coz' --- in LOC 53 we deleted the food_stuff_tp


# Check if an item exists in tuple:
print('Cheese' in food_staff_lt)


# Check if 'Estonia' is a nordic country
Nordic_Countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Is Estonia a Nordic country", 'Estonia' in Nordic_Countries)


# Check if 'Iceland' is a nordic country
print("Is Iceland a Nordic country", 'Iceland' in Nordic_Countries)
