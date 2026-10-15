"""Get the tags from the local buku database of bookmarks and output
them in a list sorted by increasing tag use frequency."""

import buku

import os
from pprint import pprint

from rich.console import Console
console = Console()


def format_brick(tag: str, count: int) -> str:
    return f'{tag} ({count})  '


def convert_to_color_code(ratio: float) -> int:
    number = int(ratio * 256 - 1)
    if number < 0:
        return 0
    return number


def brick_color(i: int, count: int, count_min: int, count_max: int) -> str:
    import colorsys

    hue_speed = 1/12
    hue = hue_speed * i % 1
    s = 1 + 0.7*((count - count_min)/(count_max - count_min) - 1)
    r, g, b = colorsys.hls_to_rgb(hue, 0.5, s)
    [R, G, B] = [convert_to_color_code(c) for c in [r, g, b]]
    return f'rgb({R},{G},{B})'


def print_tag_wall(sorted_tags: list[tuple]):
    """Print a more compact form of the tag list."""
    col = 0
    count_min = sorted_tags[0][1]
    count_max = sorted_tags[-1][1]
    for i, (tag, count) in enumerate(sorted_tags):
        brick = format_brick(tag, count)
        if len(brick) + col > max_column:
            print("\n", end="")
            col = 0
        b_style = brick_color(i, count, count_min, count_max)
        console.print(brick, end="", style=b_style)
        col += len(brick)
    print("\n")


db = buku.BukuDb()
_, count_by_tag = db.get_tag_all()
sorted_tags = sorted(count_by_tag.items(), key = lambda x: x[1])
pprint(sorted_tags) # Print list of tags sorted by increasing count.
max_column = os.get_terminal_size().columns
print("=" * max_column)
print_tag_wall(sorted_tags)

# Check tags for spaces. (Tags should be comma-delimited.)
spacey_tags = []
for tag, count in sorted_tags:
    if ' ' in tag:
        spacey_tags.append(tag)
if len(spacey_tags) > 0:
    print(f"\nThere shouldn't be a space in any tag. Please fix these: {spacey_tags}")
