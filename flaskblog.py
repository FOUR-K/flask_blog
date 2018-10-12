from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author':'ramesh ram',
        'title':'blog post 1',
        'content':'first post content',
        'date_posted':'20 april 2018'
    },
    {
        'author':'vishal kumar',
        'title':'blog post 2',
        'content':'second post content',
        'date_posted':'21 april 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='about')

if __name__=="__main__":
    app.run(debug=True)