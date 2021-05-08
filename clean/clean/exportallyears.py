import csv
import os.path
import os
import sys
from pathlib import Path

import osxphotos


def main():
    root = '/Volumes/Photos'
    allyears = Path('%s/allyears' % root)
    libraries = [x for x in allyears.iterdir() if x.is_dir()]
    libraries.sort()
    libraries.reverse()
    destdir = Path('/Volumes/Photos/archive')
    info = Path("%s/archive/info.csv" % root)
    info.parent.mkdir(parents=True, exist_ok=True)
    with open(info, "w") as csvfileobj:
        csvfile = csv.DictWriter(csvfileobj, ["dest", "uuid", "orig", "date", "date_modified", "exif"])
        csvfile.writeheader()
        for library in libraries:
            print(library)
            print()
            db = os.path.expanduser(library)
            photosdb = osxphotos.PhotosDB(db)
            for p in photosdb.photos():
                if p.ismissing:
                    continue
                edited = p.path_edited is not None
                export_album(edited, p, destdir / library.parts[-1].split('.')[0], csvfile)


'''
Ideas for detecting duplicates:

uuid: BCFCFF52-961B-403D-A691-E99BD045FE23

original_filename: IMG_5220.JPG
date: '2016-04-14T17:20:51-07:00'

date_modified: '2020-06-15T20:30:26.554560-07:00'

exif: ExifInfo(flash_fired=False, iso=160, metering_mode=5, sample_rate=None, track_format=None,
  white_balance=0, aperture=1.8, bit_rate=None, duration=None, exposure_bias=0.0,
  focal_length=6.1, fps=None, latitude=None, longitude=None, shutter_speed=0.00625,
  camera_make='Canon', camera_model='Canon PowerShot G15', codec=None, lens_model='
  6.1-30.5mm')

'''


def export_album(edited, p, destdir, csvfile):
    year_root = destdir / p.date.strftime("%Y")
    archivedir = year_root / "archive"
    export_photo(edited, archivedir, p, csvfile)
    if len(p.album_info) == 0:
        noalbum = year_root / "aaa_noalbum"
        export_photo(edited, noalbum, p, csvfile)

    for album in p.album_info:
        export_dir = year_root
        for folder in album.folder_names:
            export_dir = export_dir / folder.replace("/", "|")
        export_dir = export_dir / album.title.replace("/", "|")
        export_photo(edited, export_dir, p, csvfile)


def export_photo(edited, export_dir, p, csvfile):
    export_dir.mkdir(parents=True, exist_ok=True)
    try:
        result = p.export(export_dir,
                          edited=edited,
                          exiftool=True,
                          use_albums_as_keywords=True,
                          increment=False,
                          overwrite=True)
        destfile = ""
        if len(result[0]) > 1:
            destfile = result
        else:
            destfile = result[0][0]
        csvfile.writerow({'uuid': p.uuid,
                          'dest': destfile,
                          'orig': p.original_filename,
                          'date': p.date,
                          'date_modified': p.date_modified,
                          'exif': p.exif_info,
                          })
        mod_time = p.date_modified
        if not mod_time:
            mod_time = p.date
        os.utime(destfile[0], (p.date.timestamp(), mod_time.timestamp()))
    except:
        print("Unexpected error:", sys.exc_info()[0])



# todo get date ranges for the cameras
if __name__ == "__main__":
    main()
