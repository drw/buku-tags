"""Get the tags from the local buku database of bookmarks and output
them in a list sorted by increasing tag use frequency."""

import buku

from pprint import pprint


db = buku.BukuDb()
_, count_by_tag = db.get_tag_all()
sorted_tags = sorted(count_by_tag.items(), key = lambda x: x[1])
pprint(sorted_tags)
