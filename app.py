from flask import Flask, render_template, request
from datetime import datetime
from model import personal_meme


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', time=datetime.now())

@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        print(request.form["mood"])
        mood_value=int((request.form["mood"]))
        user_meme=personal_meme(mood_value) 
        return render_template('results.html', mood_value=mood_value, user_meme=user_meme)
    else:
        return render_template('index.html', time=datetime.now())
