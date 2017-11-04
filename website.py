
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"

d = {"username": 'jCrescencio', "password": '23four' }

print(d["username"])
print(hello())

app = Flask(__name__)

