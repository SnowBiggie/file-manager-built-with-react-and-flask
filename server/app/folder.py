import os
import pathlib
from datetime import datetime
from app import fileManagement
import os,io,zipfile,time
from flask import send_file

class Folder(fileManagement.FileManagement):
    '''calls the os to get folder/directory information,
    each file/folder properties are put into a dictionary
    and send to the frontend
    '''
    def getFolderInformation(self):
    	
        try:
            i = 0
            # Dictionary to hold file/folder properties
            folderProperties = {}
            # All directory iinformation will be stored in this array
            allFiles = []
            # Get current working current directory
            path = os.getcwd()
            # scan for file and folders in the current working directory
            folderInformation = os.scandir(path)
            # Loops through all the files in the working directory
            for entry in folderInformation:
                # checks if file or folder 
                if entry.is_dir() or entry.is_file():
                    # gets the name fo the file/foder
                    name = entry.name
                    extension = pathlib.Path(name).suffix
                    ext = extension.replace('.','')
                    # Gets file path
                    currentPath = path + '/' + name
                    # the following three lines get the different dates of the file(createdTime, modificationDate and lastAccesedTime)
                    lastAccesedTime = datetime.fromtimestamp(os.path.getatime(currentPath)).strftime("%A, %B %d, %Y %I:%M:%S")
                    createdTime = datetime.fromtimestamp(os.path.getctime(currentPath)).strftime("%A, %B %d, %Y %I:%M:%S")
                    lastModificationTime  = datetime.fromtimestamp(os.path.getmtime(currentPath)).strftime("%A, %B %d, %Y %I:%M:%S")
                    folderProperties = dict({"name": entry.name, 
                    "size": os.path.getsize(currentPath), 
                    "ext": ext,
                    "lastAccesedTime": lastAccesedTime, 
                    "createdTime": createdTime, 
                    "lastModificationTime": lastModificationTime, 
                    "path": path,
                    "type": self.fileOrFolder(name),
                    "key": i
                    })
                    allFiles.append(folderProperties)
                    i = i + 1
            return allFiles
        except:
            return {"error": "Can't get Directory"}

    def changeDirectory(self, path):
        '''changes path'''
        try:
            os.chdir(path)
            # return {"sucess": "Directory changed"}
            return {"success": "Directory changed"}
        except:
            return {"error": "Directory does not exist"}

    def fileOrFolder(self, name):
        '''check if an iten is a file or folder
        params: name-> name of the folder'''
        
        if '.' in name:
            return 'File'
        return 'Folder'

    def deleteFolder(self, name):
        '''function that calls the super delete() method to delete a folder
            params: name -> name of the folder you want to delete
        '''
        return super().delete(name, 'Folder')
        
    def createFolder(self, name):
        '''function that calls the super create() method to create a folder
            params: name -> name of the folder you want to create
        '''
        try:
            if '.' not in name:
                super().create(name, "Folder")
                return {"success": "Directory created"}
            else:
                return {"error": "Directory must not have a dot`.`"}
        except:
            return {"error": "Directory name exist"}

    def renameFolder(self, name, newName):
        '''function that calls the super rename() method to rename a folder
            params: name -> current folder name
                    newName -> new name for the folder
        '''
        return super().rename(name, newName, 'Folder')
       


