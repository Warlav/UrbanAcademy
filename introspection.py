import inspect


def introspection_info(obj):
    attr = [getattr(obj, x) for x in dir(obj) if hasattr(obj, x)]
    meths = [x for x in dir(obj) if callable(x)]
    return f'type: {type(obj)}, attributes({len(attr)}): {attr}, methods({len(meths)}): {meths}, module: {inspect.getmodule(obj)}'


number_info = introspection_info(42)
print(number_info)
