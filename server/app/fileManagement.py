import os
from datetime import datetime

class FileManagement:

    def delete(self, name, message):
        '''function that calls the os to delete a file or folder 
            params: name: name of file
                    message: whether 'File' or 'Folder'
        '''
        try:
            # os.rmdir(name)
            if message == 'Folder':
                os.rmdir(name)
            else:
                os.remove(name)
            return {"success": message + " deleted"}
        except:
            return {"error": message + " not deleted"}

    def rename(self, name, newName, message):
        '''function that calls the os to rename a file or folder 
            params: name: current file name
                    newName: new name for the file or folder
                    message: whether 'File' or 'Folder'
        '''
        try:
            os.rename(name, newName)
            return {"success": message + " renamed"}
        except OSError:
            return {"error": message + " name exist"}

    def create(self, name, message):
        '''function that calls os to create a file or folder
            params: name: name of file
                    message: whether 'File' or 'Folder'
        '''
        if message == 'Folder':
            os.mkdir(name)
            {"success": "Folder created"}
        else:
            try:
                fp = open(name, 'x')
                fp.close()
                return {"success": "File created"}
            except:
                return {"error":"File not created"}
