from fileinput import filename
from sys import path_hooks
from app import fileManagement
from flask import send_from_directory, app
from app import app
import os


class File(fileManagement.FileManagement):
    def createFile(self, name):
        '''function that calls the super create() method to create a file
            params: name -> name of the file you want to create
        '''
        return super().create(name, message='File')
        

    def renameFile(self, name, newName):
        '''function that calls the super rename() method to rename a file
            params: name -> current file name
                    newName -> new name for the fiel
        '''
        return super().rename(name, newName, 'File')

    def delete(self, name):
        '''function that calls the super delete() method to delete a file
            params: name -> name of the file you want to delete
        '''
        return super().delete(name,  'File')

    def moveFile(self, path, name):
        '''function that moves a file to a new directory
            params: name -> name of the file you want to create
                    path -> new path for the file
        '''
        return super().rename(name, path, 'File')

    def getFile(self, path, name):
        '''get the file and converts it to text or binary, serves files to the frontend
        for downloading
        '''
        try:
            path = path
            filename = name
            print(path)
            print(filename)
            # print(send_from_directory(directory=path, path=filename , as_attachment = True))
            return send_from_directory(directory=path, path=filename , as_attachment = True)
        except FileNotFoundError:
            return {"error": "File not found"}

    