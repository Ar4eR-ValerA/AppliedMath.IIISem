import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def visualize_fw(): #функция для визуализации, думаю не стоит сюда лезть, позже вслух поясню
    xcoord = np.linspace(-10.0, 10.0, 50)
    ycoord = np.linspace(-10.0, 10.0, 50)
    w1, w2 = np.meshgrid(xcoord, ycoord)
    pts = np.vstack((w1.flatten(), w2.flatten()))
    pts = pts.transpose()

    print(pts * pts)
    f_vals = np.sum(pts * pts, axis=1)
    # function_plot(pts, f_vals)
    plt.title('Objective Function Shown in Color')
    plt.show()
    return pts, f_vals


def annotate_pt(text, xy, xytext, color):
    plt.plot(xy[0], xy[1], marker='P', markersize=10, c=color)
    plt.annotate(text, xy=xy, xytext=xytext,
                 # color=color,
                 arrowprops=dict(arrowstyle="->",
                                 color=color,
                                 connectionstyle='arc3'))

def function_plot(pts, f_val):
    f_plot = plt.scatter(pts[:, 0], pts[:, 1],
                         c=f_val, vmin=min(f_val), vmax=max(f_val),
                         cmap='RdBu_r')
    plt.colorbar(f_plot)

pts, f_vals = visualize_fw()
