# photos-cleanup
cleanup of os x photos library

# Installation

osxphotos needs to be installed, see https://github.com/RhetTbull/osxphotos#installation-instructions. I installed with `pipx`

Also install the Photos applescript library from http://photosautomation.com/scripting/script-library.html, specifically:

1. Download http://photosautomation.com/scripting/PhotosUtilitiesScriptLibrary.zip and unzip
2. `mkdir 'Script Libraries'`
3. `mv '/Users/monty/Downloads/Photos Utilities.scptd'`

### also set up python env
Followed https://jacobian.org/2019/nov/11/python-environment-2020/


# running osxphotos 


```
osxphotos dump --db '/Users/monty/Pictures/2020 Pictures/Mexico 2019.photoslibrary' > photos.csv
```

## To tag all photos in the Ceramics folder:
```
cd /Users/monty/code/photos-cleanup
osxphotos query --folder Ceramics > ceramics.csv
cd clean
python -m clean.setkeywords ../ceramics.csv "ceramics,ceramics_album"
```
## To delete all photos with a tag:
1. open Photos with that library
2. search for all photos with that tag
3. select them all, then delete
4. go to Recently Deleted and permanently delete them all

## To create list of albums to turn into tags:
```
cd /Users/monty/code/photos-cleanup/clean
pythom -m clean.albums.py
```
Edit albums.csv so the album names will map to the tags you want

## To create alltags.csv to apply to the library:
```
cd /Users/monty/code/photos-cleanup/clean
python -m clean.tagitall
```

After reviewing alltags.csv, apply it to the library:
```
cd /Users/monty/code/photos-cleanup/clean
python -m clean.setalltags alltags.csv
```

Then create smart albums for every tag.


# next:

- √ query all photos
- √ tag with camera model
- √ tag with album keywords, mapped

- remove photos from before 2010 that don't have a tag other than camera
- check date field for duplicates
- remove unused tags

### Ceramics
- try out plex as the photo app
- export the Ceramics photos preserving the folder/album structure

Maybe this app for offline photos (from a website):
https://apps.apple.com/us/app/browser-offline-file-storage/id970487401

Or google photos? I downloaded the Backup and Sync from Google app.
NO--google photos will not work without access to the ios photos library

