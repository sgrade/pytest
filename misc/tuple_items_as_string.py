

def my_func():
    lst = ('localhost', [], ['127.0.0.1'])
    return ', '.join(str(s) for s in lst)


print(my_func())
