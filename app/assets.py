import mistune
import re
from app.highlightrenderer import HighlightRenderer

class Post:
    '''
    this class stores the bellow mentioned metadata of blogpost,
    markdown and HTML converted content of blog
    '''
    def __init__(self, title, date, summary, href, md_content=None):
        self.title = title
        self.date = date
        self.summary = summary
        self.href = href
        self.md_content = md_content
        if md_content == None:
            self.html_content = None
        else:
            self.html_content = md_to_html(md_content)

def parse_markdown_post(md_path: str, meta=False) -> Post:
    '''
    :param md_path -> path to markdown file
    :param meta -> set True if you want to retrive only meta data for index page
    :return Object of class Post or None if error occured during parsing
    '''
    try:
        with open(md_path, 'r') as f:
            markdown = f.read()
    except FileNotFoundError:
        return None
    '''
    following regex extracts the metadata fields and the blog content into seperate variables
    '''
    blog_pattern = re.compile(r'title: (?P<title>[^\n]*)\sdate: (?P<date>\d{4}-\d{2}-\d{2})\ssummary: (?P<summary>[^\n]*)')
    match_obj = re.match(blog_pattern, markdown)
    if match_obj is None:
        '''
        if the pattern not found, then return nothing
        '''
        return None
    title = match_obj.group('title')
    date = match_obj.group('date')
    summary = match_obj.group('summary')
    '''
    link for clog is created by replacing whitespaces in the title of blog
    '''
    href = title.lower().replace(' ', '-')
    if meta == False:
        md_content = re.split(blog_pattern, markdown)[-1]
        return Post(title, date, summary, href, md_content=md_content)
    else:
        return Post(title, date, summary, href)

def md_to_html(md_string: str) -> mistune.Markdown:
    '''
    :param md_string -> content of blog extracted from markdown file
    :return input string converted to HTML
    '''
    markdown_formatter = mistune.Markdown(
        renderer= HighlightRenderer(parse_block_html=True)
    )
    return markdown_formatter(md_string)