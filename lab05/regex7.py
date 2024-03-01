def snake_to_camel(snake_case):
    words = snake_case.split('_')
    camel_case = words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel_case

snake_case_string = 'your_snake_case_string'
camel_case_string = snake_to_camel(snake_case_string)
print(camel_case_string)
