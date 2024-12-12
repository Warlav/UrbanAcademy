import inspect


def introspection_info(obj):
    attr = []
    meths = []
    for i in dir(obj):
        # print(i, type(getattr(obj, i)))
        if inspect.ismethod(i):
            meths.append(i)

    return f'type: {type(obj)}, attributes: {attr}, methods: {meths}, module: {inspect.getmodule(obj)}'


number_info = introspection_info(42)
print(number_info)
