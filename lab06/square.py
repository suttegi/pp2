import time
from math import sqrt

def calculate_square_root(number):
    start_time = time.time() * 1000
    result = sqrt(number)
    end_time = time.time() * 1000
    elapsed_time = end_time - start_time
    return result, elapsed_time

number = int(input())
result, elapsed_time = calculate_square_root(number)
print(f"Square root of {number} after {elapsed_time:.0f} milliseconds is {result}")