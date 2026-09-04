# Building url dynamically
# Variable rule
# Jinja 2 templete engine

from flask import Flask,render_template,request,redirect, url_for

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

#Submit route
@app.route("/submit1", methods=['GET','POST'])
def submit1():
  if request.method=='POST':
    name = request.form['name']
    return f"Hello Mr./Mrs. {name}"
  return render_template('form.html')

#Variable name
@app.route("/success/<int:score>")
def success(score):
  res=""
  if score >=50:
    res="PASS"
  else:
    res="FAIL"

  return render_template('result.html', result = res)

#Variable name
@app.route("/successres/<int:score>")
def successres(score):
  res=""
  if score >=50:
    res="PASS"
  else:
    res="FAIL"

  exp= {'score':score, 'res':res}
  return render_template('result1.html', result = exp)

# if condition
@app.route("/successif/<int:score>")
def successif(score):
  return render_template('result.html', result = score)

#Variable name
@app.route("/fail/<int:score>")
def fail(score):
  return render_template('result.html', result = score)

#submit route
@app.route("/submit", methods=['GET','POST'])
def submit():
  total_score=0
  if request.method=='POST':
    science= float(request.form['science'])
    maths= float(request.form['maths'])
    c= float(request.form['c'])
    data_science= float(request.form['datascience'])

    total_score=(science + maths + c + data_science)/4
  else:
    return render_template('getresult.html')

  return redirect(url_for('successres', score= total_score))


#Starting point(Main function in java ki trh samjh lo)
if __name__=="__main__":
  app.run(debug=True)