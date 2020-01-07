'''
In simplest terms, a Closure is a function returned by a higher order function, whose return value depends on the data associated with the higher order function.
'''
def multiple_of(x):
    def multiple(y):
        return x*y
    return multiple
c1 = multiple_of(5)  # 'c1' is a closure
c2 = multiple_of(6)  # 'c2' is a closure
print(c1(4))
print(c2(4))

'''
> Decorators are evolved from the concept of closures.

> A decorator function is a higher order function that takes a function as an argument and returns the inner function.

> A decorator is capable of adding extra functionality to an existing function, without altering it.

> The decorator function is prefixed with @ symbol and written above the function definition.
'''


def outer(func):
    def inner():
        print("Accessing :", 
                  func.__name__)
        return func()
    return inner
def greet():
   print('Hello!')
wish = outer(greet)
wish()

