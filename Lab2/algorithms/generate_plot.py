import numpy as np
import matplotlib.pyplot as plt


# функция для визуализации, думаю не стоит сюда лезть, позже вслух поясню
def visualize_fw():
    x_coord = np.linspace(-10.0, 10.0, 50)
    y_coord = np.linspace(-10.0, 10.0, 50)
    w1, w2 = np.meshgrid(x_coord, y_coord)
    pts = np.vstack((w1.flatten(), w2.flatten()))
    pts = pts.transpose()

    f_vals = np.sum(pts * pts, axis=1)
    # function_plot(pts, f_vals)
    plt.title('Objective Function Shown in Color')
    plt.show()
    return pts, f_vals


def annotate_pt(text, xy, xy_text, color):
    plt.plot(xy[0], xy[1], marker='P', markersize=10, c=color)
    plt.annotate(text, xy=xy, xytext=xy_text,
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
