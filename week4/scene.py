# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.

    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_cloud(canvas, scene_width, scene_height)
    draw_fence(canvas, scene_width, scene_height)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.


def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0, scene_width, scene_height, fill = "skyblue")

def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0, scene_width, 100, fill = "green", outline="green")

def draw_cloud(canvas, scene_width, scene_height):
    draw_oval(canvas, 100, 400, 200, 350, fill = "white", outline="white")
    draw_oval(canvas, 120, 430, 200, 350, fill = "white", outline="white")

def draw_fence(canvas, scene_width, scene_height):
    x_start = 0
    y_start = 0
    fence_width = 30
    fence_color = "brown"
    for _ in range(20):
        draw_rectangle(canvas, x_start, y_start, x_start + fence_width, 200, fill = fence_color, outline = fence_color)
        x_start += fence_width * 2

# Call the main function so that
# this program will start executing.
main()