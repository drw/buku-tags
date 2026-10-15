"""Get the tags from the local buku database of bookmarks and output
them in a list sorted by increasing tag use frequency."""

import buku

import os
from pprint import pprint


def format_brick(tag: str, count: int) -> str:
    return f'{tag} ({count})  '

def print_tag_wall(sorted_tags: list[tuple]):
    """Print a more compact form of the tag list."""
    col = 0
    for tag, count in sorted_tags:
        brick = format_brick(tag, count)
        if len(brick) + col > max_column:
            print("\n", end="")
            col = 0
        print(brick, end="")
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
