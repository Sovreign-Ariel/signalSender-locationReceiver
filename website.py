import os
from flask import Flask, render_template, request, redirect, url_for # imports libraries for flask web development

app = Flask(__name__)

dev = {
    'username': 'jCrescencio',
    'password': '23four'
    }
#u = {"username": ' ', "password":' '}

message = ""

def checkValid(user,pas):
    if user == dev["username"] and pas == dev["password"]:
        return True
    return False

@app.route('/login_success')
def messageInput():
    return render_template("maps_find.html")
    
@app.route('/login_success')
def success_process():
    message = request.form['userM']
    return redirect(url_for('messageInput'))
    
#Homepage#######################################
@app.route('/') # homepage route 
def loginPage():
    return render_template("loginPage.html") # renders homepage
    
@app.route('/', methods=['POST'])
def login_process(): # function that processes POST method
    user= request.form['username'] 
    pas = request.form['password']
    if user == dev['username'] and pas == dev['password']:
        return redirect(url_for('messageInput'))# passes email into following "feature" template
    return redirect(url_for('loginPage'))

if __name__ == '__main__':
    app.run(
        debug=True,
        port = int(os.getenv('PORT', 8080)),
        host = os.getenv('IP', '0.0.0.0')
    )