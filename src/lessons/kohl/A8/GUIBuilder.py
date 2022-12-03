import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import inspect
import matplotlib
matplotlib.use('TkAgg')

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def delete_figure_agg(figure_agg):
    figure_agg.get_tk_widget().forget()
    plt.close('all')


def build_window(county_list=[], options_list=[], theme='TealMono'):
    # Pass the name of the theme into the theme() method
    sg.theme(theme)

    # This code bit creates the drop down layout for the counties
    counties = [[sg.Text('Pick the counties you would like to compare:')],
                [sg.Listbox(values=county_list, change_submits=True, size=(28, len(options_list)), key='-COUNTY1-'),
                 sg.Listbox(values=county_list, change_submits=True, size=(28, len(options_list)), key='-COUNTY2-')]]

    # This code bit creates the drop down layout for the attributes of the data
    col_listbox = [[sg.Text('Pick the attributes you would like to compare by:')],
                    [sg.Listbox(values=options_list, change_submits=True, size=(28, len(options_list)), key='-ATTRIBUTES1-'),
                    sg.Listbox(values=options_list, change_submits=True, size=(28, len(options_list)), key='-ATTRIBUTES2-')],
                   [sg.Text(' ' * 12), sg.Button('Exit'), sg.Button('Plot')]]

    # This code bit sets up the canvas for the bar chart
    col_canvas = sg.Col([[sg.Canvas(size=(500, 500), key='-CANVAS-')]])

    # This code bit sets up a window pane for the canvas and adds data source text for the bar chart
    col_chart_data = sg.Col([[sg.Pane([col_canvas], size=(500,500))],
                               [sg.Text('Chart data from open.data.gov')]])

    # This is where we put all the code come together in a layout
    layout = [[sg.Text('COVID, Hospitals + Housing Prices in Utah Counties', font=('ANY 18'))],
              [sg.Col(counties)],
              [sg.Col(col_listbox), col_chart_data]]

    # This code creates the window object
    window = sg.Window('COVID, Hospitals + Housing Prices in Utah Counties',
                       layout, resizable=True, finalize=True)


    return window