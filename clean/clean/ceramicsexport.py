import csv
import os.path
from pathlib import Path

import osxphotos


def main():
    # db = os.path.expanduser("/Users/monty/Pictures/Master Photos Library.photoslibrary")
    db = os.path.expanduser("/Users/monty/Pictures/2020 Pictures/Ceramics 2020.photoslibrary")
    photosdb = osxphotos.PhotosDB(db)
    for p in photosdb.photos():
        if p.ismissing:
            continue
        edited = p.path_edited is not None
        for album in p.album_info:
            export_dir = Path.home() / "Pictures" / "export"
            for folder in album.folder_names:
                export_dir = export_dir / folder.replace("/", "|")
            export_dir = export_dir / album.title.replace("/", "|")
            export_dir.mkdir(parents=True, exist_ok=True)
            result = p.export(export_dir,
                              edited=edited,
                              exiftool=True,
                              use_albums_as_keywords=True,
                              increment=False,
                              overwrite=True)
            if len(result[0]) > 1:
                print(result)
            else:
                print(result[0][0])


# todo get date ranges for the cameras
if __name__ == "__main__":
    main()
