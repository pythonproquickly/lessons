from pywebio.input import input, FLOAT, input_group, NUMBER
from pywebio.output import put_text

def bmi():

    data = input_group("Basic info", [
        input('Input your name', name='name'),
        input('Input your age', name='age', type=NUMBER) #, validate=check_age)
    ])
    put_text(data['name'], data['age'])

    height = input("Your Height(cm)：", type=FLOAT)
    weight = input("Your Weight(kg)：", type=FLOAT)

    BMI = weight / (height / 100) ** 2

    top_status = [(14.9, 'Severely underweight'), (18.4, 'Underweight'),
                  (22.9, 'Normal'), (27.5, 'Overweight'),
                  (40.0, 'Moderately obese'), (float('inf'), 'Severely obese')]

    for top, status in top_status:
        if BMI <= top:
            put_text('Your BMI: %.1f, category: %s' % (BMI, status))
            break



if __name__ == '__main__':
    bmi()
