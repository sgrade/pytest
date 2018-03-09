# https://www.codementor.io/sheena/essential-python-interview-questions-du107ozr6

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
print('A0:', A0)
# A0 {'d': 4, 'b': 2, 'e': 5, 'c': 3, 'a': 1}

A1 = range(10)
print('A1:', A1)
# A1: range(0, 10)
# or [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] in python 2

A2 = sorted([i for i in A1 if i in A0])
print('A2:', A2)
# A2: []

A3 = sorted([A0[s] for s in A0])
print('A3:', A3)
# A3: [1, 2, 3, 4, 5]

A4 = [i for i in A1 if i in A3]
print('A4:', A4)
# A4: [1, 2, 3, 4, 5]

A5 = {i:i*i for i in A1}
print('A5:', A5)
# {0:0, 1:1, 2:4, 3:9, ..., 9:81}
# A5: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

A6 = [[i,i*i] for i in A1]
print('A6:', A6)
# [[0, 0], [1, 1], [2, 4], ..., [9, 81]]
# A6: [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]


print('##########')
# Question 6

def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

f(2)
f(3,[3,2,1])
f(3)


l=[]
for i in range(3):
    l.append(i*i)
    print(l)


print('#################')
class MyClass(object):
    def __init__(self):
        self._some_property = "properties are nice"
        self._some_other_property = "VERY nice"
    def normal_method(*args,**kwargs):
        print("calling normal_method({0},{1})".format(args,kwargs))
    @classmethod
    def class_method(*args,**kwargs):
        print("calling class_method({0},{1})".format(args,kwargs))
    @staticmethod
    def static_method(*args,**kwargs):
        print("calling static_method({0},{1})".format(args,kwargs))
    @property
    def some_property(self,*args,**kwargs):
        print("calling some_property getter({0},{1},{2})".format(self,args,kwargs))
        return self._some_property
    @some_property.setter
    def some_property(self,*args,**kwargs):
        print("calling some_property setter({0},{1},{2})".format(self,args,kwargs))
        self._some_property = args[0]
    @property
    def some_other_property(self,*args,**kwargs):
        print("calling some_other_property getter({0},{1},{2})".format(self,args,kwargs))
        return self._some_other_property

o = MyClass()
# undecorated methods work like normal, they get the current instance (self) as the first argument

o.normal_method
# <bound method MyClass.normal_method of <__main__.MyClass instance at 0x7fdd2537ea28>>

o.normal_method()
# normal_method((<__main__.MyClass instance at 0x7fdd2537ea28>,),{})

o.normal_method(1,2,x=3,y=4)
# normal_method((<__main__.MyClass instance at 0x7fdd2537ea28>, 1, 2),{'y': 4, 'x': 3})

# class methods always get the class as the first argument

o.class_method
# <bound method classobj.class_method of <class __main__.MyClass at 0x7fdd2536a390>>

o.class_method()
# class_method((<class __main__.MyClass at 0x7fdd2536a390>,),{})

o.class_method(1,2,x=3,y=4)
# class_method((<class __main__.MyClass at 0x7fdd2536a390>, 1, 2),{'y': 4, 'x': 3})


