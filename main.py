from flask import Flask,render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = 'your_secret_key' 

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Process the signup form data
        # Add your authentication logic here
        session['username'] = request.form['username']
        return redirect(url_for('home'))
    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        # Process the signin form data
        # Add your authentication logic here
        session['username'] = request.form['username']
        return redirect(url_for('home'))
    return render_template('signin.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))
if __name__ == '__main__':
    app.run(debug=True)