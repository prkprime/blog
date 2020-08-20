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
            '''
            ignoring non-markdown files
            '''
            continue
        else:
            full_path = os.path.join(content_path, file)
            post = parse_markdown_post(full_path, meta=True)
            if post is None:
                '''
                ignoring markdown files that don't have proper structure
                '''
                continue
            else:
                posts.append(post)
                if file != post.title.lower()+'.md':
                    '''
                    if file name and url created using title aren't the same
                    rename the file
                    this is just a workarround
                    suppose you add a blogfile name "blog1.md" and title of blog is "how to write a blog"
                    then link for that blog is supposed to be "sitename/blog/how-to-write-a-blog"
                    but filename "how-to-write-a-blog.md" doesn't exists in first place.
                    so that's why this if condition renames the file if it's name doesn't match eith title

                    One drawback is filename doesn't updates unless someone accesses the index page after adding blogfile
                    '''
                    new_file = post.title.lower()+'.md'
                    os.rename(full_path, os.path.join(content_path, new_file))
    '''
    sorting posts according to date (newest first)
    '''
    sorted_posts = sorted(
        posts,
        key=lambda x:datetime.datetime.strptime(x.date, '%Y-%m-%d'),
        reverse=True
    )
    return render_template('index.html', posts=sorted_posts)

@app.route('/<post_title>')
def blogpost(post_title):
    md_path = os.path.join(app.root_path, 'content', f'{post_title.replace("-"," ")}.md')
    post = parse_markdown_post(md_path)
    if post is None:
        '''
        hanles the error occuring because of wrong URL i.e. if blog doesn't exists
        '''
        return render_template('404.html')
    return render_template('blogpost.html', post=post)

@app.errorhandler(404)
def page_not_found(e):
    '''
    handles invalid url's
    '''
    return render_template('404.html')