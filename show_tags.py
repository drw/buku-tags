"""Get the tags from the local buku database of bookmarks and output
them in a list sorted by increasing tag use frequency."""

import buku

from pprint import pprint


db = buku.BukuDb()
_, count_by_tag = db.get_tag_all()
sorted_tags = sorted(count_by_tag.items(), key = lambda x: x[1])
pprint(sorted_tags)

# Check tags for spaces. (Tags should be comma-delimited.)
spacey_tags = []
for tag, count in sorted_tags:
    if ' ' in tag:
        spacey_tags.append(tag)
if len(spacey_tags) > 0:
    print(f"\nThere shouldn't be a space in any tag. Please fix these: {spacey_tags}")
