import re

def markdown_to_html(text):
    text = re.sub(r'###### (.*)', r'<h6>\1</h6>', text)
    text = re.sub(r'##### (.*)', r'<h5>\1</h5>', text)
    text = re.sub(r'#### (.*)', r'<h4>\1</h4>', text)
    text = re.sub(r'### (.*)', r'<h3>\1</h3>', text)
    text = re.sub(r'## (.*)', r'<h2>\1</h2>', text)
    text = re.sub(r'# (.*)', r'<h1>\1</h1>', text)

    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'__(.*?)__', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    text = re.sub(r'_(.*?)_', r'<em>\1</em>', text)

    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', text)

    lines = text.split('\n')
    html_lines = []
    for line in lines:
        if re.match(r'^[-*+] ', line):
            html_lines.append('<li>' + line[2:] + '</li>')
        else:
            html_lines.append(line)
    return '\n'.join(html_lines)
