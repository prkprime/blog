# Makdown Blogging Website

This is Markdown Blogging Website created using Python3, Flask and mistune

This website is deployed on heroku [here](https://prk-blogs.herokuapp.com) (It might not be online sometimes so check bellow screenshots instead)

## Table of Contents

- [Screenshots](#screenshots)
- [Project Structure](#project-structure)
- [Steps to run the website](#steps-to-run-the-website)
- [Adding your own blogs](#adding-your-own-blogs)
- [Notes](#notes)

## Screenshots

![Index Page screenshot](https://raw.githubusercontent.com/prkprime/blog/master/app/static/img/index-screenshot.png)

![Blog Page Screenshot](https://raw.githubusercontent.com/prkprime/blog/master/app/static/img/blogpage-screenshot.png)

## Project Structure

```
|-- blog
    |
    |-- app
    |   |
    |   |-- content - stores markdown blogs
    |   |
    |   |-- static - stores static files
    |   |   |-- css - static css files for webpages
    |   |   |-- img - static images used in project
    |   |   |-- js - javascript files (i haven't used any but if you do, store them here)
    |   |
    |   |-- templates - html webpages (Flask app directly picks html file from this directory
    |   |       so you don't have to mention the pathname in code)
    |   |
    |   |-- __init__.py - contains code for creating and seeting flask app
    |   |       View functions for pages like index and blogpost etc.
    |   |       It also makes the app module importable
    |   |
    |   |-- __main__.py - contains code for starting the flask application
    |   |       It also makes the module executable and executes this file when imported
    |   |
    |   |-- assets.py - helping class and functions for parsing markdown and converting to html
    |   |
    |   |-- highlightrenderer.py - custom renderer to parse code blocks in markdown
    |
    |-- requirements.txt - list of python packages used for quick installation
    |
    |-- Procfile - declares the worker type for deploying on Heroku
    |
    |-- README.md - current file you are reading
    |
    |-- LICENSE - Licence of the project (MIT LICENSE in this project)
    |
    |-- .gitignore - list of files/folders to ignore in git
```


## Steps to run the website

1. Clone the repo and go to root directory of project

    ```bash
    git clone https://github.com/prkprime/blog
    cd blog
    ```

2. create the virtual environment using venv and activate it

    ```bash
    python3 -m venv venv/
    source venv/bin/activate
    ```

3. Install all the requirements using pip

    ```bash
    pip3 install -r requirements.txt
    ```

4. Run the website

    1. Using gunicorn

        ```bash
        gunicorn app:app
        ```

    2. Directly as a module

        ```bash
        python3 -m app
        ```

## Adding your own blogs

- All the blogs are stored in app/content folder
- New blog should contain the title, date and summary at the top of the file as shown in bellow sample. It becomes the metadata of sorts for that blog.
- Sample .md file

    ```md
    title: Blog Title
    date: 2020-07-29
    summary: Short description about blog that will appear on index page

    Start your blog here
    ```

- Important things to follow (cause my regex and implementation is weak right now)
    - Maintain the order as title, date and summary
    - Don't add whitespace before ':' and don't forget the whitespace after ':'
    - You can keep filename anything cause code will automatically rename it for you

## Notes

- I created this project only with libraries that I can understand for improving my own skills (well i googled most of the stuff. especially for css stuff cause I ain't frontend guy)
- There are many different ways and many different libraries to create markdown blogging website and there are tons of different implementations available on github which are far more better than mine so if you want to learn, I'll suggest you to check them out
- I have added some samples in app/content for testing purpose so you don't have to write something to test this app