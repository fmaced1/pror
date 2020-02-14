from flask import Flask
from .api.functions.shell import run_shell

app = Flask(__name__)

@app.route('/',methods=['GET',])
def home():
    return '<pre>'+run_shell()+'</pre>'

if __name__ == '__main__':
    app.run(debug=True)