#
#Server for creating FILEMAN
#
from app import app

#Start the server
if __name__ == "__main__":
    app.run(debug=True, threaded = True, port=8000)
    #app.run()