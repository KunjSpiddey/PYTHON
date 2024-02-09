# 1. Reverse the given string (You can take any string)

a = "Kunj is pursuing B.Tech"
print(a[::-1])

# 2. Replace some character of the string with another character without using a loop.
a = a.replace("Kunj", "Kunj Koradiya")
print(a)

# 3. Find whether the character in the given string or not.
if 'K' in a:
    print("Yes")
else:
    print("No")

# 4. Create tuple, list and set and convert them into the different strings.

a_tuple = ('Kunj', 6356365709, 'Koradiya')
b_list = ['Kunj', 6356365709, 'Koradiya']
c_set = {'Kunj', 6356365709, 'Koradiya'}

print(str(a_tuple))
print(str(b_list))
print(str(c_set))

# 5. Convert all the string characters to the upper and the lower case and split it with the different methods.

print(a.upper())
print(a.lower())

print(a.split(" "))
print(list(a))
print([char for char in a if char != ' '])

# 6. Perform the following operations to the tuple and the list Find max, min, len, sum
tup = (1,2,3,4,5,6)
lst = [1,2,3,4,5,6]

print("Max",max(tup),"Min",min(tup),"lenght",len(tup),"Sum",sum(tup))
print("Max",max(lst),"Min",min(lst),"lenght",len(lst),"Sum",sum(lst))

# 7. Copy one list to the another list without using the copy command.

org_list = [1,2,3,4]
cpy_list = org_list[:]

print(cpy_list)

# 8. Perform below task as instructed
# 	-> Create a dictionary named student with keys: 'name', 'age', and 'grade'. Assign 	values accordingly.
# 	Access Dictionary Values:
#
# 	-> Print the 'age' of the student from the dictionary created in Exercise 1.
# 	Modify Dictionary Values:
#
# 	-> Update the 'grade' of the student to a new value.
#
# 	-> Check if the key 'gender' is present in the student dictionary. Print a message 	based on the result.

student = {'name': 'Kunj', 'Age': '19', 'Grade': 'AA'}
print(student['Age'])

student['Grade'] = 'AAA'
print(student['Grade'])

if 'Gender' in student:
    print("Yes")
else:
    print("No")


 # 9. Perform below task as instructed
	# -> Create two sets: set1 with elements (1, 2, 3) and set2 with elements (3, 4, 5).
	# Union of Sets:
 #
	# -> Find the union of set1 and set2 and print the result.
	# Intersection of Sets:
 #
	# -> Find the intersection of set1 and set2 and print the result.
	# Difference of Sets:
 #
	# -> Find the elements that are in set1 but not in set2 and print the result.
	# Check Subset:
#     -> Check if set1 is a subset of set2. Print a message based on the result.


set1 = {1,2,3}
set2 = {3,4,5}

print(set1|set2) # Union
print(set1&set2) # Intersection
print(set1 - set2) # Difference
print(set1.issubset(set2)) # Subset


# 10. Perform below task as instructed
# 	Create a dictionary where keys are subjects ('math', 'science') and values are sets 	of students who take those subjects.
# 	Update Set Values:
#
# 	Add a new student to the 'math' subject in the dictionary from Exercise 11.
# 	Remove Set Values:
#
# 	Remove a student from the 'science' subject in the dictionary from Exercise 11.
# 	Check Common Students:
#
# 	Find and print the students who take both 'math' and 'science'.
# 	Nested Dictionary:
#
# 	Create a nested dictionary where each key represents a country, and the value is 	another dictionary containing cities and their populations.

Education = {'math':{'Kunj','Joey','Chandler'}, 'science':{'Kunj','Micheal','Trevor'}}
Education['math'].add('Krishna')
print(Education)
Education['science'].remove('Micheal')
print(Education)
print(Education['math'] & Education['science'])


# Nested dictionary representing countries, cities, and populations
countries = {
    'India': {
        'Junagadh': 362001 ,
        'Delhi': 1122,
        'Bangalore': 123456
    },
    'USA': {
        'New York': 11,
        'Los Angeles': 22,
        'Chicago': 33
    },
    'China': {
        'Shanghai': 44,
        'Beijing': 55,
        'Guangzhou': 66
    }

}
print(countries)


# 11. Create two lists, one containing elements at even indices and the other containing elements at odd indices from the original list.
# Original dictionary from Exercise 11
student = {'name': 'John', 'age': 20, 'grade': 'A', 'science': {'Alice': {'age': 22, 'grade': 'B'}, 'Bob': {'age': 21, 'grade': 'C'}}}
if 'science' in student:
    if 'Alice' in student['science']:
        removed_student = student['science'].pop('Alice')
        print("Removed student from 'science' subject:", removed_student)
    else:
        print("Student 'Alice' not found in 'science' subject.")
else:
    print("No 'science' subject found in the dictionary.")

print("Updated dictionary:", student)

# 12. Use tuple packing and unpacking to swap the values of two variables without using a temporary variable.

a = 5
b = 10
a, b = b, a

print("a after swapping:", a)
print("b after swapping:", b)


# 13. Check if a given list is a palindrome using slicing.
def is_palindrome(lst):
    return lst == lst[::-1]

test_list1 = [1, 2, 3, 4, 5]
test_list2 = [1, 2, 3, 2, 1]

print(is_palindrome(test_list1))
print(is_palindrome(test_list2))

# 14. oncatenate two tuples without using the + operator.

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(*tuple1,*tuple2)




