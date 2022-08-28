# Implement jar in which to store cookies with a class called Jar with these
# methods:

# __init__ should initialize a cookie jar with the given capacity,
# representing the maximum number of cookies that can fit.
# If capacity is not a non-negative int, though,
# __init__ should instead raise a ValueError.

# __str__ should return a str with  🍪, where  is the number of cookies in
# the cookie jar.
# For instance, if there are 3 cookies in the cookie jar, then str
# should return "🍪🍪🍪"

# deposit() should add n cookies to the cookie jar.
# If adding that many would exceed the cookie jar’s capacity,
# though, deposit should instead raise a ValueError.

# withdraw should remove n cookies from the cookie jar.
# Nom nom nom. If there aren’t that many cookies in the cookie jar, though,
# withdraw should instead raise a ValueError.

# capacity should return the cookie jar’s capacity.
# size should return the number of cookies actually in the cookie jar.

# Structure your class per \below do not alter the methods’ parameters,
# but you may add your own methods.

# class Jar:
#     def __init__(self, capacity=12):
#         ...

#     def __str__(self):
#         ...

#     def deposit(self, n):
#         ...

#     def withdraw(self, n):
#         ...

#     @property
#     def capacity(self):
#         ...

#     @property
#     def size(self):
#         ...

# class Jar:
#     # __init__ initialize cookie jar with given capacity,
#     #  maximum number of cookies.
#     # If capacity not a positive int,raise a ValueError.
#     def __init__(self, capacity = 12):
#         if capacity < 0:
#             raise ValueError
#         self.capacity = capacity
#         self.size = 5

#     # __str__ return str with  number of cookie 🍪 in jar.
#     # For instance, if 3, return "🍪🍪🍪"
#     def __str__(self):
#         result = self.size * "🍪"
#         return f"Cookies {result}"

#     # deposit() add n cookies to t jar.
#     # If exceed jar’s capacity, raise a ValueError.
#     def deposit(self, n):
#         self.size += n
#         if self.size > self.capacity:
#             raise ValueError("ValuError")
#         else:
#             return self.size

#     # withdraw remove n from jar.
#     # If not enough cookies in jar, though, raise a ValueError.
#     def withdraw(self, n):
#         self.size -= n
#         if self.size < 0:
#             raise ValueError("ValuError")
#         else:
#             return self.size

#     # capacity should return the cookie jar’s capacity.
#     @property
#     def capacity(self):
#         return self._capacity

#     @capacity.setter
#     def capacity(self, capacity):
#             if capacity < 0:
#                 raise ValueError
#             self._capacity = capacity

#     # size return number of cookies actually in  jar.
#     @property
#     def size(self):
#         return self._size

#     @size.setter
#     def size(self, size):
#         if self.size < 0:
#             raise ValueError("ValuError")
#         elif self.size > self.capacity:
#             raise ValueError("ValuError")
#         self._size = size


################################################################
class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        """if self._size == 0:
            return f"Cookies 0 🍪"  # this is what caused the zero cookie
                                    # error."""
        result = self._size * "🍪"  # 0 returns no 🍪
        return result

    def deposit(self, n):
        if self._size + n > self.capacity:
            raise ValueError('Cannot exeed the capacity')
        self._size += n
        print(n, "cookies deposited")
        return self._size

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        else:
            self._size -= n
        print(n, "cookies withdrawn")
        return self._size

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError('value must be >= 0')
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size


def main():
    """here is how it works"""
    jar = Jar()
    jar.deposit(10)
    print(jar.size, jar)
    jar.withdraw(10)
    print(jar.size, jar)


if __name__ == "__main__":
    main()

"""Note! a variable called size and a function called size() have
the same variable name. The one which is defined last takes precedence.
That is why the variable needs to be called _size. Note that it must
be called that everywhere. Except is it is used as a paremter to a function
as in ekine 152"""
