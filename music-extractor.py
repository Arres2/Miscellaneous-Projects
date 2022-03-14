#OJO EXTRAERA TODO LO QUE SE SE ENCUENTRE EN LOS SUBDIRECTORIOS DE DOWNLOADS

def music_extractor():
    import shutil
    import os

    path = input("Inserte una ruta completa usando doble backslash: ")
    for folderName, subfolders, filenames in os.walk(path,topdown=False):
        print('The current folder is ' + folderName)

        for subfolder in subfolders:
            try:
                os.rmdir(folderName + '\\' + subfolder)
                print('ELIMINATING FOLDER ' + folderName + '\\' + subfolder)
            except OSError:
                pass

        for filename in filenames:
            if folderName != path:
                print('FILE INSIDE ' + folderName + ': '+ filename)
                try:
                    shutil.move(folderName + "\\"+ filename, path)
                    print("FILE MOVED TO BASE FOLDER:"+ filename)
                except shutil.Error:
                    pass

        for subfolder in subfolders:
            try:
                os.rmdir(folderName + '\\' + subfolder)
                print('ELIMINATING FOLDER ' + folderName + '\\' + subfolder)
            except OSError:
                pass
    print(' ')


print("OJO: Este script extraerá todo lo que se encuentre en los subdirectorios de la carperta y eliminará los subdirectorios vacios. Si hay peliculas u otros archivos se mezclarán con las canciones.")
respuesta = input(r"Desea continuar con la extracción?: y/n ")

if respuesta == "y":
    music_extractor()
else:
    pass

