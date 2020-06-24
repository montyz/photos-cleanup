import os.path

import osxphotos


def main():
    db = os.path.expanduser("/Users/monty/Pictures/2020 Pictures/Mexico 2019.photoslibrary")
    photosdb = osxphotos.PhotosDB(db)

    for i in photosdb.album_info:
        name_list = i.folder_names[:]
        name_list.append(i.title)
        print(":".join(name_list) + " -- {}".format(len(i.photos)))



if __name__ == "__main__":
    main()
