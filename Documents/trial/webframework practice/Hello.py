from flask import Flask, render_template
"""create an app variable"""
"""instanciation of the Flask variable with name"""
app = Flask(__name__)

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
if __name__ == '__main__':
    app.run(debug=True)