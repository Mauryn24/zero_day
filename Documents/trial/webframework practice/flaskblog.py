from flask import Flask, render_template, url_for, flash, redirect
from forms import Registrationform, LoginForm
"""create an app variable"""
"""instanciation of the Flask variable with name"""
app = Flask(__name__)
app.config['SECRET_KEY'] = '93a95925c10682bd3f26dad5b2a0f554c7712353b9cdd7a9b3e87f6e0d4e2612'

posts = [
    {
        'author': 'Corey Schofer',
        'title': 'Blog Post1',
        'content': 'first post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post2',
        'content': 'second post content',
        'date_posted': 'April 21, 2018'
    }
]
"""route - what we type into our browser to go to different pages"""
@app.route ("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

"""a route to return an about"""
@app.route("/about")
def about():
    return render_template('about.html', title='About')
"""Running on http://127.0.0.1:5000 - 127.0.0 ip address of my local machine  5000 - port number"""
# export FLASK_DEBUG=1

@app.route('/register', methods=['GET', 'POST'])
def register():
    #create an instance of the form
    form = Registrationform()
    if form.validate_on_submit():
        flash(f'account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='register', form=form)

@app.route('/login')
def login():
    #create an instance of the form
    form = LoginForm()
    return render_template('login.html', title='login', form=form)

if __name__ == '__main__':
    app.run(debug=True)