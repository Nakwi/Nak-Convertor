import re

def html_to_markdown(text):
    text = re.sub(r'<h1>(.*?)</h1>', r'# \1', text)
    text = re.sub(r'<h2>(.*?)</h2>', r'## \1', text)
    text = re.sub(r'<strong>(.*?)</strong>', r'**\1**', text)
    text = re.sub(r'<em>(.*?)</em>', r'*\1*', text)
    text = re.sub(r'<a href="(.*?)">(.*?)</a>', r'[\2](\1)', text)
    text = re.sub(r'<li>(.*?)</li>', r'- \1', text)
    return text
