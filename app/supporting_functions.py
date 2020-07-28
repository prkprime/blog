import mistune
from app.post import Post
import re
from app.highlightrenderer import HighlightRenderer

def parse_markdown_post(md_path):
    with open(md_path, 'r') as f:
        markdown = f.read().decode('utf-8')
    blog_pattern = re.compile(r'title: (?P<title>[^\n]*)\sdate: (?P<date>\d{4}-\d{2}-\d{2})\ssummary: (?P<summary>[^\n]*)')
    match_obj = re.match(blog_pattern, markdown)
    title = match_obj.group('title')
    date = match_obj.group('date')
    summary = match_obj.group('summary')
    href = '/blog/'+title.lower().replace(' ', '-')
    md_content = re.split(blog_pattern, markdown)[-1]
    return Post(title, date, summary, href, md_content)

def md_to_html(md_string):
    markdown_formatter = mistune.Markdown(
        renderer= HighlightRenderer(parse_block_html=True)
    )
    return markdown_formatter(md_string)