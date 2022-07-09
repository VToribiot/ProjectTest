import glob, re, os, csv
import os.path


def checkForSignatures():
    print("Checking for virus signatures")
    programs = glob.glob("*.*")
    for p in programs:
        thisFileInfected = False
        file = open(p, "r")
        lines = file.readlines()
        file.close()

        for line in lines:
            if re.search("^# starting virus code", line):
                print("- Virus found in file" + p)
                thisFileInfected = True
            if not thisFileInfected:
                print(p + " appears to be clean")

    print("End Section")

def getFileData():
    programs = glob.glob("*.*")
    programList = []
    for p in programs:
        programSize = os.path.getsize(p)
        programModified = os.path.getmtime(p)
        programData = [p, programSize, programModified]
        programList.append(programData)
    return programList

def WriteFileData(programs):
    if (os.path.exists("fileData.text")):
        return
    with open("fileData.txt", "w") as file:
        wr = csv.writer(file)
        wr.writerows(programs)

def checkForChanges():
    print("Check for heuristic changes")

    with open("fileData.txt") as file:
        fileList = file.read().splitlines()
    originalFileList = []
    for each in fileList:
        items = each.split(',')
        originalFileList.append(items)

    currentFileList = getFileData()

    for c in currentFileList:
        for o in originalFileList:
            if c[0] == o[0]:
                if str(c[1]) != str(o[1]) or str(c[2] != str(o[2])):
                    print("Inconsistencia de archivos")
                    print("Valores actuales: " + str(c))
                    print("Original values: " + str(o))
                else:
                    print("FIle " + c[0] + " appears to be unchanged")

    print("Finished checking for changes in files")

WriteFileData(getFileData)

checkForSignatures()
checkForChanges()