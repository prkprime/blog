def parse_markdown_post(md_path):
    with open(md_path, 'r') as f:
        markdown = f.read().decode('utf-8')
    blog_pattern = re.compile(r'title: (?P<title>[^\n]*)\sdate: (?P<date>\d{4}-\d{2}-\d{2})\ssummary: (?P<summary>[^\n]*)')
    match_obj = re.match(blog_pattern, markdown)
    title = match_obj.group('title')
    date = match_obj.group('date')
    summary = match_obj.group('summary')
    href = '/blog/'+title.lower().replace(' ', '-')
    md_content = re.split(re_pat, markdown)[-1]
    return Post(title, date, summary, href, md_content)

