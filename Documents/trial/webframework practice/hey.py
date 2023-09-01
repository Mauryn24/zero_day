from flask import Flask, render_template

"""create an instance of the app"""
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

"""define route wioth the strict_slashes=False"""
@app.route('/', strict_slashes=False)
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)
#the posts=posts - the first post is a variable arguement for the posts data

@app.route("/about")
def about():
    return render_template('about.html', title='about')

if __name__ == '__main__':
    app.run(debug=True)