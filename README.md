# photos-cleanup
cleanup of os x photos library

# Installation

osxphotos needs to be installed, see https://github.com/RhetTbull/osxphotos#installation-instructions. I installed with `pipx`

Also install the Photos applescript library from http://photosautomation.com/scripting/script-library.html, specifically:

1. Download http://photosautomation.com/scripting/PhotosUtilitiesScriptLibrary.zip and unzip
2. `mkdir 'Script Libraries'`
3. `mv '/Users/monty/Downloads/Photos Utilities.scptd'`

### also set up python env
Follwed https://jacobian.org/2019/nov/11/python-environment-2020/


# running osxphotos 


```
osxphotos dump --db '/Users/monty/Pictures/2020 Pictures/Mexico 2019.photoslibrary' > photos.csv
```

To tag all photos in the Ceramics folder:
```
cd /Users/monty/code/photos-cleanup
osxphotos query --folder Ceramics > ceramics.csv
cd clean
python -m clean.setkeywords ../ceramics.csv "ceramics,ceramics_album"
```
To delete all photos with a tag:
1. open Photos with that library
2. search for all photos with that tag
3. select them all, then delete

To apply proper tags to all photos
```

```

# next:

- √ query all photos
- √ tag with camera model
- √ tag with album keywords, mapped

- remove photos from before 2010 that don't have a tag other than camera
- check date field for duplicates

Maybe this app for offline photos (from a website):
https://apps.apple.com/us/app/browser-offline-file-storage/id970487401

Or google photos? I downloaded the Backup and Sync from Google app.

