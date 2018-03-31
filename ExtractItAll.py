import os
import zipfile

filename = []
filePath = []

mydir = ".../mydirA" #The directory where the .zip files are
targetDir = ".../mydirB" #The directory in which you want to extract the files

for file in os.listdir(mydir):
    if file.endswith(".zip"):
        myPath = (os.path.join(mydir, file))
        targetFile = file.split(".")
        with zipfile.ZipFile(myPath,'r') as zip_ref:
            zip_ref.extractall(targetDir + "/" + targetFile[0])
