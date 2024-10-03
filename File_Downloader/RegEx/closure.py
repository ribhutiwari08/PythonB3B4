def outer_function(message):
    #value of messae is present here
    def inner_function():
        print(message)
    return inner_function

closure = outer_function("Hello From Closure")

closure()