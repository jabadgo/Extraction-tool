import os
import zipfile

while True:
    mydir = raw_input("Please write the path to where the files you want to extract are. \nPath:") #The directory where the .zip files are
    print "Your path is:", mydir, "\n"
    if mydir != " ":
        break
    else:
        print "You didn't write a path, try again."

targetDir = raw_input("Please write the path to where you want to extract the files. Leave this empty if you want to use the source directory. \nPath:") #The directory in which you want to extract the files
if targetDir == " ":
    targetDir = mydir
    print "Your extraction path is:", targetDir, "\n"


for file in os.listdir(mydir):
    if file.endswith(".zip"): #check filetype
        filePath = (os.path.join(mydir, file))
        targetFile = file.split(".") #remove the .zip suffix from the target filename
        with zipfile.ZipFile(filePath,'r') as zip_ref:
            zip_ref.extractall(targetDir + "/" + targetFile[0])
