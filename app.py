from flask import Flask, render_template, request
from db import load_genes

app = Flask(__name__)

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def convert():
    if request.method == 'POST':
        inp = request.form['text']
        lim = request.form['textlim']
        y = load_genes(inp, lim)
        return render_template('index.html', y=y)

if __name__ == '__main__':
    app.run()