from flask import Flask, render_template,request
#import flask_mysqldb
#from flask_mysqldb import MySQL
from similar import similar, similar_papers

import pandas as pd
app = Flask(__name__)


data = pd.read_csv("cite_updated.csv")

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/results',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      keyword = request.form['keyword']
      keyword= keyword.lower()
      index,result,author = similar(keyword)
      return render_template("results.html",keyword = keyword ,result = result, index = index,author = author)

@app.route('/recommend',methods = ['POST', 'GET'])
def recommend():
    index = request.args.get('index')
    title = data.loc[int(index)].title
    recommended,titles,authors = similar_papers(title)
    print(title,recommended)
    return render_template("results.html",keyword = title ,result = titles, index = recommended,author = authors)


if __name__ == "__main__":
    app.run(debug=True)
app.static_folder = 'static'
