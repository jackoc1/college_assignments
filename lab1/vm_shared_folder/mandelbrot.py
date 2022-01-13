from matplotlib import pyplot as plt
from time import time

MAX_ITERATIONS = [50, 200, 400, 600, 800, 1000, 1200]
IMAGE_WIDTHS = [50, 200, 400, 600, 800, 1000, 1200]

def scaled_x(x, origin):
    return 1.15 * (x - origin[0]) / (origin[0]) - 0.45


def scaled_y(y, origin):
    return 1.15 * (y - origin[1]) / (origin[1])


def iter_to_color(iter, max_iter):
    return int((iter / max_iter) * 255)


def mandelbrot(im_width, max_iter):
    t_0 = time()
    origin = [im_width // 2] * 2
    image = [[0] * im_width for i in range(im_width)]

    for p_y in range(len(image)):
        for p_x in range(len(image[p_y])):
            x_0 = scaled_x(p_x, origin)
            y_0 = scaled_y(p_y, origin)

            x = 0.0
            y = 0.0

            iter = 0
            while x**2 + y**2 <= 4 and iter < max_iter:
                xtemp = x**2 - y**2 + x_0
                y = 2*x*y + y_0
                x = xtemp
                iter += 1

            color = iter_to_color(iter, max_iter)
            image[p_y][p_x] = (0, 0, color)

    t_1 = time()
    return image, t_1 - t_0


# Plotting

fig, axs = plt.subplots(len(MAX_ITERATIONS), len(IMAGE_WIDTHS))

for i, im_width in enumerate(IMAGE_WIDTHS):
    for j, max_iter in enumerate(MAX_ITERATIONS):
        fig, ax = plt.subplots(1, 1)
        plot = mandelbrot(im_width, max_iter)

        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_xticks([])
        ax.set_yticks([])

        ax.set_title(f"Iteration depth: {max_iter}, Image width: {im_width} pixels")
        ax.set_xlabel(f"Time taken: {plot[1]:.5f} seconds")
        ax.imshow(plot[0])

        plt.savefig(f"iter:{max_iter}-width:{im_width}-time:{plot[1]:.5f}.png")
        plt.close(fig)
        # print(f"iter:{max_iter}-width:{im_width}-time:{plot[1]:.5f}.png")
