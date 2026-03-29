from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def jsonify():
    return "message: Pokemon API is running"

@app.route("/hello/<name>")
def hello(name):
    r = f"hello: {name}" 
    return jsonify(r)


@app.route("/status")
def status_server():
    r = f"Status : OK!\n Running Time..." 
    return jsonify(r)
    
if __name__ == "__main__": 
    app.run()
    
    