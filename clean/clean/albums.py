import csv
import os.path
from collections import defaultdict

import osxphotos


def main():
    db = os.path.expanduser("/Users/monty/Pictures/Master Photos Library.photoslibrary")
    photosdb = osxphotos.PhotosDB(db)
    with open("albums.csv", "w") as tagfile:
        alltagscsv = csv.DictWriter(tagfile, ["name", "tag", "count"])
        alltagscsv.writeheader()
        tagcount = defaultdict(int)
        for album in photosdb.album_info:
            title = album.title
            tagcount[title] = tagcount[title] + len(album.photos)
            for folder in album.folder_names:
                tagcount[folder] = tagcount[folder] + len(album.photos)
        keys = sorted(tagcount.keys())

        for key in keys:
            rowdict = {"name": key, "tag": key, "count": tagcount[key]}
            alltagscsv.writerow(rowdict)
            print(rowdict)

# todo get date ranges for the cameras
if __name__ == "__main__":
    main()
