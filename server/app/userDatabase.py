import csv
from app import folder

class UserDatabase:
    '''a depiction of noSQL database'''
    folder = folder.Folder()
    filename = 'users.csv'
    fields = ['password', 'username']
    data = []

    def __init__(self):
        '''constructor for userDatabase class'''
        with open(self.filename, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fields)
            writer.writeheader()
        
    def ReadDatabase(self):
        '''the function reads the csv file and sores the data inside the data array for future use'''
        with open(self.filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.data.append(dict(row))
    
    def Register(self, username, password):
        '''using the information from frontend, the function registers the user
        in a csv file
        params: username -> username of the user
        '''
        if self.SearchUser(username.lower()):
            return {'error': 'Username exists'}
        else:
            new_user ={
                "username": username.lower(),
                "password": password
            }
            with open(self.filename, 'a') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.fields)
                writer.writerow(new_user)
                # self.data.append(new_user)
                self.folder.createFolder(username)
                self.folder.changeDirectory('./' + username)
            return {'success': "user registered"}

    def SearchUser(self, username):
        '''querries the user in the database
            params: username -> username of the user
        '''
        self.ReadDatabase()
        for row in self.data:
            for key, val in row.items():
                if username in val.lower():
                    return True
        return False

    def Login(self, username, password):
        '''using the information from frontend, the function authenticates the user
        using a csv file
        params: username -> username of the user
        '''
        self.ReadDatabase()
        for row in self.data:
            for key, val in row.items():
                if username in val.lower() and password in val:
                    self.folder.changeDirectory('./' + username)
                    return {'success': "user logging in"}
        return {"error": "username does not exist"}


