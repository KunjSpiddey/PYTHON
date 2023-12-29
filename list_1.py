emptyList = [] # 1 ...
itemList5 = ["Kunj" , "28-11-2004" , "Charusat" , "Kiwi" , "D23CE160"] # 2 ...
print(len(itemList5)) # 3 ...
print(f"First item: {itemList5[0]}, Last item: {itemList5[-1]}, Middle item: {itemList5[len(itemList5) // 2]}") # 4 ...
mixed_data_types = ["Kunj" , 20 , 6.00 , "Un-Married" , "Junagadh"] # 5...
it_companies = ["Facebook" , "Google" , "Microsoft" , "Apple" , "IBM" , "Oracle" , "Amazon"] # 6...
print(it_companies) # 7 ...
print(len(it_companies)) # 8 ...
print(f"First Company: {it_companies[0]}, Middle Company: {it_companies[len(it_companies) // 2]} , Last Company: {it_companies[-1]}") # 9 ...
it_companies[0] = "Reliance" # 10 ...
it_companies.append("TCS") # 11 ...
it_companies.insert(len(it_companies) // 2 + 1, "Wipro") # 12 ...
print(it_companies[1].upper()) # 13 ...
print('#'.join(it_companies)) # 14 ...
if "Apple" in it_companies:
    print("Apple Exist in the list")
else:
    print("Apple doesn't Exist in the list") # 15 ...
it_companies.sort() # 16 ...
it_companies.reverse() # 17 ...
print(it_companies[0:2]) # 18 ...
print(it_companies[-3:-1]) # 19 ...
if len(it_companies) % 2 != 0:
    print(it_companies[len(it_companies) // 2]) # 20 ...
print(it_companies.pop(0)) # 21 ...
print(it_companies.pop(len(it_companies) // 2)) # 22 ...
print(it_companies.pop(-1)) # 23 ...
print(it_companies) # 24 ...
del it_companies # 25 ...
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end # 26 ...
full_stack.insert(full_stack.index('Redux') + 1, "Python")
full_stack.insert(full_stack.index('Redux') + 2, "SQL")  # 27 ...
print(full_stack)