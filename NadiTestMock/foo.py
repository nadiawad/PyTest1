from old import Old

class Foo:

    def __init__(self, old1):
        self.old1 = old1

    def method_1(self):
        results = self.old1.returnX()
        return results

#old1 = Old(5)
#foo1 = Foo(old1)
#print foo1.method_1()