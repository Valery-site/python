import struct
import plotly.graph_objects as go
import numpy as np
from tkinter import filedialog

filepath = filedialog.askopenfilename() #чтение = открытие диалового окна, путь к файлу

f = open(filepath,'r', encoding="ansi")
str = f.readline().split('|')
xlen = int(str[0]) #размер карты по ширине (371)
ylen = int(str[1]) #размер карты по длине (784)
stepx = float(str[2].replace(',','.')) #масштаб карты по ширине (3,5498046875)
stepy = float(str[3]) #масштаб карты по длине (8)
startx = int(str[4]) #начало данных на карте по ширине (0)
starty = int(str[5]) #начало данных на карте по длине (0)
lastx = int(str[6]) #конец данных на карте по ширине (370)
lasty = int(str[7]) #конец данных на карте по длине (783)
width = int(str[8]) #количество точек по ширине (371)
height = int(str[9]) #количество точек по длине (784)
level = float(str[10].replace(',','.')) #базовый уровень (20,7608547210693)
header = int(f.readline())
f.close()

def CreatePlot(filepath):
    Values = []

    with open(filepath, 'rb') as f:
        f.read(header)
        while True:
            Value = f.read(4)
            if not Value:
                break
            Values.append(float(struct.unpack('<f', bytes(Value))[0]) + level)

    i = 0
    Matrix = [[0.0 for x in range(lastx - startx+1)] for y in range(lasty - starty+1)]
    for y in range(height):
        for x in range(width):
            if startx <= x <= lastx and starty <= y <= lasty:
                Matrix[y - starty][x - startx] = Values[i]
            i+=1
    
    fig = go.Figure(go.Surface(x = np.arange(startx, lastx),
    y = np.arange(starty, lasty),
    z = Matrix, colorscale = 'turbo'))

    fig.update_layout(scene = {"aspectratio": {"x": stepx, "y": stepy, "z": 0.01}})
    fig.show()

CreatePlot(filepath)