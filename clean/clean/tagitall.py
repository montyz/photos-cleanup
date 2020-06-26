import csv
import os.path
from collections import defaultdict

import osxphotos


def main():
    db = os.path.expanduser("/Users/monty/Pictures/Master Photos Library.photoslibrary")
    photosdb = osxphotos.PhotosDB(db)
    with open("alltags.csv", "w") as tagfile:
        alltagscsv = csv.DictWriter(tagfile, ["uuid", "tags"])
        alltagscsv.writeheader()

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
                    tags.append(folder)
                tags.append(album.title)

            rowdict = {"uuid": p.uuid, "tags": ",".join(tags)}
            alltagscsv.writerow(rowdict)
            print(rowdict)

# todo get date ranges for the cameras
if __name__ == "__main__":
    main()
