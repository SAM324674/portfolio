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
    return "contacts"

@app.route('/skills/')
def skills():
    return render_template("skills.html")

@app.route('/education/')
def education():
    return render_template("education.html")

if __name__=='__main__':
    app.run(debug=True)

