from time import gmtime, strftime
from PIL import Image, ImageDraw
from typing import Any

from base.colored_grid import ColoredGrid

STEP_BACKGROUND = 0


def render(grid: ColoredGrid, **kwargs: Any) -> None:
    filename = strftime("%Y%m%d%H%M%S", gmtime())
    cell_size = 10
    coloring = False

    for key in kwargs:
        if key == "filename":
            filename = kwargs[key]
        elif key == "cell_size":
            cell_size = kwargs[key]
        elif key == "coloring":
            coloring = kwargs[key]

    image_width = cell_size * grid.columns
    image_height = cell_size * grid.rows

    wall_color = (0, 0, 0)

    image = Image.new("RGBA", (image_width + 1, image_height + 1), (255, 255, 255))

    draw = ImageDraw.Draw(image)

    for draw_pass in range(2):
        for cell in grid.each_cell():
            x1 = cell.column * cell_size
            y1 = cell.row * cell_size
            x2 = (cell.column + 1) * cell_size
            y2 = (cell.row + 1) * cell_size

            if draw_pass == STEP_BACKGROUND and coloring:
                color = grid.background_color_for(cell)
                draw.rectangle((x1, y1, x2, y2), fill=color)
            else:
                if not cell.north:
                    draw.line((x1, y1, x2, y1), fill=wall_color, width=1)
                if not cell.west:
                    draw.line((x1, y1, x1, y2), fill=wall_color, width=1)
                if not cell.linked_to(cell.east):
                    draw.line((x2, y1, x2, y2), fill=wall_color, width=1)
                if not cell.linked_to(cell.south):
                    draw.line((x1, y2, x2, y2), fill=wall_color, width=1)

    image.save("{}.png".format(filename), "PNG", optimize=True)

# -----
# Unused at least for now: Pixel-based drawing:
# pixels = img.load()
# for x in range(img.size[0]):
#     for y in range(img.size[1]):
#         pixels[x, y] = (x, y, 100)
