from app import app, folderController, fileController
from flask import request
from app import folder
import os

folders = folderController.FolderController()
files = fileController.fileController()

'''listens for upload routes and calls the appropriate method to deal with the required functionaliy'''
@app.route('/upload', methods=['POST'])
def upload():
    fold = folder.Folder() 
    files = request.files.getlist('files')
    path = fold.getFolderInformation()[0]['path']
    for index, file in enumerate(files):
        print(file)
        file.save(os.path.join(path, file.filename))
    return {"success": "Files uploading"}


'''listens for file download routes and calls the appropriate method to deal with the required functionaliy''' 
@app.route('/downloadfile/', methods=["POST"])
def downloadFile():
    path = request.json['path'] 
    name = request.json['name']
    return files.httpDownloadFile(path, name)

'''listens for get current working directory routes and calls the appropriate method to deal with the required functionaliy'''   
@app.route('/', methods=['GET'])
def getCurrentDirectory():
    return folders.httpCurrentWorkingDirectory()

'''listens for change directory routes and calls the appropriate method to deal with the required functionaliy'''
@app.route('/folder/changedirectory/', methods=['POST'])
def changeDirectory():
    res = request.json['path']
    return folders.httpChangeDirectory(res)

'''listens for delete folder routes and calls the appropriate method to deal with the required functionaliy'''
@app.route('/folder/delete/<name>', methods=['GET'])
def DeleteDirectory(name):
    return folders.httpDeleteFolder(name)

'''listens for rename folder routes and calls the appropriate method to deal with the required functionaliy'''
@app.route('/folder/rename/<name>/<newname>', methods=['GET'])
def renameDirectory(name, newname):
    return folders.httpRenameFolder(name, newname)

'''listens for create folder routes and calls the appropriate method to deal with the required functionaliy'''
@app.route('/folder/create/<name>', methods=['GET'])
def createDirectory(name):
    return folders.httpCreateFolder(name)

'''listens for create file routes and calls the appropriate method to deal with the required functionaliy'''
@app.route('/file/create/<name>', methods=['GET'])
def createFile(name):
    return files.httpCreatefile(name)

'''listens for rename file routes and calls the appropriate method to deal with the required functionaliy'''
@app.route('/file/rename/<name>/<newname>', methods=['GET'])
def rename(name, newname):
    return files.httpRenamefile(name, newname)

'''listens for create file routes and calls the appropriate method to deal with the required functionaliy'''
@app.route('/file/create/<name>/<newname>', methods=['GET'])
def renameFile(name, newname):
    return files.httpRenamefile(name, newname)

'''listens for delete file routes and calls the appropriate method to deal with the required functionaliy'''
@app.route('/file/delete/<name>', methods=['GET'])
def deleteFile(name):
    return files.httpDeletefile(name)

'''listens for file move routes and calls the appropriate method to deal with the required functionaliy'''
@app.route('/file/move', methods=['POST'])
def delete(currentpath, newpath):
    path = request.json['path']
    filename = request.json['name']
    return files.httpMoveFile(filename, path)


