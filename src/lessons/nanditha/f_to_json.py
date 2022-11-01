def secret_function():
    return "Secret key is 1234"


def function_creator():
    # expression to be evaluated
    expr = input("Enter the function(in terms of x):")

    # variable used in expression
    x = int(input("Enter the value of x:"))

    # passing variable x in safe dictionary
    safe_dict['x'] = x

    # evaluating expression
    y = eval(expr, {}, safe_dict)

    # printing evaluated result
    print("y = {}".format(y))


if __name__ == "__main__":

    # list of safe methods
    safe_list = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos',
                 'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor',
                 'fmod', 'frexp', 'hypot', 'ldexp', 'log', 'log10',
                 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt',
                 'tan', 'tanh']

    # creating a dictionary of safe methods
    safe_dict = {}
    for safe_key in safe_list:
        safe_dict[safe_key] = locals().get(safe_key)

    function_creator()
