ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print("Min Age:", ages[0])
print("Max Age:", ages[-1])
ages.extend([ages[0], ages[-1]])

middle_index = len(ages) // 2
median_age = (ages[middle_index]) // 2

print(median_age)
print(sum(ages) / len(ages))
print(max(ages) - min(ages))

min_average_diff = abs(ages[0] - (sum(ages) / len(ages)))
max_average_diff = abs(ages[-1] - (sum(ages) / len(ages)))

country = ["India", "USA", "Germany", "Denmark", "Netherlands", "Israel"]
mid = (len(country)) // 2
if (len(country)) % 2 == 0:
    one = country[:mid]
    second = country[mid:]
else:
    country.append("BHARAT")
    one = country[:mid]
    second = country[mid:]

print(one)
print(second)
print("Middle Contry from the lst is: ", len(country) // 2)

list_country = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_half, scandic_countries = list_country[:3], list_country[3:]
print("All countriess", first_half + scandic_countries)
print(first_half)
print(scandic_countries)
