import os
from flask import Flask, render_template, request, redirect, url_for # imports libraries for flask web development

app = Flask(__name__)

d = {"username": 'jCrescencio', "password": '23four' }
u = {"username": ' ', "password":' '}

message = ""

def checkValid(user,dictionary):
    if ((user.username== dictionary.username) and (user.password== dictionary.password)):
        return True
    return False

@app.route('/login_success')
def messageInput():
    return render_template("messageInput.html", )
    
@app.route('/login_success')
def success_process():
    message = request.form['userM']
    return redirect(url_for(messageInput))
    
#Homepage#######################################
@app.route('/') # homepage route 
def loginPage():
    return render_template("loginPage.html") # renders homepage
    
@app.route('/', methods=['POST'])
def login_process(): # function that processes POST method
    u.username = request.form['username'] 
    u.password = request.form['password']
    if(checkValid(u,d)):
        return redirect(url_for(messageInput))# passes email into following "feature" template
    return redirect(url_for(loginPage))

if __name__ == '__main__':
    app.run(
        debug=True,
        port = int(os.getenv('PORT', 8080)),
        host = os.getenv('IP', '0.0.0.0')
    )