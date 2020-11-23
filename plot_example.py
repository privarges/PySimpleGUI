import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib
import os

# GREO Logo File path
GREOlogofile = os.path.join(
            './images/greologo.png'
        )

fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

matplotlib.use("TkAgg")

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg


######    Define the window layout    ###############
# Left Column
inputs_column = [
    [sg.Image(key="GREOLogo")], # PNG or GIF image
    [sg.Text("Inputs")], 
    [sg.Input('', enable_events=True,  key='-INPUT-')], # Text input field
]

# Right Column
image_viewer_column = [
    [sg.Text("Result")], # Simple Text
    [sg.Text(size=(40, 1), key="-TextResult-")], # Simple Text
    [sg.Canvas(key="-CANVAS-")], # Result Plot space 
    [sg.Button("Ok")], # Button
]

# Full Window layout
layout = [
        [   sg.Column(inputs_column),
            sg.VSeperator(),
            sg.Column(image_viewer_column),
        ]
]

#######################################################

# Create the form and show it without the plot
window = sg.Window(
    "Matplotlib Single Graph",
    layout,
    location=(0, 0),
    finalize=True,
    element_justification="center",
    font="Helvetica 18",
)
sg.theme('TanBlue')

# Add the plot to the window
draw_figure(window["-CANVAS-"].TKCanvas, fig)
window["GREOLogo"].update(filename=GREOlogofile,size=(200,200))

event, values = window.read()

window.close()
