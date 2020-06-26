import collections
import csv


class TagMap(collections.abc.Mapping):
    def __init__(self, fn):
        self.tagmap = {}
        with open(fn) as albumfile:
            tagmapcsv = csv.DictReader(albumfile)
            for d in tagmapcsv:
                self.tagmap[d['name']] = d['tag']

    def __iter__(self):
        return self.tagmap.__iter__()

    def __len__(self) -> int:
        return self.tagmap.__len__()

    def __getitem__(self, k):
        if k in self.tagmap:
            return self.tagmap[k]
        else:
            return 'UNKNOWN TAG: ' + k
