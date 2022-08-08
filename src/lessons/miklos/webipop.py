#  pip install pywebio

from pywebio.input import input_group
from pywebio.input import FLOAT
from pywebio.input import input
from pywebio.input import NUMBER
from pywebio.output import put_text


def qanda():
    data = input_group("Basic info", [
        input('Input your name', name='name'),
        input('Input your age', name='age', type=NUMBER),
        input('Input your fav color', name='fav')
    ])
    put_text(data['name'])
    put_text(data['fav'])

    height = input("Your Height(in)：", type=FLOAT)
    weight = input("Your Weight(lbs)：", type=FLOAT)
    message = data['name'] + " is " + str(height) + \
        " inches tall and weighs " + str(weight) + " lbs."

    put_text(message)


if __name__ == '__main__':
    qanda()
