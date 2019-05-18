#!/usr/bin/env python3

import os
import requests  # to use args.get function
from functools import wraps
from flask import Flask, flash, redirect, render_template, request
from flask import session as login_session  # dictionary store values in it
from flask import url_for
# import all modules needed for sqlalchemy configuration
from sqlalchemy import asc, create_engine, or_
from sqlalchemy.orm import sessionmaker

from database_setup import (Admin, Base, Departments, Downloads,
                            Facaulties, Students)

# initializes an app variable, using the __name__ attribute
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get(
    'SECRET_KEY', 'this_should_be_configured')

# Connect to Database and create database session
engine = create_engine('sqlite:///collegedemo.db',
                       connect_args={'check_same_thread': False}, echo=True)
Base.metadata.bind = engine


# create session maker object
DBSession = sessionmaker(bind=engine)
session = DBSession()


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'role' not in login_session:
            flash('you can not authorized')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


def check_role(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'role' in login_session:
            if login_session['role'] != 'Admin':
                flash('you can not authorized')
                return redirect(url_for('home'))
        return f(*args, **kwargs)
    return decorated_function


def check_role1(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'role' in login_session:
            if login_session['role'] != 'Student':
                flash('you can not authorized')
                return redirect(url_for('home'))
        return f(*args, **kwargs)
    return decorated_function


# open first page
# open default page
@app.route('/')
@app.route('/home/')
def home():
    downloads = session.query(Downloads).all()
    return render_template('main.html', downloads=downloads)


# open about page
@app.route('/about/')
def about():
    return render_template('about.html')


# open academics page
@app.route('/academics/')
def academics():
    departments = session.query(Departments).all()
    facaulties = session.query(Facaulties).all()
    return render_template('academics.html',
                           departments=departments, facaulties=facaulties)


# open map with gmap api
@app.route('/gmap/')
def gmap():
    return render_template('gmap.html')


# create facaulty via admin
@app.route('/admin/facaulty/new', methods=['GET', 'POST'])
@login_required
@check_role
def ad_fc_add():
    if login_session['role'] != 'Admin':
        flash('you can not authorized')
        return redirect('/home')
    departments = session.query(Departments).all()
    if request.method == 'POST':
        newfacaulty = Facaulties(fac_name=request.form['name'],
                                 admin_id=login_session['id'],
                                 email=request.form['email'],
                                 password=request.form['password'],
                                 picture=request.form['picture'],
                                 ac_rank=request.form['position'],
                                 edu=request.form['edu'],
                                 dept_id=request.form.get('dept')
                                 )
        session.add(newfacaulty)
        session.commit()
        flash(f"new facaulty {request.form['name']} created!")
        return redirect(url_for('admin_fac'))
    else:
        return render_template('admin/newaddfacaulty.html',
                               departments=departments)


# edit facaulty data via admin
@app.route('/admin/facaulty/<int:fac_id>/edit', methods=['GET', 'POST'])
@login_required
@check_role
def ad_fc_edit(fac_id):
    departments = session.query(Departments).all()
    editedfacaulty = session.query(Facaulties).filter_by(id=fac_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedfacaulty.fac_name = request.form['name']
        if request.form['email']:
            editedfacaulty.email = request.form['email']
        if request.form['password']:
            editedfacaulty.password = request.form['password']
        if request.form['picture']:
            editedfacaulty.picture = request.form['picture']
        if request.form['position']:
            editedfacaulty.ac_rank = request.form['position']
        if request.form['edu']:
            editedfacaulty.edu = request.form['edu']
        if login_session['id']:
            editedfacaulty.admin_id = login_session['id']
        if request.form['dept']:
            editedfacaulty.dept_id = request.form['dept']
        session.add(editedfacaulty)
        session.commit()
        flash(f"Facaulty {request.form['name']} has been updated")
        return redirect(url_for('admin_fac'))
    else:
        return render_template('admin/editadminfacaulty.html',
                               departments=departments,
                               facaulties=editedfacaulty)


# delete facaulty data via admin
@app.route('/admin/facaulty/<int:fac_id>/delete', methods=['GET', 'POST'])
@login_required
@check_role
def ad_fc_delete(fac_id):
    facaultyToDelete = session.query(Facaulties).filter_by(id=fac_id).one()
    if request.method == 'POST':
        session.delete(facaultyToDelete)
        session.commit()
        flash("Facaulty has been deleted")
        return redirect(url_for('admin_fac'))
    else:
        return render_template('admin/deleteadfacaulty.html',
                               facaulty=facaultyToDelete)


# new student data via admin
@app.route('/admin/student/add', methods=['GET', 'POST'])
@login_required
@check_role
def ad_st_add():
    departments = session.query(Departments).all()
    if request.method == 'POST':
        newstudent = Students(st_name=request.form['name'],
                              admin_id=login_session['id'],
                              roll_no=request.form['roll_no'],
                              picture=request.form['picture'],
                              mob_no=request.form['mob_no'],
                              dept_id=request.form.get('dept')
                              )
        session.add(newstudent)
        session.commit()
        flash(f"new student {request.form['name']} created!")
        return redirect(url_for('admin_st'))
    else:
        return render_template('admin/newaddstudent.html',
                               departments=departments)


# update student data via admin
@app.route('/admin/student/<int:st_id>/edit', methods=['GET', 'POST'])
@login_required
@check_role
def ad_st_edit(st_id):
    departments = session.query(Departments).all()
    editedstudent = session.query(Students).filter_by(id=st_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedstudent.st_name = request.form['name']
        if request.form['roll_no']:
            editedstudent.roll_no = request.form['roll_no']
        if request.form['picture']:
            editedstudent.picture = request.form['picture']
        if request.form['mob_no']:
            editedstudent.mob_no = request.form['mob_no']
        if login_session['id']:
            editedstudent.admin_id = login_session['id']
        if request.form['dept']:
            editedstudent.dept_id = request.form['dept']
        session.add(editedstudent)
        session.commit()
        flash(f"Student {request.form['name']} has been updated")
        return redirect(url_for('admin_st'))
    else:
        return render_template('admin/editadstudent.html',
                               departments=departments,
                               student=editedstudent)


# delete student data via admin
@app.route('/admin/student/<int:st_id>/delete', methods=['GET', 'POST'])
@login_required
@check_role
def ad_st_delete(st_id):
    studentToDelete = session.query(Students).filter_by(id=st_id).one()
    if request.method == 'POST':
        session.delete(studentToDelete)
        session.commit()
        flash("Student has been deleted")
        return redirect(url_for('admin_st'))
    else:
        return render_template('admin/deleteadstudent.html',
                               student=studentToDelete)


# add files via admin
@app.route('/admin/download/add', methods=['GET', 'POST'])
@login_required
@check_role
def ad_dw_add():
    if request.method == 'POST':
        newdownload = Downloads(file_name=request.form['file_name'],
                                admin_id=login_session['id'],
                                file_path=request.form['file_path']
                                )
        session.add(newdownload)
        session.commit()
        flash(f"new download{request.form['file_name']} created!")
        return redirect(url_for('admin_dw'))
    else:
        return render_template('admin/newadddownload.html')


# delete files via admin
@app.route('/admin/download/<int:dw_id>/delete', methods=['GET', 'POST'])
@login_required
@check_role
def ad_dw_delete(dw_id):
    downloadToDelete = session.query(Downloads).filter_by(id=dw_id).one()
    if request.method == 'POST':
        session.delete(downloadToDelete)
        session.commit()
        flash("File has been deleted")
        return redirect(url_for('admin_dw'))
    else:
        return render_template('admin/deleteaddownloads.html',
                               download=downloadToDelete)


# admin files page
@app.route('/admin/downloads')
@login_required
@check_role
def admin_dw():
    downloads = session.query(Downloads).all()
    return render_template('admin/admindownload.html', downloads=downloads)


# admin students page
@app.route('/admin/students')
@login_required
@check_role
def admin_st():
    departments = session.query(Departments).all()
    students = session.query(Students).all()
    return render_template('admin/adminstudent.html',
                           students=students,
                           departments=departments)


# admin facaulty page
@app.route('/admin/facaulty')
@login_required
@check_role
def admin_fac():
    departments = session.query(Departments).all()
    facaulties = session.query(Facaulties).all()
    return render_template('admin/adminfacaulty.html',
                           facaulties=facaulties,
                           departments=departments)


# admin default page
@app.route('/admin/home')
@login_required
@check_role
def admin_home():
    return render_template('admin/adminpage.html')


# student default page
@app.route('/student/home')
@login_required
@check_role1
def student_home():
    return render_template('students/studentpage.html')


# login page
@app.route('/login/')
def login():
    if 'role' in login_session:
        if login_session['role'] == 'Admin':
            flash(f'you already authorized as {login_session["role"]}')
            return redirect(url_for('admin_home'))
        elif login_session['role'] == 'Student':
            flash(f'you already authorized as {login_session["role"]}')
            return redirect(url_for('student_home'))
    else:
        return render_template('login.html')


# student login
@app.route('/student/login', methods=["GET", "POST"])
def st_login():
    if request.method == 'POST':
        role = request.form['role']
        roll_no = request.form['roll_no']
        mob_no = request.form['mob_no']
        st_query = session.query(Students).filter_by(
            roll_no=roll_no, mob_no=mob_no).first()
        if st_query is None:
            flash('Roll Number or/and mobile no is invalid', 'error')
            return redirect(url_for('login'))
        else:
            login_session['st_name'] = st_query.st_name
            login_session['id'] = st_query.id
            login_session['role'] = role
            flash('Logged in successfully')
            return redirect(url_for('student_home'))
    else:
        return redirect(url_for('login'))


# Admin login
@app.route('/admin/login', methods=["GET", "POST"])
def ad_login():
    if request.method == 'POST':
        role = request.form['role']
        email = request.form['email']
        password = request.form['password']
        admin_query = session.query(Admin).filter_by(
            email=email, password=password).first()
        if admin_query is None:
            flash('Username or Password is invalid', 'error')
            return redirect(url_for('login'))
        else:
            # store data in session for letter use
            login_session['role'] = role
            login_session['id'] = admin_query.id
            login_session['ad_name'] = admin_query.name
            flash('Logged in successfully')
            return redirect(url_for('admin_home'))
    else:
        return redirect(url_for('login'))


# logout
@app.route('/logout')
def logout():
    if 'role' in login_session:
        if login_session['role'] == 'Admin':
            del login_session['role']
            del login_session['ad_name']
            del login_session['id']
        else:
            del login_session['st_name']
            del login_session['role']
            del login_session['id']
        flash('successfully Logout')
        return redirect(url_for('login'))
    else:
        flash('You are already logout')
        return redirect(url_for('login'))


# This only happens when application.py is called directly:
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
