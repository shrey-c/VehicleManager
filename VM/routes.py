import os
import secrets
from VM import app, db, bcrypt
from PIL import Image
from flask import Flask, session, escape, render_template, url_for, flash, redirect, request
from VM.forms import RegisterForm, AdminRegisterForm, CarRegistration, RegisterForm, LoginForm, AdminLoginForm,RequestForm
from VM.models import User, Admin, Car, Request
import hashlib #for sha512
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy.orm import Session
import re
import requests
from sqlalchemy import or_ , and_




@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('index.html')


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
        hashed_password = (str)((hashlib.sha512((str(s).encode('utf-8'))+((form.password.data).encode('utf-8')))).hexdigest())
            #hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User( email_id= form.email_id.data , password= hashed_password )
        db.session.add(user)
        db.session.commit()
        flash(f'Success! Please fill in the remaining details', 'success')
        return redirect(url_for('login'))
    return render_template('regForm.html', form=form)

@app.route("/adminRegister", methods=['GET', 'POST'])
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
        hashed_password = (str)((hashlib.sha512((str(s).encode('utf-8'))+((form.password.data).encode('utf-8')))).hexdigest())
            #hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        admin = Admin( email_id= form.email_id.data , password= hashed_password )
        db.session.add(admin)
        db.session.commit()
        flash(f'Success! Please fill in the remaining details', 'success')
        return redirect(url_for('login_admin'))
    return render_template('regFormAdmin.html', form=form)



@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email_id=form.email_id.data).first()

        #modified to use sha512

        s = 0
        for char in (form.password.data):
            a = ord(char)
            s = s+a
        now_hash = (str)((hashlib.sha512((str(s).encode('utf-8'))+((form.password.data).encode('utf-8')))).hexdigest())
        #if user and bcrypt.check_password_hash(user.password, form.password.data):
        if (user and (user.password==now_hash)):

            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(url_for('account'))
        else:
            print('halaaa2')
            flash('Login Unsuccessful. Please check email and password', 'danger')
            print('halaaa2')
    else:
        print('halaaa1')
    return render_template('login.html', title='Login', form=form)



@app.route("/adminLogin", methods=['GET', 'POST'])
def login_admin():
    form = AdminLoginForm(request.form)
    if form.validate_on_submit():
        admin = Admin.query.filter_by(email_id=form.email_id.data).first()

        #modified to use sha512

        s = 0
        for char in (form.password.data):
            a = ord(char)
            s = s+a
        now_hash = (str)((hashlib.sha512((str(s).encode('utf-8'))+((form.password.data).encode('utf-8')))).hexdigest())
        #if user and bcrypt.check_password_hash(user.password, form.password.data):
        if (admin and (admin.password==now_hash)):

            login_user(admin, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(url_for('account_admin'))
        else:
            print('halaaa2')
            flash('Login Unsuccessful. Please check email and password', 'danger')
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

    return render_template('home.html', title='Account',current_user=current_user)

@app.route("/accountAdmin", methods= ['POST', 'GET'])
@login_required
def account_admin():

    return render_template('homeAdmin.html', title='Account',current_user=current_user)

@app.route("/carRegistration", methods= ['POST', 'GET'])
@login_required
def car_Registration():
    form = CarRegistration(request.form)
    if form.validate_on_submit():
        car = Car(user_id=current_user.id,car_plate=form.car_plate.data, car_regNumber=form.car_regNumber.data, date=form.date.data, first=form.first.data, middle=form.middle.data, last=form.last.data, state=form.state.data, mobile=form.mobile.data, r_status=0)
        requests=Request(admin_id=1,user_id=current_user.id, r_status=0)
        db.session.add(car)
        db.session.add(requests)
        db.session.commit()
        flash(f'Success! Please fill in the remaining details', 'success')
        return redirect(url_for('account'))
    return render_template('carRegistration.html', title= "Car Registration", form=form, current_user=current_user)


@app.route("/requestsPage", methods=['POST', 'GET'])
@login_required
def admin():
    requests=Request.query.filter_by(r_status=0).all()
    print(requests)
    form=RequestForm(request.form)
    status=list([])
    car=list([])
    for license in requests:
        print(license)
        status.append((license.user_id,license.r_status))
        print(license.user_id)
        user = User.query.filter_by(id=license.user_id).first()
        car = Car.query.filter_by(user_id=user.id).first()
        print(status)
        print(user)
        print(car)
        if form.validate_on_submit():
                if form.invite_status.data=='1':
                    user.r_status=1
                    license.r_status=1
                    car.r_status=1
                    db.session.commit()
                elif  form.invite_status.data=='0':
                    user.r_status=0
                    license.r_status=0
                    car.r_status=0
                    db.session.commit()
    return render_template('requestPage.html', requests=requests, status=status, form=form,car=car)

@app.route("/viewstatus", methods= ['POST', 'GET'])
@login_required
def statusAdmin():
    admin=Admin.query.filter_by(id=current_user.id).first()
    requests=Request.query.all()
    cars=Car.query.all()
    return render_template('viewStatus.html', requests=requests,cars=cars)

@app.route("/viewstatususer", methods= ['POST', 'GET'])
@login_required
def statusUser():
    user=User.query.filter_by(id=current_user.id).first()
    cars=Car.query.filter_by(user_id=user.id).all()
    return render_template('viewStatusUser.html', requests=requests,cars=cars)




