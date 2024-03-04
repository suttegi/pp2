from functools import reduce
numbers_input = input()
numbers = list(map(int, numbers_input.split()))
result = reduce(lambda x,y:x * y,numbers)
print(result)
