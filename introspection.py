import builtins
import inspect


class Abyr:
    first = 1

    def __init__(self):
        self.second = 2

    def third(self):
        pass


def introspection_info(obj):
    # print(hasattr(obj, '__name__'))
    meths = [x for x in dir(obj) if inspect.ismethod(x)]
    return (f'type: {type(obj)}\nattributes({len(dir(obj))}): {dir(obj)}\n'
            f'methods({len(meths)}): {meths}\nmodule: {inspect.getmodule(obj)}')


fourth = Abyr()
number_info = introspection_info(fourth)
print(number_info)
print(fourth.__module__)
