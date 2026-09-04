from flask import Flask

#instance class-->WSGI
app= Flask(__name__)

#home route
@app.route("/")

def welcome():
  return "Welcome to krish neik Flask course.This course must end before 15 November"

@app.route("/index")
def index():
  return "welcome to index page"

#This is the entry point for the execution of any .py file
if __name__=="__main__":
  app.run(debug= True)
