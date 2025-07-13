from flask import Flask,request,render_template,redirect,url_for
app = Flask(__name__)
@app.route("/")
def home():
    return "welcome to the home page...."
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username=="Ruchika_Mam" and password=="ruchiRoman100%":
            return redirect(url_for('dashboard'))
        else:
            return render_template("login.html",error="invalid cradentials!")
    return render_template("login.html")
@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')
if __name__=="__main__":
    app.run(debug=True)

