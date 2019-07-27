from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True 
app.config['TESTING'] = True 

@app.route('/', methods=['POST','GET'])
def home():
    return render_template('index.html')