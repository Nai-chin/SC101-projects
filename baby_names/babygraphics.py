"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

This program draw the trend of baby name ranking in specific
range of years. The graphic including 2 parts:
1. fixed graphic: lines, axis to present the trend.
2. trend of baby names: draw the trend of names which user searched.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    yrs = len(YEARS)
    width_m = width - 2 * GRAPH_MARGIN_SIZE
    x_coordinate = GRAPH_MARGIN_SIZE + width_m / yrs * year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # Draw line on top
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    # Draw line at bottom
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, )

    # Draw vertical lines & add year scale
    for yr_index in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, yr_index)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[yr_index], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)                                        # draw the fixed background grid

    # Write your code below this line
    #################################
    rank_scale = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / 1000     # scale of the rank, only show rank within 1,000
    for i in range(len(lookup_names)):
        name = lookup_names[i]
        n_yr_rank = name_data[name]                                 # dict, rank at each year

        # 1st year, only need to find y on the line and add the text
        yr_0 = str(YEARS[0])
        if yr_0 in n_yr_rank:
            rank_yr0 = n_yr_rank[yr_0]
            dot1_x = get_x_coordinate(CANVAS_WIDTH, 0)
            dot1_y = GRAPH_MARGIN_SIZE + (int(rank_yr0) - 1) * rank_scale
            canvas.create_text(dot1_x + TEXT_DX, dot1_y, text=(name + ' ' + rank_yr0),
                               anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])
        else:
            # Rank out of 1,000
            dot1_x = get_x_coordinate(CANVAS_WIDTH, 0)
            dot1_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            canvas.create_text(dot1_x + TEXT_DX, dot1_y, text=name + ' *',
                               anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])

        # Draw lines of other years
        for j in range(1, len(YEARS)):
            yr = str(YEARS[j])
            dot2_x = get_x_coordinate(CANVAS_WIDTH, j)
            if yr in n_yr_rank:
                rank = n_yr_rank[yr]
                dot2_y = GRAPH_MARGIN_SIZE + (int(rank) - 1) * rank_scale
                canvas.create_text(dot2_x + TEXT_DX, dot2_y, text=(name + ' ' + rank),
                                   anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])
            else:
                # Rank out of 1,000
                dot2_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                canvas.create_text(dot2_x + TEXT_DX, dot2_y, text=name + ' *',
                                   anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])
            canvas.create_line(dot1_x, dot1_y, dot2_x, dot2_y, width=LINE_WIDTH, fill=COLORS[i % len(COLORS)])
            # Update x, y of dot1 for next line
            dot1_x = dot2_x
            dot1_y = dot2_y


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
