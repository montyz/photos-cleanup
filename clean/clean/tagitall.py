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
        alltagscsv = csv.DictWriter(tagfile, ["uuid", "tags", "fn", "taken"])
        alltagscsv.writeheader()
        tagmap = TagMap("albums.csv")

        for p in photosdb.photos():
            if p.ismissing:
                continue
            tags = set()

            model = p.exif_info.camera_model
            if model:
                camera = "camera:" + str(model)
            else:
                camera = "camera:Missing"
            tags.add(camera)
            for album in p.album_info:
                for folder in album.folder_names:
                    tags.add(tagmap[folder])
                tags.add(tagmap[album.title])

            rowdict = {"uuid": p.uuid,
                       "tags": ",".join([i for i in tags if i is not None]),
                       "fn": p.path,
                       "taken": p.date.strftime("%Y-%m-%d-%H:%M:%S.%f")}
            alltagscsv.writerow(rowdict)
            print(rowdict)


# todo get date ranges for the cameras
if __name__ == "__main__":
    main()
