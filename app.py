from flask import Flask, render_template, request, redirect, url_for, abort,session 


app = Flask(__name__)
app.secret_key = "ABC123"
app.config['ENV'] = 'development'
app.config['DEBUG'] = True 
app.config['TESTING'] = True 

donation_goal = 10000
curr_don_perc = 80
donation_value = 0 

@app.route('/', methods=['POST','GET'])
def index():
    if 'dv' in session:
        donation_value = int(session['dv'])
        value = calculate_value(donation_value,donation_goal,curr_don_perc)
        return render_template('index.html', curr_value=value)
    return render_template('index.html', curr_value=curr_don_perc)

@app.route('/charity_information', methods=['POST','GET'])
def charity_infomration():
    return render_template('charity_information.html')

@app.route('/donation', methods=['POST','GET'])
def donation():
    donation_value = 0 
    if request.method == 'POST':
        if "donate" in request.form:
            donation_value = request.form['donation_value']
            session['dv'] = donation_value
            print(session['dv'])
            return redirect('/')
    return render_template('donation.html')

@app.route('/dropsession')
def dropsession():
    session.pop('dv', None)
    return 'Dropped!'

def calculate_value(donation_value, final_goal, curr_perc):
    return (int(curr_perc + donation_value/(final_goal/100)))

    
    
    


