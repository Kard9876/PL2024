from md_to_html_aux import *
from functools import partial

import sys
import re

def identify_tag(s):
    begin = s.split(' ')[0]

    match begin:
        case "###":
            return "header_three"
        case "##":
            return "header_two"
        case "#":
            return "header_one"
        case "#":
            return "header_one"
        case "-":
            return "li"
        case _:
            return "paragraph"    

def process_text(md_line):
    symbols = ["*", "_", "!", "["]

    processed_line = ""

    #TODO Search all substrings using regex, find index of each substring, process substring and keep it in place
    substrings_process = {
        "bold" : [],
        "italic" : [],
        "anchor" : [],
        "image" : []
    }

    print()


    # Bold
    ans = re.findall(r'\*\*[a-zA-Z0-9\_\:\.\ ,;-]*\*\*', md_line)
    substrings_process["bold"] += ans if ans != None else []

    ans = re.findall(r'\_\_[a-zA-Z0-9\_\:\.\ ,;-]*\_\_', md_line)
    substrings_process["bold"] += ans if ans != None else []

    # Italic
    ans = re.findall(r'\*[a-zA-Z0-9\_\:\.\ ,;-]\*', md_line)
    substrings_process["italic"] += ans if ans != None else []
    
    ans = re.findall(r'\_[a-zA-Z0-9\_\:\.\ ,;-]\_', md_line)    
    substrings_process["italic"] += ans if ans != None else []

    # Link
    ans = re.findall(r'\[[a-zA-Z0-9\_\:\.\ ,;-]*\]\([a-zA-Z0-9\_\:\.\ ,;-]*\)', md_line) 
    substrings_process["anchor"] += ans if ans != None else []
    
    # Image
    ans = re.findall(r'!\[[a-zA-Z0-9\_\:\.\ ,;-]*\]\([a-zA-Z0-9\_\:\.\ ,;-]*\)', md_line) 
    substrings_process["image"] += ans if ans != None else []

    print(md_line, substrings_process)

    return md_line    
        
def main(args):
    final_html = ""
    cur_li = ""

    tag_func_dict = {
        "bold" : partial(bold_tag),
        "italic" : partial(italic_tag),
        "header_one" : partial(header_one_tag),
        "header_two" : partial(header_two_tag),
        "header_three" : partial(header_three_tag),
        "anchor" : partial(anchor_tag),
        "image" : partial(image_tag),
        "paragraph" : partial(paragraph_tag),
        "ul" : partial(ul_tag),
        "li" : partial(li_tag)
    }

    for line in sys.stdin:
        line = line.rstrip()

        # Ignore empty lines
        if len(line) == 0:
            continue

        tag = identify_tag(line)

        text = process_text(line)
        processed_text = tag_func_dict[tag](text)

        if tag == "li":
            cur_li += processed_text + "\n"
            continue
        else:
            if cur_li != "":
                processed_text = tag_func_dict["ul"](cur_li)
            else:
                cur_li = ""
        
        final_html += processed_text + "\n"

    if cur_li != "":
        processed_text = tag_func_dict["ul"](cur_li)
        final_html += processed_text + "\n"
    
    print(final_html)

if __name__ == "__main__":
    main(sys.argv)

# 
# print(tag_func_dict["bold"]("**Ola**"))
# print(tag_func_dict["italic"]("*Ola*"))
# print(tag_func_dict["header_one"]("#Ola"))
# print(tag_func_dict["header_two"]("##Ola"))
# print(tag_func_dict["header_three"]("###Ola"))
# print(tag_func_dict["anchor"]("[Ola](link)"))
# print(tag_func_dict["image"]("![Ola](link)"))
