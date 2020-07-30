import mistune
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html
from pygments import highlight

class HighlightRenderer(mistune.Renderer):
    '''
    Renderer class for mistune.markdown
    this renderer converts the blog code blocks into proper html when it finds code blocks
    so that code hilighting can be done
    css needed for this is in "app/css/code-highliting.css" file
    '''
    def block_code(self, code, lang):
        if not lang:
            return f'\n<pre><code>{mistune.escape(code)}</code></pre>\n'
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)