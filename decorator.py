def my_decorator(func):
    def wrappers():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrappers

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
