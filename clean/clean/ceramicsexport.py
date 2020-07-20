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
        for album in p.album_info:
            export_dir = Path.home() / "Pictures" / "export"
            for folder in album.folder_names:
                export_dir = export_dir / folder
            export_dir = export_dir / album.title
            export_dir.mkdir(parents=True, exist_ok=True)
            result = p.export2(export_dir,
                      exiftool=True,
                      use_albums_as_keywords=True,
                      update=True)
            print(result)



# todo get date ranges for the cameras
if __name__ == "__main__":
    main()
