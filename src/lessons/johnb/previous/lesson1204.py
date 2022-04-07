def dosomething(name, type="y", *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)

dosomething("xx", type=0, 9, 3, 2, 1, 2, a=5, b=9, c=10)
