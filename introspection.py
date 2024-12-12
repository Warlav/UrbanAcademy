import inspect


def introspection_info(obj):
    meths = [x for x in dir(obj) if callable(x)]
    return f'type: {type(obj)}, attributes: {dir(obj)}, methods: {meths}, module: {inspect.getmodule(obj)}'


number_info = introspection_info(42)
print(number_info)
