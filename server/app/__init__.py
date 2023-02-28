from flask import Flask
from flask_cors import CORS

app =Flask(__name__)
CORS(app)


from app import fileManagement
from app import file
from app import fileController
from app import folderRouter
from app import folderController
from app import folder
from app import authRouter
from app import userDatabase





