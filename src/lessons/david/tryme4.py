def nine_lines():
    print("calling nine_lines")

    def three_lines():
        def new_line():
            print(".")

        new_line()
        new_line()
        new_line()

    three_lines()
    three_lines()
    three_lines()


def clear_screen():
    print("calling clear_screen")

    def nine_lines():
        def three_lines():
            def new_line():
                print(".")

            new_line()
            new_line()
            new_line()

        three_lines()
        three_lines()
        three_lines()

    nine_lines()
    nine_lines()

    def three_lines():
        def new_line():
            print(".")

        new_line()
        new_line()
        new_line()

    three_lines()
    three_lines()

    def new_line():
        print(".")

    new_line()
