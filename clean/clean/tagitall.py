import csv
import os.path
from collections import defaultdict

import osxphotos

from clean.tagmap import TagMap


def main():
    # db = os.path.expanduser("/Users/monty/Pictures/Master Photos Library.photoslibrary")
    db = os.path.expanduser("/Users/monty/Pictures/2020 Pictures/Mexico 2019.photoslibrary")
    photosdb = osxphotos.PhotosDB(db)
    with open("alltags.csv", "w") as tagfile:
        alltagscsv = csv.DictWriter(tagfile, ["uuid", "tags", "fn"])
        alltagscsv.writeheader()
        tagmap = TagMap("albums.csv")

        for p in photosdb.photos():
            tags = []

            model = p.exif_info.camera_model
            if model:
                camera = str(model)
            else:
                camera = "Camera Missing"
            tags.append(camera)
            for album in p.album_info:
                for folder in album.folder_names:
                    tags.append(tagmap[folder])
                tags.append(tagmap[album.title])

            rowdict = {"uuid": p.uuid, "tags": ",".join(tags), "fn": p.filename}
            alltagscsv.writerow(rowdict)
            print(rowdict)


# todo get date ranges for the cameras
if __name__ == "__main__":
    main()
