# These lines import the Numpy and Datascience modules.
import numpy as np
from datascience import *

# These lines do some fancy plotting magic.
import matplotlib
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import warnings
warnings.simplefilter('ignore', FutureWarning)
import matplotlib.patches as patches

def pivot_table_to_groups(pivoted, x_label):
    """
    Convert a contingency table that's been computed by pivot() to a
    table with the same information as it computed by groups() on the
    two pivot columns.  This kind of table is easier for a computer to
    work with, but harder for a human to read than a pivot table.
    """
    y_label = pivoted.labels[0]
    x_categories = np.array(pivoted.labels).take(range(1, pivoted.num_columns))
    y_categories = pivoted.column(0)

    grouped = Table([x_label, "x index", y_label, "y index"]).with_rows([(x, x_idx, y, y_idx) for (x_idx, x) in enumerate(x_categories) for (y_idx, y) in enumerate(y_categories)])

    def get_combination_count(x_idx, y_idx):
        return pivoted.column(x_categories.item(x_idx)).item(y_idx)
    grouped.append_column("count", grouped.apply(get_combination_count, ["x index", "y index"]))

    return grouped.select([x_label, y_label, "count"])

def normalize(array, intended_sum):
    return intended_sum * array / sum(array)

COLORS = [
    0x000072, #yale blue
    0xfea610, #california gold
    0xdc1134, #stanfurd red
    0x81a63d, #green
    0x000000, #black
    0xa0f6aa, #light green
    0x513985, #purple
    0x00ffff, #light blue
    0x72322e, #brown
]

def get_colors(num_colors):
    return COLORS[0:min(num_colors, len(COLORS))] \
         + list(np.random.randint(0xFFFFFF, size=max(0, num_colors-len(COLORS))))

def compute_combination_data(combinations, individuals_name):
    """
    Given a table of grouped counts, produces a table of information that
    will be used in plotting:
      * The percentage of things in each group
      * A message describing the group
      * The color to use when displaying the group
    """
    assert(combinations.labels[-1] == "count")
    x_label = combinations.labels[0]
    y_label = combinations.labels[1]
    combinations = combinations.where(combinations.column("count") > 0)
    combinations = combinations.sort("count", descending=True)

    def make_compute_message(total_count):
        def compute_message(row):
            labels = row[:-1]
            count = row[-1]
            descriptions = ["%s %s" % (l, category) for (l, category) in zip(labels, combinations.labels[:-1])]
            if len(descriptions) == 1:
              description = descriptions[0]
            elif len(descriptions) == 2:
              description = " and ".join(descriptions)
            else:
              descriptions[-1] = "and " + descriptions[-1]
              description = ", ".join(descriptions)
            return ("%.8g out of %.8g %s have %s" % (count, total_count, individuals_name, description))
        return compute_message

    combinations.append_column("message", combinations.apply(make_compute_message(sum(combinations.column("count")))))
    combinations.append_column("percentage", normalize(combinations.column("count"), 100))
    combinations.append_column("color", ["#%0.6X" % c for c in get_colors(combinations.num_rows)])
    return combinations

def make_displayed_rectangles(combinations):
    """
    Given a table like that produced by compute_combination_data, produces
    a new version of the table that includes the Rectangle objects to draw
    when displaying each category in an icon array.  The objects are drawn
    in a 10x10 grid.  Sometimes the whole grid isn't drawn.
    """
    n = combinations.num_rows
    displays = combinations.copy()
    total_count = sum(displays.column("count"))
    if 1 < total_count < 100:
      # Use counts instead of percentages to make a clearer visualization.
      amount_column = "count"
    else:
      amount_column = "percentage"

    displays.append_column("start amount", np.cumsum(np.append([0], displays.column(amount_column)))[0:n])
    displays.append_column("end amount", np.cumsum(displays.column(amount_column)))

    SQUARE_SIZE = .1
    SQUARE_PADDING = .01
    DRAWN_SQUARE_SIZE = SQUARE_SIZE - 2*SQUARE_PADDING

    def square_logical_coordinates(start_percentile, end_percentile):
        percentile = int(np.floor(start_percentile))
        return (percentile % 10, percentile // 10)

    def square_bottom_left(logical_x, logical_y):
        return (logical_x / 10, logical_y / 10)

    # Coordinates of the bottom-left of a rectangle inside its square.
    # (0, 0) is the bottom-left of the square, and the square has a side
    # length of 1.
    def bottom_left_in_square(start_percentile, end_percentile):
        percentile = int(np.floor(start_percentile))
        left_end = start_percentile - percentile
        return (left_end, 0)

    def rectangle_for_percentile(start_percentile, end_percentile, color):
        (logical_x, logical_y) = square_logical_coordinates(start_percentile, end_percentile)
        (square_x, square_y) = square_bottom_left(logical_x, logical_y)
        (x_in_square, y_in_square) = bottom_left_in_square(start_percentile, end_percentile)
        absolute_x = square_x + SQUARE_PADDING + DRAWN_SQUARE_SIZE*x_in_square
        absolute_y = square_y + SQUARE_PADDING + DRAWN_SQUARE_SIZE*y_in_square
        rectangle_proportion = end_percentile - start_percentile
        return patches.Rectangle((absolute_x, absolute_y), rectangle_proportion*DRAWN_SQUARE_SIZE, DRAWN_SQUARE_SIZE, facecolor=color)

    def rectangles_for_percentage_range(start, end, color):
        rectangles = []
        for percentile in range(int(np.floor(start)), int(np.ceil(end))):
            start_percentile = max(start, percentile)
            end_percentile = min(end, percentile+1)
            rectangles.append(rectangle_for_percentile(start_percentile, end_percentile, color))
        return rectangles

    displays.append_column("rectangles", displays.apply(rectangles_for_percentage_range, ["start amount", "end amount", "color"]))

    return displays

def draw_plot(displays, individuals_name):
    """
    Given a table of categories and the rectangles to display for each category,
    draw an icon array made from those rectangles.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect="equal")
    all_rectangles = [r for rectangles in displays.column("rectangles") for r in rectangles]
    for r in all_rectangles:
        ax.add_patch(r)

    # Make the axes more useful:
    total_count = sum(displays.column("count"))
    if 1 < total_count < 100:
        count_per_box = 1
    else:
        count_per_box = total_count/100
    x_side_count = 10*count_per_box
    y_side_count = 100*count_per_box
    xticks = matplotlib.ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x*x_side_count))
    ax.xaxis.set_major_formatter(xticks)
    yticks = matplotlib.ticker.FuncFormatter(lambda y, pos: '{0:g}'.format(y*y_side_count))
    ax.yaxis.set_major_formatter(yticks)

    # Draw a legend:
    def make_dummy_rectangle(color, message):
        return patches.Patch(color=color, label=message)
    dummy_rectangles = displays.apply(make_dummy_rectangle, ["color", "message"])
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), handles=list(dummy_rectangles))
    plt.text(1.1, 0.1, "Each box represents %g %s." % (count_per_box, individuals_name), fontsize=20)

def display_combinations(category_counts, individuals_name="people"):
    displays = make_displayed_rectangles(compute_combination_data(category_counts, individuals_name))
    draw_plot(displays, individuals_name)


def test():
  cancer = Table().with_columns(["cancer status", ["cancer", "no cancer"], "positive", [90, 198], "negative", [10, 9702]]) #SOLUTION
  grouped = pivot_table_to_groups(cancer, "test status")
  display_combinations(grouped)

  trinkets = Table(["x", "y"]).with_rows([
          ["a", "i"],
          ["a", "j"],
          ["b", "k"]
      ])
  display_combinations(trinkets.groups(['x']))
  display_combinations(trinkets.groups(['x', 'y']))

if __name__ == "__main__":
  test()
