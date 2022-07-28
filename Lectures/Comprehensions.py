
numbers = [i for i in range(1, 5+1)] # create list numbers with comprehention
print(numbers)

sq = [i ** 2 for i in range(1, 5+1)] # create list numbers**2 with comprehention
print(sq) 

numbers = [1, 4, 1, 3, 2, 5, 2, 6]
sq = {i ** 2 for i in numbers} # create set numbers**2 with comprehention
print(sq)   # {1, 4, 36, 9, 16, 25}

numbers = [1, 4, 1, 3, 2, 5, 2, 6]
sq = {i: i ** 2 for i in numbers} # create dict numbers**2 with comprehention
print(sq)   # {1: 1, 4: 16, 3: 9, 2: 4, 5: 25, 6: 36}