def a_new_decorator(a_func):

    def wrap_the_func():
        print("I am doing some boring work before executing a_func")

        a_func()

        print("I am doing some boring work after executing a_func")
    return wrap_the_func


def a_function_requiring_decoration():
    print("I am the function which needs some decoration")


# a_function_requiring_decoration()
#
# a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
#
# a_function_requiring_decoration()


"""
    Adding another decorator function 
    date: 08-10-2018
"""


def decorator_function(original_function):
    def wrapper_function():
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function


@decorator_function
def display():
    print("Display method ran")


decorated_display = decorator_function(display)
#print(decorated_display)
#print(decorated_display())

display()

