from app import file
import json
from flask import Response

class fileController:
    file = file.File()

    '''creates a http response for delete file functionality'''
    def httpDeletefile(self, name):
        response = json.dumps(self.file.delete(name))
        return Response(response, status=200, mimetype='application/json')
    
    '''creates a http response for rename file functionality'''
    def httpRenamefile(self, name, newName):
        response = json.dumps(self.file.renameFile(name, newName))
        return Response(response, status=200, mimetype='application/json')

    '''creates a http response for create file functionality'''
    def httpCreatefile(self, name):
        response = json.dumps(self.file.createFile(name))
        return Response(response, status=200, mimetype='application/json')

    '''creates a http response for move file functionality'''
    def httpMoveFile(self, name, path):
        response = json.dumps(self.file.moveFile(name, path))
        return Response(response, status=200, mimetype='application/json')

    '''creates a http response for download functionality'''
    def httpDownloadFile(self, path, name):
        return self.file.getFile(path, name)




 