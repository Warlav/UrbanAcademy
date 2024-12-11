def introspection_info(obj):
    return f'type: {type(obj)}, attributes: {dir(obj)}'

number_info = introspection_info(42)
print(number_info)