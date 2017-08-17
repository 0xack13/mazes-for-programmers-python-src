from base.grid import Grid
from algorithms.sidewinder import Sidewinder
import renderers.ascii_renderer as ASCIIRenderer
import renderers.unicode_renderer as UNICODERenderer
import renderers.png_renderer as PNGRenderer


if __name__ == "__main__":
    grid = Grid(6, 6)
    grid = Sidewinder.on(grid)
    ASCIIRenderer.render(grid)
    UNICODERenderer.render(grid)
    PNGRenderer.render(grid)
