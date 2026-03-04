from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Name: Parth</h1><h2>AppID: 101</h2><h3>Hobbies: Coding, Reading, Gaming</h3>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
