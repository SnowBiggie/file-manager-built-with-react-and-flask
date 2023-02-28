from app import folder
import json
from flask import Response
# import folder

class FolderController:
    folder = folder.Folder()

    '''creates a http response for get working directory functionality'''
    def httpCurrentWorkingDirectory(self):
        response = json.dumps(self.folder.getFolderInformation())
        return Response(response, status=200, mimetype='application/json')

    '''creates a http response for change directory functionality'''
    def httpChangeDirectory(self, path):
        response = json.dumps(self.folder.changeDirectory(path))
        return Response(response, status=200, mimetype='application/json')

    '''creates a http response for delete folder functionality'''
    def httpDeleteFolder(self, name):
        response = json.dumps(self.folder.deleteFolder(name))
        return Response(response, status=200, mimetype='application/json')
    
    '''creates a http response for rename folder functionality'''
    def httpRenameFolder(self, name, newName):
        response = json.dumps(self.folder.renameFolder(name, newName))
        return Response(response, status=200, mimetype='application/json')
    
    '''creates a http response for create folder functionality'''
    def httpCreateFolder(self, name):
        response = json.dumps(self.folder.createFolder(name))
        return Response(response, status=200, mimetype='application/json')
    

        


