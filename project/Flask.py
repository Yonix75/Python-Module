from flask import Flask#import Flask is other module we need to used
#module is (a file containing Python code)
app = Flask(__name__)#Flask(__name__) creates the Flask application

@app.route('/')#@app.route('/')connects the home URL (/) to a function
def hello_worldd():
    return 'hello world'#The function returns text shown in the browser

#Le routage d'applications Flask est le processus d'association des URL à des fonctions spécifiques dans une application web.
#to creat route in flask @app.route


if __name__ == '__main__':
    app.run()#app.run() starts the local server
    