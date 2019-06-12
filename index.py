from flask import Flask, render_template, request,flash, send_from_directory
from flask_wtf import Form
from wtforms import TextField, StringField, validators
import os

app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/')
def form():
   return render_template('form.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      print(result['Name'])
      return render_template("result.html",result = result)

@app.route('/download',methods = ['POST', 'GET'])
def download():
    if request.method == 'POST':
      result = request.form
      file2 = open("doc.txt","w")
      print(str(result["Date"]))
      s1 = "Dear Mr/Ms {} \n\nHope you are well. I have decided to visit you on {} as per you request. This is just a heads-up.\n\nYours truely,\nXXX"
      print(s1.format(result["Name"],result["Date"]))
      print(s1)
      file2.write(s1.format(result["Name"],result["Date"]))
      file2.close()
    try:
        return send_from_directory(os.path.dirname(os.path.abspath(__file__)),'doc.txt',as_attachment=True)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
   app.run(debug = True)

    