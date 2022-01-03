class Person():
    pass


class Professional(Person):
    pass


def main():
    person = Person()
    professional = Professional()

    assert isinstance(person, Person) is True
    assert isinstance(professional, Professional) is True
    assert isinstance(professional, Person) is True
    assert str(type(person)) == "<class '__main__.Person'>"
    assert str(type(professional)) == "<class '__main__.Professional'>"
    assert str(type(professional)) != "<class '__main__.Person'>"


if __name__ == "__main__":
    main()
