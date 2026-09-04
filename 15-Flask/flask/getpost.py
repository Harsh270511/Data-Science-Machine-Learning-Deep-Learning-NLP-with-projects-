from flask import Flask,render_template,request

app=Flask(__name__)

#Home route
@app.route("/")
def Welcome():
  return "<html ><h1 >Welcome to Harsh Web Application</h1> </html>"

#Index route
@app.route("/index",methods=['GET'])
def index():
  return render_template("index.html")

#About route
@app.route("/about")
def about():
  return render_template("about.html")

#Form route
@app.route("/form", methods=['GET','POST'])
def form():
  if request.method=='POST':
    name = request.form['name']
    return f"Hello Mr./Mrs. {name}"
  return render_template('form.html')

#Submit route
@app.route("/submit", methods=['GET','POST'])
def submit():
  if request.method=='POST':
    name = request.form['name']
    return f"Hello Mr./Mrs. {name}"
  return render_template('form.html')


#Starting point(Main function in java ki trh samjh lo)
if __name__=="__main__":
  app.run(debug=True)