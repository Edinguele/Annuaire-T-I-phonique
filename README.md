# Annuaire-T-I-phonique
#pour la fontion de login
default_username = "Admin"
default_password = "Ftsl"
if request.method == 'POST':
username = request.form['username']
password = request.form['password']
if username == default_username and password == default_password:
return redirect(url_for('dashboard'))
return render_template('login.html')