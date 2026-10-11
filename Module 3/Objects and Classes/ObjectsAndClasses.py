class C(object):
    arg2="Test"
    # Constructor
    def __init__(self, arg = None):
        self.arg = arg

    def fun(self):
        return self

obj = C()
print(obj.arg)
obj.arg = 2
print(obj.arg)
print(obj.fun())
obj = C("New")
print(obj.arg)
print(obj.arg2)
