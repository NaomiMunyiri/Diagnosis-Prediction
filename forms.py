from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, PasswordField,EmailField
from wtforms.validators import DataRequired, Email, EqualTo,InputRequired


#Form risk
class RisksForm(FlaskForm):
    #email=EmailField("What is your account mail",validators=[InputRequired()])
    age=IntegerField("How old are you?", validators=[InputRequired()])
    sexual_partners_no=IntegerField("How many sexual partners have you had?", validators=[InputRequired()])
    sexual_partners_age=IntegerField("How old were you when you first had sexual intercourse?", validators=[InputRequired()])
    pregnancies=IntegerField("How many pregnancies have you had?", validators=[InputRequired()])
    smoked_years=IntegerField("How many years have you smoked?", validators=[InputRequired()])
    packs_year=IntegerField("Estimated packs of cigarrettes per year", validators=[InputRequired()])
    hormonal_contraceptives=IntegerField("Years on hormonal contraceptives", validators=[InputRequired()])
    IUD_years=IntegerField("Years on IUD", validators=[InputRequired()])
    STD=BooleanField("Have you had any Sexually Transmitted Diseases(STDs)?")
    STD_number=IntegerField("How many STDs have you had?", validators=[InputRequired()])
    Condylomatosis=BooleanField("Condylomatosis")
    #Cervical=BooleanField("Cervical Condylomatosis")
    Vaginal=BooleanField("Vaginal Condylomatosis")
    Vulvo=BooleanField("Vulvo-Perineal Condylomatosis")
    Syphilis=BooleanField("Syphilis")
    Pelvic=BooleanField("Pelvic Inflammatory Disease")
    Herpes=BooleanField("Genital Herpes")
    Molluscum=BooleanField("Molluscum Contagiosum")
    #AIDS=BooleanField("AIDS")
    HIV=BooleanField("HIV")
    Hep=BooleanField("Hepatisis B")
    HPV=BooleanField("HPV")
    STD_diagnosis=IntegerField("Number of STD diagnosis'", validators=[InputRequired()])
    Cancer=BooleanField("DX:Cancer")
    Cin=BooleanField("DX:Cin")
    DX_HPV=BooleanField("DX:HPV")
    Dx=BooleanField("DX")
    Hinselmann=BooleanField("Hinselmann")
    Schiller=BooleanField("Schiller")
    Citology=BooleanField("Citology")
    submit=SubmitField("Submit")

#Form user
class UserForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    password_hash = PasswordField('Password', validators=[DataRequired(), EqualTo('password_hash2', message='Passwords Must Match!')])
    password_hash2 = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField("Submit")

#login form
class LoginForm(FlaskForm):
    email=EmailField("Email", validators=[DataRequired()])
    password=PasswordField("Password",validators=[DataRequired()])
    submit=SubmitField("Submit")