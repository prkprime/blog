class Post:
    def __init__(self, title, date, summary, href, md_content):
        self.title = title
        self.date = date
        self.summary = summary
        self.href = href
        self.md_content = md_content
        self.html_content = md_to_html(md_content)