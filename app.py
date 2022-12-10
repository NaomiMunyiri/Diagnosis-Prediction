from flask import Flask, render_template, request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from flask import flash
from flask_login import UserMixin,login_user,LoginManager,login_required,logout_user,current_user
from werkzeug.security import generate_password_hash, check_password_hash
from forms import UserForm,LoginForm,RisksForm
import numpy as np
import pickle
#from joblib import load
from numpy import int64
#import pandas

app= Flask(__name__) #creates instance of flask
#add database
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///cervical_cancer.db'
app.config['SECRET_KEY']="secret"
#initialize the database
db=SQLAlchemy(app)
migrate=Migrate(app,db)

#load model
model=pickle.load(open('cancermodel.sav','rb'))


#flask login
login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'

@login_manager.user_loader#loads user when logged in
def load_user(email):
    return Users.query.get(email)

#ROUTES
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")


#uploading risk form
@app.route('/risk/add', methods=['GET','POST'])
def add_risk():
    form = RisksForm()
    if form.validate_on_submit():
        risk=Cervical_Cancer(
                            email=form.email.data,
                            age=form.age.data,
                            sexual_partners_no=form.sexual_partners_no.data,
                            sexual_partners_age=form.sexual_partners_age.data,
                            pregnancies=form.pregnancies.data,
                            smoked_years=form.smoked_years.data,
                            packs_year=form.packs_year.data,
                            hormonal_contraceptives=form.hormonal_contraceptives.data,
                            IUD_years=form.IUD_years.data,
                            STD=form.STD.data,
                            STD_number=form.STD_number.data,
                            Condylomatosis=form.Condylomatosis.data,
                            #Cervical=form.Cervical.data,
                            Vaginal=form.Vaginal.data,
                            Vulvo=form.Vulvo.data,
                            Syphilis=form.Syphilis.data,
                            Pelvic=form.Pelvic.data,
                            Herpes=form.Herpes.data,
                            Molluscum=form.Molluscum.data,
                            #AIDS=form.AIDS.data,
                            HIV=form.HIV.data,
                            Hep=form.Hep.data,
                            HPV=form.HPV.data,
                            STD_diagnosis=form.STD_diagnosis.data,
                            Cancer=form.Cancer.data,
                            Cin=form.Cin.data,
                            DX_HPV=form.DX_HPV.data,
                            Dx=form.Dx.data,
                            Hinselmann=form.Hinselmann.data,
                            Schiller=form.Schiller.data,
                            Citology=form.Citology.data)
        db.session.add(risk)
        db.session.commit()
        form=RisksForm(formdata=None)#clears the form
        flash("Variables added successfully!")

        x = model.predict([[form.age.data,form.sexual_partners_no.data,form.sexual_partners_age.data,
        form.pregnancies.data,form.smoked_years.data,form.packs_year.data,form.hormonal_contraceptives.data,form.IUD_years.data,
        form.STD.data,form.STD_number.data,form.Condylomatosis.data,form.Vaginal.data,form.Vulvo.data,form.Syphilis.data,
        form.Pelvic.data,form.Herpes.data,form.HIV.data,form.Hep.data,form.HPV.data,form.STD_diagnosis.data,
        form.Cancer.data,form.Cin.data,form.DX_HPV.data,form.Dx.data,form.Hinselmann.data,form.Schiller.data,form.Citology.data]])
        print("Cancer [0 - No Yes - 1] :\n Result : ",[x])
                
    return render_template("add_risk.html",**locals())

#registering new user
@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    form=UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            # Hash the password!!!
                hashed_pw = generate_password_hash(form.password_hash.data, "sha256")
                user = Users(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data,password_hash=hashed_pw)
                db.session.add(user)
                db.session.commit()
        form.first_name.data = ''
        form.last_name.data = ''
        form.email.data = ''
        form.password_hash.data = ''
        flash("User Added Successfully!")
    return render_template("add_user.html",form=form)

#login page
@app.route('/login', methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()
        if user:
            #check hash
            if check_password_hash(user.password_hash, form.password.data):
                login_user(user)
                flash("Login Successful!")
                return redirect(url_for('dashboard'))
            else:
                flash("Wrong Passoword-Try Again!")
        else:
            flash("That User Doesn't Exist-Try Again!")

    return render_template('login.html',form=form)

#dashboard page
@app.route('/dashboard', methods=['GET','POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')

#logout page
@app.route('/logout', methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    flash("You Have Been Logged Out!")
    return redirect(url_for('login'))



#CLASS MODELS
#database model
class Cervical_Cancer(db.Model):
    id=db.Column(db.Integer, primary_key=True)#creates column s in database
    date_created=db.Column(db.DateTime, default=datetime.now)
    email=db.Column(db.String,nullable=False)
    age=db.Column(db.Integer, nullable=False)
    sexual_partners_no=db.Column(db.Integer, nullable=False)
    sexual_partners_age=db.Column(db.Integer, nullable=False)
    pregnancies=db.Column(db.Integer, nullable=False)
    smoked_years=db.Column(db.Integer, nullable=False)
    packs_year=db.Column(db.Integer, nullable=False)
    hormonal_contraceptives=db.Column(db.Integer, nullable=False)
    IUD_years=db.Column(db.Integer, nullable=False)
    STD=db.Column(db.Boolean, nullable=False)
    STD_number=db.Column(db.Integer, nullable=False)
    Condylomatosis=db.Column(db.Boolean, nullable=False)
    #Cervical=db.Column(db.Boolean, nullable=False)
    Vaginal=db.Column(db.Boolean, nullable=False)
    Vulvo=db.Column(db.Boolean, nullable=False)
    Syphilis=db.Column(db.Boolean, nullable=False)
    Pelvic=db.Column(db.Boolean, nullable=False)
    Herpes=db.Column(db.Boolean, nullable=False)
    Molluscum=db.Column(db.Boolean, nullable=False)
    #AIDS=db.Column(db.Boolean, nullable=False)
    HIV=db.Column(db.Boolean, nullable=False)
    Hep=db.Column(db.Boolean, nullable=False)
    HPV=db.Column(db.Boolean, nullable=False)
    STD_diagnosis=db.Column(db.Integer, nullable=False)
    Cancer=db.Column(db.Boolean, nullable=False)
    Cin=db.Column(db.Boolean, nullable=False)
    DX_HPV=db.Column(db.Boolean, nullable=False)
    Dx=db.Column(db.Boolean, nullable=False)
    Hinselmann=db.Column(db.Boolean, nullable=False)
    Schiller=db.Column(db.Boolean, nullable=False)
    Citology=db.Column(db.Boolean, nullable=False)

    #create function to return string when we add something
    def __repr__(self):
        return '<Age %r>' % self.id
 
#users model
class Users(db.Model, UserMixin):
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, primary_key=True)

    # Do some password stuff!
    password_hash = db.Column(db.String(128))
    
    def get_id(self):
        return self.email

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute!')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Create A String
    def __repr__(self):
        return '<Name %r>' % self.name