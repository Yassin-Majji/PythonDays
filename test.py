class   A(Exception):
   def __str__(self):
      return "yaaaaaaassssssssssssssiiiiiiiiiiiiin"



def f(height):
   if (height < 50):
      raise A()

def g():
   height = 10
   try:
      f(height)

   except A as e:
      print(e)

      
g()