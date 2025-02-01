from flask import Flask, render_template,redirect,url_for,request,flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,login_manager,LoginManager
from flask_login import login_required,current_user
from datetime import datetime
from sqlalchemy import text
import logging
# db connection
local_server = True

app = Flask(__name__, template_folder='templates')


login_manager = LoginManager(app)
login_manager.login_view='login'
app.secret_key = 'sani#9876'
@login_manager.user_loader
def load_user(id):
    return Login.query.get(int(id))
# Correct the configuration name to SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sanika:adinpass@localhost:3306/pet'

db = SQLAlchemy(app)




class Login(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    empid=db.Column(db.String(50))
    password=db.Column(db.String(1000))



# creating db model (db tables)
class Pet(db.Model):
    pet_id = db.Column(db.Integer, primary_key=True)
    breed = db.Column(db.String(50))
    age = db.Column(db.Integer)  # Corrected from db.Int(2)
    species = db.Column(db.String(50))
    u_id = db.Column(db.String(50))

class Health_record(db.Model):
    record_id=db.Column(db.Integer,primary_key=True)
    pet_id=db.Column(db.Integer)
    vaccination=db.Column(db.String(100))
    medication=db.Column(db.String(100))
    medical_history=db.Column(db.String(100))


class Nutrition_and_diet(db.Model):
    nutrition_diet_id=db.Column(db.Integer,primary_key=True)
    pet_id=db.Column(db.Integer)
    diet_plan=db.Column(db.String(100))
    requirements=db.Column(db.String(100))



class Emergency_contact(db.Model):
    contact_id=db.Column(db.Integer,primary_key=True)
    pet_relation=db.Column(db.String(50))
    name=db.Column(db.String(50))
    pet_id=db.Column(db.Integer)
    phone=db.Column(db.String(10))



class Appointment(db.Model):
    ap_id=db.Column(db.Integer,primary_key=True)
    pet_id=db.Column(db.Integer)
    date=db.Column(db.Date)
    purpose=db.Column(db.String(100))
    notes=db.Column(db.String(100))











@app.route('/')
  
def index():
    return render_template('index.html')
@app.route('/home')    

#appointmnet
@app.route('/appointment',methods=['POST','GET'])
@login_required 
def appointment():
    if request.method =="POST":
        # pet_id=request.form.get('pet_id')
        pet_id=request.form.get('pet_id')
        date=request.form.get('date')
        purpose=request.form.get('purpose')
        notes=request.form.get('notes')

        query = text(
            f"INSERT INTO appointment (pet_id, date, purpose, notes) VALUES ('{pet_id}', '{date}', '{purpose}', '{notes}');"
        )
        db.session.execute(query)
        db.session.commit()

        flash("appointment details added","success")
        return redirect(url_for('viewappointment'))
    return render_template('appointment.html')

#nutrition
@app.route('/nutrition',methods=['POST','GET'])   
@login_required 
def nutrition():
    if request.method =="POST":
        # pet_id=request.form.get('pet_id')
        pet_id=request.form.get('pet_id')
        diet_plan=request.form.get('diet_plan')
        requirements=request.form.get('requirements')
      

        query = text(
            f"INSERT INTO Nutrition_and_diet (pet_id, diet_plan, requirements) VALUES ('{pet_id}', '{diet_plan}', '{requirements}');"
        )
        db.session.execute(query)
        db.session.commit()

        flash("health record details added","success")
        return redirect(url_for('viewnutrition'))

    return render_template('nutrition.html')


#healthrecord
@app.route('/healthrecord',methods=['POST','GET'])
@login_required 
def healthrecord():
    if request.method =="POST":
        # pet_id=request.form.get('pet_id')
        pet_id=request.form.get('pet_id')
        vaccination=request.form.get('vaccination')
        medication=request.form.get('medication')
        medical_history=request.form.get('medical_history')

        query = text(
            f"INSERT INTO health_record (pet_id, vaccination, medication,medical_history) VALUES ('{pet_id}', '{vaccination}', '{medication}', '{medical_history}');"
        )
        db.session.execute(query)
        db.session.commit()

        flash("health record details added","success")
        return redirect(url_for('viewhealthrecord'))
    return render_template('healthrecord.html')


#contact
@app.route('/contact',methods=['POST','GET'])
@login_required 
def contact():
    if request.method =="POST":
        # pet_id=request.form.get('pet_id')
        pet_relation=request.form.get('pet_relation')
        name=request.form.get('name')
        pet_id=request.form.get('pet_id')
        phone=request.form.get('phone')

        query = text(
            f"INSERT INTO emergency_contact (pet_relation, name, pet_id, phone) VALUES ('{pet_relation}', '{name}', '{pet_id}', '{phone}');"
        )

        # Use db.engine.execute to execute the textual SQL expression
        db.session.execute(query)
        db.session.commit()

        flash("contact details added","success")
        return redirect(url_for('viewcontact'))

    return render_template('contact.html')


#pet register
@app.route('/pet_register',methods=['POST','GET'])
def register():
    if request.method =="POST":
        # pet_id=request.form.get('pet_id')
        breed=request.form.get('breed')
        age=request.form.get('age')
        species=request.form.get('species')
        u_id=request.form.get('u_id')

        query = text(
            f"INSERT INTO pet (breed, age, species, u_id) VALUES ('{breed}', '{age}', '{species}', '{u_id}');"
        )

        # Use db.engine.execute to execute the textual SQL expression
        db.session.execute(query)
        db.session.commit()
        flash("Pet details added","success")
        return redirect(url_for('index'))
    return render_template('register.html')

#view pet


@app.route('/view_pet', methods=['GET'])
def view():
    query = text("SELECT * FROM pet;")
    query_result = db.session.execute(query)

    # Fetch all rows from the query result
    pet_data = query_result.fetchall()

    # No need to commit when reading data
    # db.session.commit()
    
    # Use Flask's logger instead of print
    app.logger.info(pet_data)

    return render_template('view.html', pet_data=pet_data)


#view appointment
@app.route('/view_appointment',methods=['GET'])
def viewappointment():
    query = text("SELECT * FROM appointment;")
    query_result = db.session.execute(query)

    # Fetch all rows from the query result
    appointment= query_result.fetchall()

    # No need to commit when reading data
    # db.session.commit()
   
    return render_template('view_appointment.html', appointment=appointment)

#view contact
@app.route('/view_contact',methods=['GET'])
def viewcontact():
    query = text("SELECT * FROM emergency_contact;")
    query_result = db.session.execute(query)

    # Fetch all rows from the query result
    contact= query_result.fetchall()

    # No need to commit when reading data
    # db.session.commit()
   
    return render_template('view_contact.html', contact=contact)

#view helath_record
@app.route('/view_healthrecord',methods=['GET'])
def viewhealthrecord():
    query = text("SELECT * FROM Health_record;")
    query_result = db.session.execute(query)

    # Fetch all rows from the query result
    health= query_result.fetchall()

    # No need to commit when reading data
    # db.session.commit()
   
    return render_template('view_healthrecord.html', health=health)


#view nutrition
@app.route('/view_nutrition',methods=['GET'])
def viewnutrition():
    query = text("SELECT * FROM Nutrition_and_diet;")
    query_result = db.session.execute(query)

    # Fetch all rows from the query result
    nutrition= query_result.fetchall()

    # No need to commit when reading data
    # db.session.commit()
   
    return render_template('view_nutrition.html', nutrition=nutrition)



#login
@app.route('/login', methods=['POST','GET'])
def login():
    if request.method =="POST":
        empid=request.form.get('empid')
        password=request.form.get('password')
        if(len(password)<8 or len(password)>25):
            flash("Password must be atleast 8 characters long","danger")
            return render_template('login.html')
        login=Login.query.filter_by(empid=empid,password=password).first()
        if login:
            login_user(login)
            flash("Login successful","success")
            return redirect(url_for('index'))
        else:
            flash("invalid credentials","danger")
            return render_template('login.html')
    
    return render_template('login.html')




#logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

#edit pet
@app.route("/edit/pet/<string:pet_id>", methods=['POST', 'GET'])
@login_required
def epet(pet_id):
    post = Pet.query.filter_by(pet_id=pet_id).first()
    
    if request.method == "POST":
        pet_id=request.form.get('pet_id')
        breed = request.form.get('breed')
        age = request.form.get('age')
        species = request.form.get('species')
        u_id = request.form.get('u_id')
        app.logger.info(f"Received form data: breed={breed}, age={age}, species={species}, u_id={u_id}")


        query = text(
            f"UPDATE  pet set breed='{breed}',age={age},u_id='{u_id}',species='{species}' where pet_id={pet_id};"
        )
        db.session.execute(query)
        db.session.commit()
        flash("Updated", "success")
        return redirect('/view_pet')
    
    app.logger.info(post)
    return render_template('edit_pet.html', post=post)

#edit appointment
@app.route("/edit/appointment/<string:ap_id>", methods=['POST', 'GET'])
@login_required
def editap(ap_id):
    
    post = Appointment.query.filter_by(ap_id=ap_id).first()
    if request.method == "POST":
        
        ap_id=request.form.get('ap_id')
        pet_id = request.form.get('pet_id')
        date = request.form.get('date')
        purpose = request.form.get('purpose')
        notes = request.form.get('notes')
        # print(f"Received form data: pet_id={pet_id}, date={date}, purpose={purpose}, notes={notes}")

        query = text(
            f"UPDATE  appointment set pet_id='{pet_id}',date='{date}',purpose='{purpose}',notes='{notes}' where ap_id='{ap_id}';"
        )

        db.session.execute(query)
        db.session.commit()
        flash("Updated", "success")
        return redirect('/view_appointment')
    
    return render_template('edit_appointment.html', post=post)

#edit contact
@app.route("/edit/contact/<string:contact_id>", methods=['POST', 'GET'])
@login_required
def editco(contact_id):
    
    post = Emergency_contact.query.filter_by(contact_id=contact_id).first()
    if request.method == "POST":
        
        contact_id_id=request.form.get('contact_id')
        pet_relation = request.form.get('pet_relation')
        pet_id = request.form.get('pet_id')
        phone = request.form.get('phone')
        
        # print(f"Received form data: pet_id={pet_id}, date={date}, purpose={purpose}, notes={notes}")

        query = text(
            f"UPDATE  Emergency_contact set pet_relation='{pet_relation}',pet_id='{pet_id}',phone='{phone}' where   contact_id='{contact_id}';"
        )

        db.session.execute(query)
        db.session.commit()
        flash("Updated", "success")
        return redirect('/view_contact')
    
    return render_template('edit_contact.html', post=post)

#edit healthrecord
@app.route("/edit/health/<string:record_id>", methods=['POST', 'GET'])
@login_required
def edithealth(record_id):
    
    post = Health_record.query.filter_by(record_id=record_id).first()
    if request.method == "POST":
        
        record_id=request.form.get('record_id')
        pet_id = request.form.get('pet_id')
        vaccination = request.form.get('vaccination')
        medication = request.form.get('medication')
        medical_history = request.form.get('medical_history')
        
        
        # print(f"Received form data: pet_id={pet_id}, date={date}, purpose={purpose}, notes={notes}")

        query = text(
            f"UPDATE  Health_record set pet_id='{pet_id}',vaccination='{vaccination}',medication='{medication}',medical_history='{medical_history}' where   record_id='{record_id}';"
        )

        db.session.execute(query)
        db.session.commit()
        flash("Updated", "success")
        return redirect('/view_healthrecord')
    
    return render_template('edit_healthrecord.html', post=post)

#edit nutrition
@app.route("/edit/nutrition/<string:nutrition_diet_id>", methods=['POST', 'GET'])
@login_required
def editnu(nutrition_diet_id):
    
    post = Nutrition_and_diet.query.filter_by(nutrition_diet_id=nutrition_diet_id).first()
    if request.method == "POST":
        
        pet_id=request.form.get('pet_id')
        diet_plan = request.form.get('diet_plan')
        requirements = request.form.get('requirements')
  
        
        # print(f"Received form data: pet_id={pet_id}, date={date}, purpose={purpose}, notes={notes}")

        query = text(
            f"UPDATE  Nutrition_and_diet set pet_id='{pet_id}',diet_plan='{diet_plan}',requirements='{requirements}' where   nutrition_diet_id='{nutrition_diet_id}';"
        )
 
        db.session.execute(query)
        db.session.commit()
        flash("Updated", "success")
        return redirect('/view_nutrition')
    
    return render_template('edit_nutrition.html', post=post)

#delete pet
@app.route("/delete/pet/<string:pet_id>", methods=['POST','GET'])
@login_required
def dellp(pet_id):
    query=text(f"DELETE FROM pet WHERE pet_id={pet_id};")
    db.session.execute(query)
    db.session.commit()
    flash("Deleted","danger")
    return redirect('/view_pet')


#delete appointment
@app.route("/delete/appointment/<string:ap_id>", methods=['POST','GET'])
@login_required
def dellap(ap_id):
    query=text(f"DELETE FROM appointment WHERE ap_id={ap_id};")

    
    db.session.execute(query)
    db.session.commit()
    flash("Deleted","danger")
    return redirect('/view_appointment')

#delete appointment
@app.route("/delete/contact/<string:contact_id>", methods=['POST','GET'])
@login_required
def dellco(contact_id):
    query=text(f"DELETE FROM Emergency_contact WHERE contact_id={contact_id};")

    
    db.session.execute(query)
    db.session.commit()
    flash("Deleted","danger")
    return redirect('/view_contact')

#delete health_record
@app.route("/delete/health/<string:record_id>", methods=['POST','GET'])
@login_required
def dellhl(record_id):
    query=text(f"DELETE FROM Health_record WHERE record_id={record_id};")

    
    db.session.execute(query)
    db.session.commit()
    flash("Deleted","danger")
    return redirect('/view_healthrecord')

#delete nutrition
@app.route("/delete/nutrition/<string:nutrition_diet_id>", methods=['POST','GET'])
@login_required
def dellnu(nutrition_diet_id):
    query=text(f"DELETE FROM Nutrition_and_diet WHERE nutrition_diet_id={nutrition_diet_id};")

    
    db.session.execute(query)
    db.session.commit()
    flash("Deleted","danger")
    return redirect('/view_nutrition')

if __name__ == '__main__':
    app.run(debug=True)