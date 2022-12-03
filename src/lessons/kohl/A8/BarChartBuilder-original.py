# This function draws the barchart in the GUI
# The function takes in five parameters: county1, county2, choice1, choice2, and dictionary
# These parameters represent the choices passed from the GUI

def barchart(county1='', county2='', choice1='', choice2='', dict={}):
    import matplotlib.pyplot as plt
    import numpy as np

    # This is where we define what data to plot
    display_value1 = []
    display_value2 = []
    display_value1.append(dict[county1[0]][choice1[0]])
    display_value1.append(dict[county2[0]][choice1[0]])
    display_value2.append(dict[county1[0]][choice2[0]])
    display_value2.append(dict[county2[0]][choice2[0]])

    # Here we assign the width of the bars
    bar_width = 0.35

    # Here we set the position of bars on the X axis
    pos_1 = np.arange(len(display_value1))
    pos_2 = pos_1 + bar_width

    # This is where we draw the bars
    plt.bar(pos_1, display_value1, color='#d8b365', width=bar_width, edgecolor='white', label=choice1)
    plt.bar(pos_2, display_value2, color='#5ab4ac', width=bar_width, edgecolor='white', label=choice2)

    # This creates a label for the x axis
    plt.xlabel('County')

    # To wrap up the bar chart, we create labels
    plt.xticks(pos_1 + bar_width / 2, [county1] + [county2])
    plt.title(''.join(choice1[0]) + " x " + ''.join(choice2[0]) + ' by County')

    plt.legend()

    plt.tight_layout()

    # We convert the plot into the proper format for the GUI
    fig = plt.gcf()

    return fig