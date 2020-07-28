from flask import Flask, render_template
from app.assets import Post
import os
import datetime
from app.assets import parse_markdown_post

app = Flask(__name__)

@app.route('/')
def index():
    posts = []
    content_path = os.path.join(app.root_path, 'content')

    for file in os.listdir(content_path):
        if not file.endswith('.md'):
            continue
        else:
            full_path = os.path.join(content_path, file)
            posts.append(parse_markdown_post(full_path))
    sorted_posts = sorted(
        posts,
        key=lambda x:datetime.datetime.strptime(x.date, '%Y-%m-%d'),
        reverse=True
    )
    return render_template('index.html', posts=sorted_posts)