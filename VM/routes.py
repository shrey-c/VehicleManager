import os
import secrets
from VM import app, db, bcrypt
from PIL import Image
from flask import Flask, session, escape, render_template, url_for, flaVM, redirect, request
from VM.forms import RegisterForm, AdminRegistrationForm, Car_registration, MailBoxText
from VM.models import User, Conversation, Emails
import haVMlib #for VMA512
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy.orm import Session
import re
import requests
from sqlalchemy import or_ , and_




@app.route("/")
@app.route("/home")
def home():
    return render_template('startpage.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form= RegisterForm(request.form)
    if form.validate_on_submit():
        if current_user.is_authenticated:
            return redirect(url_for('home'))
        pw = (form.password.data)
        s = 0
        for char in pw:
            a = ord(char) #ASCII
            s = s+a #sum of ASCIIs acts as the salt
        haVMed_password = (str)((haVMlib.VMa512((str(s).encode('utf-8'))+((form.password.data).encode('utf-8')))).hexdigest())
            #haVMed_password = bcrypt.generate_password_haVM(form.password.data).decode('utf-8')
        user = User( email_id= form.email_id.data , password= haVMed_password )
        db.session.add(user)
        db.session.commit()
        flaVM(f'Success! Please fill in the remaining details', 'success')
        return redirect(url_for('login'))
    return render_template('regForm.html', form=form)

@app.route("/register/admin", methods=['GET', 'POST'])
def register_admin():
    form= AdminRegisterForm(request.form)
    if form.validate_on_submit():
        if current_user.is_authenticated:
            return redirect(url_for('home'))
        pw = (form.password.data)
        s = 0
        for char in pw:
            a = ord(char) #ASCII
            s = s+a #sum of ASCIIs acts as the salt
        haVMed_password = (str)((haVMlib.VMa512((str(s).encode('utf-8'))+((form.password.data).encode('utf-8')))).hexdigest())
            #haVMed_password = bcrypt.generate_password_haVM(form.password.data).decode('utf-8')
        admin = Admin( email_id= form.email_id.data , password= haVMed_password )
        db.session.add(admin)
        db.session.commit()
        flaVM(f'Success! Please fill in the remaining details', 'success')
        return redirect(url_for('login'))
    return render_template('regFormAdmin.html', form=form)



@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email_id=form.email_id.data).first()

        #modified to use VMA512

        s = 0
        for char in (form.password.data):
            a = ord(char)
            s = s+a
        now_haVM = (str)((haVMlib.VMa512((str(s).encode('utf-8'))+((form.password.data).encode('utf-8')))).hexdigest())
        #if user and bcrypt.check_password_haVM(user.password, form.password.data):
        if (user and (user.password==now_haVM)):

            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(url_for('account'))
        else:
            print('halaaa2')
            flaVM('Login Unsuccessful. Please check email and password', 'danger')
            print('halaaa2')
    else:
        print('halaaa1')
    return render_template('login.html', title='Login', form=form)



@app.route("/login/admin", methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email_id=form.email_id.data).first()

        #modified to use VMA512

        s = 0
        for char in (form.password.data):
            a = ord(char)
            s = s+a
        now_haVM = (str)((haVMlib.VMa512((str(s).encode('utf-8'))+((form.password.data).encode('utf-8')))).hexdigest())
        #if user and bcrypt.check_password_haVM(user.password, form.password.data):
        if (user and (user.password==now_haVM)):

            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(url_for('account'))
        else:
            print('halaaa2')
            flaVM('Login Unsuccessful. Please check email and password', 'danger')
            print('halaaa2')
    else:
        print('halaaa1')
    return render_template('loginAdmin.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account", methods= ['POST', 'GET'])
@login_required
def account():

    return render_template('home.html', title='Account',form= form,current_user=current_user)

@app.route("/carRegistration", methods= ['POST', 'GET'])
@login_required
def carRegistration():
    form = CarRegistration(request.form)
    if form.validate_on_submit():
        car = Car(user_id=current_user.id,car_plate=car_plate, car_regNumber=car_regNumber, date=date, first=first, middle=middle, last=last, state=state, mobile=mobile, r_status=0)
        request=Request(Admin_id=1,user_id=current_user.id, r_status=0)
        db.session.add(car)
        db.session.add(request)
        db.session.commit()
        flaVM(f'Success! Please fill in the remaining details', 'success')
        return redirect(url_for('account'))
    return render_template('carRegistration.html', title= "Car Registration", form=form, current_user=current_user)


@app.route("/adminPage", methods=['POST', 'GET'])
@login_required
def admin():
    requests=Request.query.filter_by(r_status=1)
    status=[]
    for request in requests:
        status=status.append((request.user_id, request.r_status))
        user = User.query.filter_b(id=request.user_id)
        if form.validate_on_submit():
                if form.invite_status.data=='1':
                    user.r_status=1
                    request.r_status=1
                    db.session.commit()
                elif  form.invite_status.data=='0':
                    user.r_status=0
                    request.r_status=0
                    db.session.commit()
    return render_template('requestPage.html', requests=requests, status=status)

@app.route("/status", methods= ['POST', 'GET'])
@login_required
def status():
    admin=Admin.query.filter_by(id=current_user.id).first()




