from flask import Flask, render_template, request, logging, Response, redirect, flash
from similarity import generate_similarity

app = Flask(__name__)

@app.route('/', methods = ["GET" , "POST"])
def index():
   if request.method == 'POST':
       line_input = request.form['line_input'] 

       line_output = [generate_similarity(line_input).to_html(classes="data", header="table")]

       return render_template('app_page.html', line_input = line_input, line_output = line_output)
   else:
       return render_template('app_page.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)