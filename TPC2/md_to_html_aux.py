def bold_tag(s):
    text = s.replace('**', '')
    text = text.replace('__', '')

    return f'<b>{text.strip()}</b>'

def italic_tag(s):
    text = s.replace('*', '')
    text = text.replace('_', '')

    return f'<i>{text.strip()}</i>'

def header_one_tag(s):
    text = s.replace('#', '')

    return f'<h1>{text.strip()}</h1>'

def header_two_tag(s):
    text = s.replace('##', '')

    return f'<h2>{text.strip()}</h2>'

def header_three_tag(s):
    text = s.replace('###', '')

    return f'<h3>{text.strip()}</h3>'

def anchor_tag(s):
    text_idx1 = s.index('[')
    text_idx2 = s.index(']')
    text = s[text_idx1 + 1 : text_idx2]

    link_idx1 = s.index('(')
    link_idx2 = s.index(')')
    link = s[link_idx1 + 1 : link_idx2]

    return f'<a href="{link}">{text.strip()}</a>'

def image_tag(s):
    text_idx1 = s.index('[')
    text_idx2 = s.index(']')
    text = s[text_idx1 + 1 : text_idx2]

    link_idx1 = s.index('(')
    link_idx2 = s.index(')')
    link = s[link_idx1 + 1 : link_idx2]

    return f'<img src="{link}" alt="{text.strip()}"/>'

def paragraph_tag(s):
    return f'<p>{s}</p>'

def ul_tag(s):
    return f'<ul>{s}</ul>'

def li_tag(s):
    return f'<li>{s.replace("-", "").strip()}</li>'