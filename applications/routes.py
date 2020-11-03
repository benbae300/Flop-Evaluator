from applications import app 

from flask import redirect, render_template, flash, request, session, url_for
from .forms import LoginForm, SignupForm
from .models import db, User
from . import login_manager
from flask_login import login_user, logout_user, login_required, current_user

import applications.Evaluator.breakdownTheRange as bt
from .Evaluator.classifyFlop import classify
from .Evaluator.handVsRange import handVsRange
from .Evaluator.card import Card

import json

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('titlepage.html')  

@app.route('/home')
@login_required
def routeHome():
    return render_template('home.html', name = current_user.name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()  # Validate Login Attempt
        if user and user.check_password(password=form.password.data):
            login_user(user)
            #next_page = request.args.get('next')
            return render_template('home.html', name = current_user.name)
        flash('Invalid username/password combination')
        return render_template('login.html', form = form )    
    return render_template('login.html', form = form )    



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(name=form.name.data).first()
        if existing_user is None:
            print('hello')
            user = User(name=form.name.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()  # Create new user
            login_user(user)  # Log in as newly created user
            return render_template('home.html', name = current_user.name)
        flash('A user already exists with that username.')

 
    return render_template('signup.html', form = form )  

@app.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return render_template('titlepage.html')  

@app.route("/titlepage")
def getTitlePage():
    """User log-out logic."""
    return render_template('titlepage.html')  

@app.route('/ranges')
@login_required
def routeRanges():
    return render_template('ranges.html')

@app.route('/faq')
@login_required
def routeFAQ():
    return render_template('faq.html')



@app.route('/findFlop')
@login_required
def routeFindFlop():    
    return render_template('findFlop.html')

@app.route('/allRangesHands')
@login_required
def routeAllRangesHands():
    return render_template('allRangesHands.html')

@app.route('/handRange', methods=['GET', 'POST'])
@login_required
def routeHandRange():
    if request.method == 'POST':
        req = request.json
        hand = [Card(req['h1'][0],req['h1'][1].lower()), Card(req['h2'][0],req['h2'][1].lower())]
        flop = [
                Card(req['f1'][0],req['f1'][1].lower()),
                Card(req['f2'][0],req['f2'][1].lower()),
                Card(req['f3'][0],req['f3'][1].lower())
                ]

        eq = handVsRange(req['pos'], hand, req['r1'], req['r2'], req['action'], flop)
        trueEquity = str(( int((eq) *100* 100) / 100)) + '%'
        return json.dumps({'success':True, 'equity':trueEquity}), 200, {'ContentType':'application/json'} 
    return render_template('handRange.html')

def cleanURL(url):
    return 'UTG/HJ' if '%2F' in url else url 


@app.route('/data')
@login_required
def getData():
    print(request.url)
    u = request.url.split('?')
    url = u[1].split('%3F')
    action, r1, r2 = url[0], url[1], url[2]
    r1 = cleanURL(r1)
    r2 = cleanURL(r2)
    f = [url[3].lower(),url[4].lower(),url[5].lower()]
    flop = []
    for c in f: 
        flop.append(Card(c[0].upper(), c[1]))
    range1, range2 = bt.breakdownTheRange(action, r1, r2, flop)
    flopClass = classify(flop)

    ranges = [range1, range2 ]
    return render_template('data.html', ranges = ranges, flopClass = flopClass )


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    return render_template('titlepage.html')  