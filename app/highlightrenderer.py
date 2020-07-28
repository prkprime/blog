import mistune
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html
from pygments import highlight

class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        if not lang:
            return f'\n<pre><code>{mistune.escape(code)}</code></pre>\n'
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)