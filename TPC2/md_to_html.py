from md_to_html_aux import *
from stack import Stack
from functools import partial

import sys
import re

tag_func_dict = {
        "bold" : partial(bold_tag),
        "italic" : partial(italic_tag),
        "bold_italic" : partial(bold_italic_tag),
        "header_one" : partial(header_one_tag),
        "header_two" : partial(header_two_tag),
        "header_three" : partial(header_three_tag),
        "header_four" : partial(header_four_tag),
        "header_five" : partial(header_five_tag),
        "header_six" : partial(header_six_tag),
        "anchor" : partial(anchor_tag),
        "image" : partial(image_tag),
        "paragraph" : partial(paragraph_tag),
        "ul" : partial(ul_tag),
        "ol" : partial(ol_tag),
        "li" : partial(li_tag),
        "horizontal_ruler" : partial(horizontal_ruler_tag),
        "code" : partial(code_tag),
        "blockquote" : partial(blockquote_tag)
    }

def identify_tag(s):
    begin = s.split(' ')[0]

    ans = ""

    match begin:
        case "######":
            ans = "header_six"
        case "#####": 
            ans = "header_five"
        case "####":
            ans = "header_four"
        case "###":
            ans = "header_three"
        case "##":
            ans = "header_two"
        case "#":
            ans = "header_one"
        case "#":
            ans = "header_one"
        case "-":
            ans = "li"
        case _:
            if re.findall(r'^[0-9].*', begin) != []:
                ans = "li"
            elif re.findall(r'^-{3,}$', begin) != []:
                ans = "horizontal_ruler"
            elif re.findall(r'^>.*', begin) != []:
                ans = "blockquote"
            else:
                ans = "paragraph"   

    return ans 

def process_text(md_line:str):
    #TODO Search all substrings using regex, find index of each substring, process substring and keep it in place
    substrings_process = {
        "bold_italic" : [],
        "anchor_image" : [],
        "code" : []
    }

    # Link
    ans = re.findall(r'!?\[.+\]\(.+\)', md_line) 
    substrings_process["anchor_image"] += ans if ans != None else []

    ans = re.findall(r'`.*`', md_line) 
    substrings_process["code"] += ans if ans != None else []

    ans = re.findall(r'`.*`', md_line) 
    substrings_process["code"] += ans if ans != None else []

    s = Stack()

    symbols = ['*', '_']
    i = 0
    cur = ""
    cur_symbol = ""
    length = len(md_line)
    final = False
    code_block = False

    while i < length:
        c = md_line[i]

        prev = md_line[i-1] if i > 0 else ' '
        prev = prev if prev != '`' else ' '

        if c == '`':
            code_block = not(code_block)

        if c in symbols:
            if not(code_block) and (cur == "" or cur == c):
                cur = c
                cur_symbol += c

            else:
                if cur_symbol != "":
                    final = s.final_obj(cur_symbol, i-len(cur_symbol))
                    cur = ""
                    
                if final:
                    start = s.get_start()
                    end = s.get_end()
                    if start == 0 or md_line[start-1] in [' ', '*', '_']:
                        cur_str = md_line[start : (end + len(cur_symbol))]
                        substrings_process["bold_italic"].append(cur_str)
                        final = False
                
                cur_symbol = ""

        else:
            if cur_symbol != "":
                final = s.final_obj(cur_symbol, i-len(cur_symbol))
                cur = ""
                
            if final:
                start = s.get_start()
                end = s.get_end()
                if start == 0 or md_line[start-1] in [' ', '*', '_']:
                    cur_str = md_line[start : (end + len(cur_symbol))]
                    substrings_process["bold_italic"].append(cur_str)
                    final = False
            
            cur_symbol = ""
            
        i += 1

    if cur_symbol != "":
        final = s.final_obj(cur_symbol, i-len(cur_symbol))
        cur = ""
    
    if final:
        start = s.get_start()
        end = s.get_end()

        if start == 0 or md_line[start-1] in [' ', '*', '_']:
            cur_str = md_line[start : (end + len(cur_symbol))]
            substrings_process["bold_italic"].append(cur_str)
            final = False
    
    cur_symbol = ""

    processed_text = md_line

    for p in substrings_process["bold_italic"]:
        tag = True
        idx = 0
        try:
            idx = processed_text.index(p)
        except ValueError:
            tag = False

        if tag:
            length = len(p)

            symbol = ""
            flag = True
            j = 0

            while flag and j < length:
                c = p[j]
                if c != '*' and c != '_':
                    flag = False
                
                if flag:
                    symbol += c
                    j += 1


            p_processed = symbol + process_text(p[len(symbol): - len(symbol)]) + symbol

            function_tag = "italic" if len(symbol) == 1 else "bold" if len(symbol) == 2 else "bold_italic"

            processed_text = processed_text[0:idx] + tag_func_dict[function_tag](p_processed) + processed_text[idx+length:]


    for p in substrings_process["anchor_image"]:
        tag = True
        idx = 0
        try:
            idx = processed_text.index(p)
        except ValueError:
            tag = False
            
        if tag:
            lenght = len(p)

            first_str = re.search(r'\!?\[(.*)\]', p)[1]
            second_str = re.search(r'\((.*)\)', p)[1]

            image = p[0] == '!'

            p_processed = ("!" if image else "") +  '[' + process_text(first_str) + '](' + process_text(second_str) + ')'

            processed_text = processed_text[0:idx] + tag_func_dict["image" if image else "anchor"](p_processed) + processed_text[idx+lenght:]

    for p in substrings_process["code"]:
        tag = True
        idx = 0
        try:
            idx = processed_text.index(p)
        except ValueError:
            tag = False
            
        if tag:
            lenght = len(p)

            processed_text = processed_text[0:idx] + tag_func_dict["code"](re.search(r'`(.*)`', p)[1]) + processed_text[idx+lenght:]

    return processed_text
    

def main(args):
    final_html = ""
    cur_li = ""
    final_list = ""
    blockquote_count = 0

    for line in sys.stdin:
        line = line.rstrip()
        line = line.strip()

        # Ignore empty lines
        if len(line) != 0:
            tag = identify_tag(line)

            while tag == "blockquote":
                blockquote_count += 1

                line = line[1:]

                line = line.rstrip()
                line = line.strip()

                # Ignore empty lines
                if len(line) != 0:
                    tag = identify_tag(line)

            cur_list = "ol" if re.findall(r'^[0-9].*', line) != [] else "ul" if tag == "li" else ""

            if cur_list == "ol":
                line = re.search(r'\d+\.(.*)', line)[1]

            text = process_text(line)
            processed_text = tag_func_dict[tag](text)

            while blockquote_count > 0:
                processed_text = tag_func_dict["blockquote"](processed_text)
                blockquote_count -= 1

            if tag != "li":
                if cur_li != "":
                    final_html += tag_func_dict[final_list](cur_li) + "\n"
                    cur_li = ""
                    final_list = ""
                
                final_html += processed_text + "\n"

            else:
                if final_list == "" or cur_list == final_list:
                    final_list = cur_list
                    cur_li += processed_text + "\n"

                else:
                    if cur_li != "":
                        final_html += tag_func_dict[final_list](cur_li) + "\n"

                    cur_li = processed_text + "\n"
                    final_list = cur_list


    if cur_li != "":
        processed_text = tag_func_dict[final_list](cur_li)
        final_html += processed_text + "\n"
        cur_li = ""
    
    print(final_html)

if __name__ == "__main__":
    main(sys.argv)
