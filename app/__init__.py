from flask import Flask, render_template
from app.post import Post

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')