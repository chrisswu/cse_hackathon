from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True 
app.config['TESTING'] = True 

@app.route('/', methods=['POST','GET'])
def home():
    # if request.method  == 'POST':
    return render_template('index.html')

@app.route('/charity_information', methods=['POST','GET'])
def charity_infomration():
    return render_template('charity_information.html')

@app.route('/donation', methods=['POST','GET'])
def donation():
    return render_template('donation.html')

