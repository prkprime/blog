from flask import Flask, render_template
from app.assets import Post
import os
import datetime
from app.assets import parse_markdown_post

app = Flask(__name__)

@app.route('/blog')
def index():
    posts = []
    content_path = os.path.join(app.root_path, 'content')

    for file in os.listdir(content_path):
        if not file.endswith('.md'):
            continue
        else:
            full_path = os.path.join(content_path, file)
            post = parse_markdown_post(full_path)
            posts.append(post)
            if file != post.title.lower()+'.md':
                new_file = post.title.lower()+'.md'
                os.rename(full_path, os.path.join(content_path, new_file))
    sorted_posts = sorted(
        posts,
        key=lambda x:datetime.datetime.strptime(x.date, '%Y-%m-%d'),
        reverse=True
    )
    return render_template('index.html', posts=sorted_posts)

@app.route('/blog/<post_title>')
def blogpost(post_title):
    md_path = os.path.join(app.root_path, 'content', f'{post_title}.md')
    post = parse_markdown_post(md_path)
    if post == None:
        return render_template('404.html')
    return render_template('blogpost.html', post=post)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')