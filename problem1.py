def compose_map(fun1, fun2, L):
    """
    Returns a new list R where each element in R is fun2(fun1(i)) for the
    corresponding element i in L
    :param fun1: function
    :param fun2: function
    :param L: list
    :return R: list
    """

    return [fun2(el2) for el2 in [fun1(el1) for el1 in L]]


def triple_map(fun, L):
    """
    Returns a new list R where each element in R is fun(fun(fun(i))) for the
    corresponding element i in L
    :param fun: function
    :param L: list
    :return R: list
    """
    return [fun(i3) for i3 in [fun(i2) for i2 in [fun(i) for i in L]]]


def compose(fun1, fun2):
    """
    Returns a new function ret_fun. ret_fun should take a single input i, and return
    fun1(fun2(i))
    :param fun1: function
    :param fun2: function
    :return ret_fun: function
    """
    def ret_fun(i):
        return fun1(fun2(i))
    return ret_fun


def repeater(fun, num_repeats):
    """
    Returns a new function ret_fun. ret_fun should take a single input i, and return
    fun applied to i num_repeats times. In other words, if num_repeats is 1, ret_fun
    should return fun(i). If num_repeats is 2, ret_fun should return fun(fun(i)). If
    num_repeats is 0, ret_fun should return i.
    :param fun: function
    :param num_repeats: int
    :return ret_fun: function
    """
    def ret_fun(x):
        for i in range(num_repeats):
            x = fun(x)
        return x
    return ret_fun


if __name__ == '__main__':

    def test1(x):
        return x * 2

    def test2(x):
        return x - 3

    data = [2, 5, -10, -7, -7, -3, -1, 9, 8, -6]

    # Testing the compose_map function
    print(compose_map(test1, test2, data)) # Calling the compose_map fuction with fuctions test1, test2 and the list data as the argument

    print(compose_map(test2, test1, data)) # Calling the compose_map fuction with fuctions test2, test1 and the list data as the argument (order of function input changed)

    # Testing the triple_map function
    print(triple_map(test1, data)) # Calling the triple_map fuction with fuction test1 and the list data as the argument

    # Using the compose fuction with functions test1 and test2 as arguments and returning its value to f1
    f1 = compose(test1, test2)

    # Running f1 with i=4
    print(f1(4))


    # The map function below is an in-built function in python 
    # that applies the first argument (a function) on to each element of the second argument (a list) 
    # Note that the output will not be a list but an intermediate datatype that needs to be converted to a list
    # i.e. list(map(f1, data)) will return a list equivalent to [f1(data[0]), f1(data[1]), ..., f1(data[len(data)-1])]
    
    print(list(map(f1, data)))

    # Using the compose fuction with functions test2 and test1 as arguments and returning its value to f2
    f2 = compose(test2, test1)

    # Running f2 with i=4
    print(f2(4)) 

    # Applying f2 on to each value in the list data
    print(list(map(f2, data)))


    # Testing the repeater function that with the function test1 with different num_repreats argument.
    z = repeater(test1, 0)
    once = repeater(test1, 1)
    twice = repeater(test1, 2)
    thrice = repeater(test1, 3)

    print("repeat 0 times: {}".format(z(5)))
    print("repeat 1 time: {}".format(once(5)))
    print("repeat 2 times: {}".format(twice(5)))
    print("repeat 3 times: {}".format(thrice(5)))
