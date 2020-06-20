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

osxphotos dump --db '/Users/monty/Pictures/2020 Pictures/Mexico 2019.photoslibrary' > photos.csv

