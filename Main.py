import tkinter as tk
from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubble_sort
from quicksort import quick_sort
from mergesort import merge_sort

window = tk.Tk() #gives a name so we can just functions like title and geometry

data = []

window.title('Algorithm Visualiser') #title for the gui
window.geometry("900x600+200+80") #size of the gui
window.config(bg='#a09dca')

def drawData(data, colorArray):
    canvas.delete("all")
    canvas_height = 450
    canvas_width = 870
    x_width = canvas_width / (len(data) + 1)
    offset = 10
    spacing_bet_rect = 10
    normalised_data = [i/max(data) for i in data]

    for i , height in enumerate(normalised_data):
        x0 = i*x_width + offset + spacing_bet_rect
        y0 = canvas_height - height * 400
        x1 = (i+1) * x_width
        y1 = canvas_height

        canvas.create_rectangle(x0,y0,x1,y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text = str(data[i]), font = ("new roman", 15, "italic bold"),
                           fill = "orange")

    window.update_idletasks()

def startAlgorithm():
    print("starting Algorithm")
    global data
    if not data:
        return
    
    if(algo_menu.get() == 'Quick Sort'):
        quick_sort(data, 0, len(data)-1, drawData, speedScale.get())
    
    elif(algo_menu.get() == 'Bubble sort'):
        bubble_sort(data, drawData, speedScale.get())

    elif algo_menu.get() == "Merge Sort":
        merge_sort(data, drawData, speedScale.get())
    drawData(data, ['green' for x in range(len(data))])


def Generate():
    global data
    print("Selected Algorithm: " + selected_algorithm.get())
    minivalue = int(minvalue.get())
    maxivalue = int(maxvalue.get())
    sizeevalue = int(sizevalue.get())

    data = []
    for _ in range(sizeevalue):
        data.append(random.randrange(minivalue, maxivalue+1))
    drawData(data, ['red' for x in range(len(data))])


    drawData(data)

# Variables
selected_algorithm = StringVar()

# labels
mainlabel = Label(window, text = "Algorithm: ", font = ("new roman", 16, "italic bold"), bg = "#7f5a7a",
                  width = 10, fg = "black", relief = GROOVE, bd = 5)
mainlabel.place(x=0,y=0)

algo_menu = ttk.Combobox(window, state="readonly", width=15, font = ("new roman", 16, "italic bold"), textvariable= selected_algorithm,
                         values=['Bubble sort', 'Merge Sort', 'Quick Sort'])
algo_menu.place(x=145, y=0)
algo_menu.current(0)

random_generate = Button(window, text="Generate", bg= "#7f5a7a", font = ("arial", 12, "italic bold"), relief=SUNKEN,
                         activebackground="#05945b", activeforeground="white", bd = 5, width = 10, command=Generate)
random_generate.place(x=750, y=60)

#
sizevaluelabel = Label(window, text="Size: ", font=("new roman", 12, "italic bold"), bg = "#7f5a7a",
                       width= 10, fg="Black", height=2, relief=GROOVE, bd=5)
sizevaluelabel.place(x=0,y=60)

sizevalue = Scale(window, from_= 1, to = 30, resolution=1, orient=HORIZONTAL, font= ("Arial", 14),
                  relief= GROOVE, bd = 2, width=10)
sizevalue.place(x=120,y=60)

#
minvaluelabel = Label(window, text="Min value: ", font=("new roman", 12, "italic bold"), bg = "#7f5a7a",
                       width= 10, fg="Black", height=2, relief=GROOVE, bd=5)
minvaluelabel.place(x=250,y=60)

minvalue = Scale(window, from_= 0, to = 10, resolution=1, orient=HORIZONTAL, font= ("Arial", 14),
                  relief= GROOVE, bd = 2, width=10)
minvalue.place(x=370,y=60)

#
maxvaluelabel = Label(window, text="Max Value: ", font=("new roman", 12, "italic bold"), bg = "#7f5a7a",
                       width= 10, fg="Black", height=2, relief=GROOVE, bd=5)
maxvaluelabel.place(x=500,y=60)

maxvalue = Scale(window, from_= 1, to = 100, resolution=1, orient=HORIZONTAL, font= ("Arial", 14),
                  relief= GROOVE, bd = 2, width=10)
maxvalue.place(x=620,y=60)


#
start = Button(window, text="Start", bg= "#c45b09", font = ("arial", 12, "italic bold"), relief=SUNKEN,
                activebackground="#05945b", activeforeground="white", bd = 5, width = 10, command= startAlgorithm)
start.place(x=750, y=0)

speedLabel = Label(window, text="Speed: ", font=("new roman", 12, "italic bold"), bg = "#7f5a7a",
                       width= 10, fg="Black", relief=GROOVE, bd=5)
speedLabel.place(x=400, y=0)

speedScale = Scale(window, from_= 0.1, to = 5.0, resolution= 0.2,length=200, digits=2, orient=HORIZONTAL, font= ("Arial", 14),
                  relief= GROOVE, bd = 2, width=10)
speedScale.place(x=520, y=0)

canvas = Canvas(window, width = 870, height=450, bg = "black")
canvas.place(x=10, y=130)

window.mainloop()
