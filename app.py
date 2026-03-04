```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Name: Parth</h1><h2>AppID: 2410244</h2><h3>Hobbies: Coding, Reading, Gaming</h3>'

if __name__ == '__main__':
    app.run(debug=True)
```
