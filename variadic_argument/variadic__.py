def adder( **num ):
    sum = 0

    for n in num:
        sum = sum + n

    print("SUM", sum)

# variadic argument for potional parameter
adder(1,2,3,4)
adder(1,2)