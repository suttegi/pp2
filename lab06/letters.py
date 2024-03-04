def count_upper_lower(string):
    upper_count = sum(map(str.isupper, string))
    lower_count = sum(map(str.islower, string))
    return upper_count, lower_count

input_string = input()
upper, lower = count_upper_lower(input_string)

print(upper)
print(lower)