### File Library ###
import os
from .ui import *

def initPathToParentDir(filePathAttr):
	return os.path.dirname(os.path.realpath(filePathAttr))

#Standard Path Init
def goToPath(pathToParentDir, path):
	os.chdir(pathToParentDir+"/{}".format(path))

#Standard File In
def wFileData(pathToParentDir, pathToFolder, filename, data, isOverwrite):
	goToPath(pathToParentDir, pathToFolder)
	mode = "a"
	if isOverwrite: mode = "w"
	with open(filename, mode) as f:
		f.write(data)

#Standard File Out
def rFileData(pathToParentDir, pathToFolder, filename):
	goToPath(pathToParentDir, pathToFolder)
	with open(filename, "r") as f:
		data = "".join(f.readlines())
		return data

#File Select UI
def gInternalFile(pathToParentDir, folder, question):
	goToPath(pathToParentDir, folder)
	items = os.listdir()
	filename = gList(question, [x for x in items if x[0] != "."], False)
	print(filename)
	return filename

#File Generation UI
def mFile(pathToParentDir, pathToFolder, data, fileType):
	goToPath(pathToParentDir, pathToFolder)
	while True:
		refresh()
		filename = input("Name of new file: ")
		if os.path.exists(filename+fileType):
			errorMessage("That file already exists!")
		else:
			break
	wFileData(pathToParentDir, pathToFolder, filename+fileType, data, True)
