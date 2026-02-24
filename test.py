class A:
    def f1(self):
        self.name = "yassin"
        self.f(self)


def f2(self):
    print(f"i am {self.name}")


ob = A()

ob.f = f2
ob.f1()