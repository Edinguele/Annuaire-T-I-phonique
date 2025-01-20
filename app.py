from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash

from models import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'votre_clé_secrète_ici'  # Changez ceci en production

# Configuration pour PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ivan@localhost/annuaire'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# Modèle User pour l'authentification


# Modèle Contact pour la gestion des contacts
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    telephone = db.Column(db.String(20), nullable=False)
    poste = db.Column(db.String(100), nullable=False)
    agence = db.Column(db.String(100), nullable=False)
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/dashboard')
def dashboard():
    contacts = Contact.query.order_by(Contact.nom).all()
    return render_template('dashboard.html', contacts=contacts)


@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        telephone = request.form['telephone']
        poste = request.form['poste']
        agence = request.form['agence']

        new_contact = Contact(
            nom=nom,
            prenom=prenom,
            telephone=telephone,
            poste=poste,
            agence=agence
        )

        try:
            db.session.add(new_contact)
            db.session.commit()
            flash('Contact ajouté avec succès')
            return redirect(url_for('dashboard'))
        except:
            db.session.rollback()
            flash('Erreur lors de l\'ajout du contact')
            return redirect(url_for('dashboard'))


@app.route('/edit_contact', methods=['POST'])
def edit_contact():
    if request.method == 'POST':
        contact_id = request.form['id']
        contact = Contact.query.get_or_404(contact_id)

        try:
            contact.nom = request.form['nom']
            contact.prenom = request.form['prenom']
            contact.telephone = request.form['telephone']
            contact.poste = request.form['poste']
            contact.agence = request.form['agence']

            db.session.commit()
            return redirect(url_for('dashboard'))
        except:
            db.session.rollback()
            return redirect(url_for('dashboard'))


@app.route('/delete_contact/<int:id>')
def delete_contact(id):
    contact = Contact.query.get_or_404(id)
    try:
        db.session.delete(contact)
        db.session.commit()
    except:
        db.session.rollback()
    return redirect(url_for('dashboard'))


if __name__ == '__main__':
    app.run(debug=True)