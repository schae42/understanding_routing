
from flask import Flask  
app = Flask(__name__)

@app.route('/')         
def hello_world():
    return 'Hello World!'

@app.route('/dojo')         
def hello_dojo():
    return 'Dojo!'

@app.route('/say/<name>')         
def hi(name):
    print("*"*80)
    print("in hi function")
    print(name)
    return f"Hello {name}!"

@app.route('/repeat/<number>/<name>')         
def repeat(number, name):
    return int(number) * f"{name} "

if __name__=="__main__":
    app.run(debug=True)
