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