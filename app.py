from flask import Flask, redirect,render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/winpa/OneDrive/Desktop/Web development assignment/text.db'
db = SQLAlchemy(app)

class Sign_in(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(40))
    Email = db.Column(db.String(80))
    Password = db.Column(db.String(80))
    def __repr__(self):
        return '<Sign_in %r>' % self.id
    
class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)

    def __repr__(self):
        return '<Donation %r>' % self.id
        

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        Name = request.form.get("Name")
        Email = request.form.get("Email")
        Password = request.form.get("Password")
       
        new_user = Sign_in( Name=Name, Email=Email, Password=Password)
        
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template('register.html')

@app.route('/signin', methods =["GET", "POST"]) 
def signin():
    if request.method == "POST":
        Name = request.form.get("Name")
        Password = request.form.get("Password") 
        user = Sign_in.query.filter_by(Name = Name).first()
        
        if user and user.Password == Password:
            return redirect(url_for('welcome'))
        else:
           return redirect(url_for('advice'))
    return render_template('signin.html')

@app.route('/donate', methods=["POST"])
def donate():
    if request.method == "POST":
        amount = float(request.form.get("amount"))
        new_donation = Donation(amount=amount)
        db.session.add(new_donation)
        db.session.commit()
        return redirect(url_for('thanks'))
    return render_template('donate.html')


@app.route('/')
def home():
    return render_template('base.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/community')
def community():
    return render_template('community.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/advice')
def advice():
    return render_template('advice.html')

if __name__ == '__main__':
    app.run(debug=True)
    