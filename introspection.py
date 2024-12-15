import inspect


def introspection_info(obj):
    attrs = [x for x in dir(obj) if not callable(getattr(obj, x))]
    methods = [x for x in dir(obj) if callable(getattr(obj, x))]
    non_dunder_methods = [x for x in dir(obj) if callable(getattr(obj, x)) and not x.startswith('__')]
    return (f'type: {type(obj)}\n'
            f'all attributes and methods({len(dir(obj))}): {dir(obj)}\n'
            f'attributes({len(attrs)}): {attrs}\n'
            f'methods({len(methods)}): {methods}\n'
            f'non dunder methods ({len(non_dunder_methods)}): {non_dunder_methods}\n'
            f'module: {inspect.getmodule(obj)}'
            )


number_info = introspection_info(42)
print(number_info)
