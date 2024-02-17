import re

def bold_tag(s):
    text = s[2:-2]

    return f'<b>{text}</b>'

def italic_tag(s):
    text = s[1:-1]

    return f'<i>{text}</i>'

def bold_italic_tag(s):
    text = s[3:-3]

    return f'<b><i>{text}</i></b>'

def header_one_tag(s):
    text = s.replace('#', '')

    return f'<h1>{text}</h1>'

def header_two_tag(s):
    text = s.replace('##', '')

    return f'<h2>{text}</h2>'

def header_three_tag(s):
    text = s.replace('###', '')

    return f'<h3>{text}</h3>'

def header_four_tag(s):
    text = s.replace('####', '')

    return f'<h4>{text}</h4>'

def header_five_tag(s):
    text = s.replace('#####', '')

    return f'<h5>{text}</h5>'

def header_six_tag(s):
    text = s.replace('######', '')

    return f'<h6>{text}</h6>'

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

    return f'<img src="{link}" alt="{text}"/>'

def paragraph_tag(s):
    return f'<p>{s}</p>'

def ul_tag(s):
    return f'<ul>{s}</ul>'

def ol_tag(s):
    return f'<ol>{s}</ol>'

def li_tag(s):
    return f'<li>{s.replace("-", "")}</li>'

def horizontal_ruler_tag(s):
    return f'<hr>'

def code_tag(s):
    return f'<code>{s}</code>'

def blockquote_tag(s):
    return f'<blockquote>{s}</blockquote>'
