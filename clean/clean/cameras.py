import os.path
from collections import defaultdict

import osxphotos


def main():
    db = os.path.expanduser("/Users/monty/Pictures/Master Photos Library.photoslibrary")
    photosdb = osxphotos.PhotosDB(db)

    cameras = defaultdict(int)
    for p in photosdb.photos():
        #makemodel = "{}:{}".format(p.exif_info.camera_make,p.exif_info.camera_model)
        makemodel = str(p.exif_info.camera_model)
        cameras[makemodel]=cameras[makemodel]+1
    sorted_cameras = list(cameras.keys())
    sorted_cameras.sort()
    [print("{} -- {}".format(j, cameras[j])) for j in sorted_cameras]

# todo get date ranges for the cameras
if __name__ == "__main__":
    main()
