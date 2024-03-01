import re

def camel_to_snake(camel_case):
    snake_case = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', camel_case).lower()
    return snake_case

camel_case_string = 'yourCamelCaseString'
snake_case_string = camel_to_snake(camel_case_string)
print(snake_case_string)
