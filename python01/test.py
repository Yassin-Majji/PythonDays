class A:
    def f():
        print("hHHH")

class c(A):
    def f():
        print("hello")


class B(c, A):
    def g():
        print("how are you")

class D(B, c):
    def  H():
        print("hi")




print(D.__dict__)