import numpy as np
import matplotlib.pyplot as plt

def draw_hb():
    x1 = [65.5,80.35,90.25,105.1]
    y1 = [1,1,1,0]
    x2 = [77.7,96.15,108.54,126.9]
    y2 = [0,1,1,1]
    my_title = "Hb Diffetential Diagnosis"
    my_axis = [60.0,130.0,0.0,1.2]

    return x1, y1, x2, y2, my_title, my_axis

def draw_rbc_mvc():
    x1 = [1.1, 2.9, 4.1, 5.9]
    y1 = [1, 1, 1, 0]
    x2 = [4.5, 6.9, 8.5, 10.9]
    y2 = [0, 1, 1, 1]
    my_title = "RBC/MCV Diffetential Diagnosis"
    my_axis = [1.0,11.0,0.0,1.2]

    return x1, y1, x2, y2, my_title, my_axis

def draw_rdw():
    x1 = [19.5, 21.45, 22.75, 24.7]
    y1 = [0, 1, 1, 1]
    x2 = [12.1, 16, 18.6, 22.5]
    y2 = [1, 1, 1, 0]
    my_title = "RDW Diffetential Diagnosis"
    my_axis = [12.0,25.0,0.0,1.2]

    return x1, y1, x2, y2, my_title, my_axis

if __name__ == '__main__':

    x1, y1, x2, y2, my_title, my_axis = draw_hb()
    plt.figure()
    plt.plot(x1,y1,"g-",label="Iron deficiency anemia")
    plt.plot(x2,y2,"r-.",label="Thalassemia",linewidth=2)

    plt.axis(my_axis)
    plt.xlabel("")
    plt.ylabel("Possibility")
    plt.title(my_title)

    plt.grid(True)
    plt.legend()
    plt.show()
