from flask import Flask, render_template 
#render template accesses an html file stored in the application files and displays that html for the requested URL

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)
