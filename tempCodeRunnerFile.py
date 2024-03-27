from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def home():
    return render_template("nav.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/contact/')
def contact():
    return "contact"

@app.route('/skills/')
def skills():
    return "skills"

@app.route('/education/')
def education():
    return "education"

if __name__=='__main__':
    app.run(debug=True)