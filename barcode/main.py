#! -*-coding:utf8-*-
from __future__ import annotations
import argparse

import pyperclip


VERSION = "0.1rc15.0"
A = 0
B = 1
C = 2
WILDCARD = 3
SPACE = " "
BAR = "#"
BLACK = "black"
WHITE = "white"
WIDTH = "5"

elements = {
    A: {
        0: [0, 0, 0, 1, 1, 0, 1],
        1: [0, 0, 1, 1, 0, 0, 1],
        2: [0, 0, 1, 0, 0, 1, 1],
        3: [0, 1, 1, 1, 1, 0, 1],
        4: [0, 1, 0, 0, 0, 1, 1],
        5: [0, 1, 1, 0, 0, 0, 1],
        6: [0, 1, 0, 1, 1, 1, 1],
        7: [0, 1, 1, 1, 0, 1, 1],
        8: [0, 1, 1, 0, 1, 1, 1],
        9: [0, 0, 0, 1, 0, 1, 1],
    },
    B: {
        0: [0, 1, 0, 0, 1, 1, 1],
        1: [0, 1, 1, 0, 0, 1, 1],
        2: [0, 0, 1, 1, 0, 1, 1],
        3: [0, 1, 0, 0, 0, 0, 1],
        4: [0, 0, 1, 1, 1, 0, 1],
        5: [0, 1, 1, 1, 0, 0, 1],
        6: [0, 0, 0, 0, 1, 0, 1],
        7: [0, 0, 1, 0, 0, 0, 1],
        8: [0, 0, 0, 1, 0, 0, 1],
        9: [0, 0, 1, 0, 1, 1, 1],
    },
    C: {
        0: [1, 1, 1, 0, 0, 1, 0],
        1: [1, 1, 0, 0, 1, 1, 0],
        2: [1, 1, 0, 1, 1, 0, 0],
        3: [1, 0, 0, 0, 0, 1, 0],
        4: [1, 0, 1, 1, 1, 0, 0],
        5: [1, 0, 0, 1, 1, 1, 0],
        6: [1, 0, 1, 0, 0, 0, 0],
        7: [1, 0, 0, 0, 1, 0, 0],
        8: [1, 0, 0, 1, 0, 0, 0],
        9: [1, 1, 1, 0, 1, 0, 0],
    },
    WILDCARD: {
        0: [1, 0, 1],
        1: [0, 1, 0, 1, 0],
    }
}

scheme = {
    0: [A, A, A, A, A, A, C, C, C, C, C, C],
    1: [A, A, B, A, B, B, C, C, C, C, C, C],
    2: [A, A, B, B, A, B, C, C, C, C, C, C],
    3: [A, A, B, B, B, A, C, C, C, C, C, C],
    4: [A, B, A, A, B, B, C, C, C, C, C, C],
    5: [A, B, B, A, A, B, C, C, C, C, C, C],
    6: [A, B, B, B, A, A, C, C, C, C, C, C],
    7: [A, B, A, B, A, B, C, C, C, C, C, C],
    8: [A, B, A, B, B, A, C, C, C, C, C, C],
    9: [A, B, B, A, B, A, C, C, C, C, C, C],
}


def check_input_validity(current_code:str) -> bool:
    """
    Check if user input is valid
    :param current_code:
    :return:
    """
    if len(current_code) != 13:
        return False
    try:
        int(current_code)
        return True
    except ValueError:
        return False


def get_user_input(input_value:str) -> str:
    """
    Question user for input
    :return:
    """
    pred = lambda iv: isinstance(iv, type(None)) or not check_input_validity(iv)
    
    while pred(input_value):
        try:
            input_value = input("Your code (max length 13 char from [0, 9]):\n\t")
        except:
            input_value = input("Your code (max length 13 char from [0, 9]):\n\t")
    return input_value
        


def retrieve_motif(current_code:str) -> list[int]:
    """
    Retrieve scheme from a valid user input
    Scheme is determined by the first digit of the user input
    :param current_code:
    :return:
    """
    corresponding = int(current_code[0])
    return scheme[corresponding]


def retrieve_value(current_scheme:int , current_digit:str) -> list[int]:
    '''
    Retrieve display representation for digit.
    Value corresponding to scheme applying on this digit
    :param current_motif:
    :param current_digit:
    :return:
    '''
    return elements[current_scheme][int(current_digit)]


def convert_value_to_ascii(values:list[int]) -> str:
    '''
    Generating ASCII display for one digit
    :param values: the digit to convert
    :return: String
    '''
    output = ""
    for value in values:
        current = SPACE
        if value == 1:
            current = BAR
        output += current
    return output


def extract_values_to_encode(current_code:str) -> str:
    '''
    Extract the digits to convert on a displayable representation
    :param current_code:
    :return:
    '''
    return current_code[1:]


def append_side_delimiter() -> dict[str, int]:
    '''
    Generate a side delimiter
    :return:
    '''
    return {"value": 0, "mask": WILDCARD}


def append_middle_delimiter() -> dict[str, int]:
    '''
    Generate a center delimiter
    :return:
    '''
    return {"value": 1, "mask": WILDCARD}


def assemble_value_representation(extracted_value:str, current_scheme:list[int]) -> list[dict[str, int]]:
    '''
    Associate masks by digits
    :param extracted_value: digits list
    :param current_motif: global current scheme
    :return: list of dictionary
    '''
    # Initialize with a start marker
    current_formated_code = [append_side_delimiter()]
    for index, value in enumerate(extracted_value):
        # Add center marker
        if index == 6:
            current_formated_code.append(append_middle_delimiter())
        current_formated_code.append({"value": int(value), "mask": current_scheme[index]})

    # finish with an end marker
    current_formated_code.append(append_side_delimiter())
    return current_formated_code


def construct_barcode(current_formated_code:list[dict[str, int]]) -> list[list[int]]:
    '''
    Convert digit/scheme information into displayable representation
    :param current_formated_code: associated values and schemes
    :return: List of displayable elements (7 bits per digits)
    '''
    converted_list = []
    for digit in current_formated_code:
        converted_list.append(retrieve_value(digit["mask"], digit["value"]))
    return converted_list


def generate_ascii(converted_list:list[list[int]]) -> str:
    '''
    Compute the ascii string representation of the barcode constructed by construct_barcode
    :param converted_list: 
    :return: string of Hash symbols and Spaces
    '''
    return ''.join(map(str, map(
        convert_value_to_ascii,
        converted_list
    )))


def display_selected_scheme(current_scheme:list[int]):
    '''
    Display the selected scheme.
    Depend of the first digit
    :param current_motif:
    :return:
    '''
    print("Selected motif: ", end="")
    for value in current_scheme:
        current_value = "A"
        if value == B:
            current_value = "B"
        elif value == C:
            current_value = "C"
        print(current_value, end="")


def convert_value_to_color(values:list[list[int]]) -> list[str]:
    '''
    Generating coloring display for one digit
    :param values: the digit to convert
    :return: List of colors
    '''
    output = []
    for value in values:
        current = WHITE
        if value == 1:
            current = BLACK
        output.append(current)
    return output


def unify_value(converted_list:list[list[int]]) -> list[str]:
    '''
    Generate list of color values
    1 digit = 7 colors
    :param converted_list:
    :return:
    '''
    unified_values = []
    for value in converted_list:
        unified_values.extend(convert_value_to_color(value))
    return unified_values


def generate_svg(converted_list:list[list[int]], current_code:str) -> str:
    '''
    Generate SVG output format
    :param converted_list: list
    :param current_code: User input
    :return: SVG code
    '''
    unified_value = unify_value(converted_list)
    current_x_position = 1
    svg_output = "<svg>"
    template_line = '<line x1="{0}" y1="5" x2="{0}" y2="45" stroke-width="2" stroke="{1}" />'
    template_text = '<text x="30" y="60" fill="black" font-family="Arial">{1}</text>'
    for bar_color in unified_value:
        svg_output += template_line.format(current_x_position, bar_color)
        current_x_position += 2
    text_align = current_x_position / 3
    svg_output += template_text.format(text_align, current_code)
    svg_output += '</svg>'
    return svg_output


def generate_html_content(svg:str) -> str:
    '''
    Generate HTML content file
    :param svg: SVG to integrate into html
    :return: HTML formated content file
    '''
    return "<html><body>" + svg + "</body></html>"


def save(filename:str, content:str, extension:str):
    '''
    Save HTML content in file
    :param svg:
    :param filename:
    :return:
    '''
    filename = f"{filename}.{extension}"
    with open(filename, "w+") as outfile:
        outfile.write(content)
    print(f"Result saved into {filename}")


def main(args:argparse.Namespace):
    '''
    Launch barcode.py
    :return:
    '''
    current_code = get_user_input(args.argument)
    current_motif = retrieve_motif(current_code)
    
    if args.motif:
        display_selected_scheme(current_motif)
    
    extracted_value = extract_values_to_encode(current_code)
    current_code_formated = assemble_value_representation(extracted_value, current_motif)
    converted_list = construct_barcode(current_code_formated)
    
    ascii = generate_ascii(converted_list)
    content = ascii
    print()
    [print(f"{ascii}") for i in range(5)]
    
    filename = args.outfile if args.outfile else f"barcode-{args.argument}"
        
    print()
    if args.ascii:
        save(filename, ascii, 'ascii')
    if args.html:
        svg = generate_svg(converted_list, current_code)
        html = generate_html_content(svg)
        content = html
        save(filename, html, 'html')
    if args.svg:
        svg = generate_svg(converted_list, current_code)
        content = svg
        save(filename, svg, 'svg')
    if args.copy:
        pyperclip.copy(content)


def version():
    print("version : {0}".format(VERSION))


def brand():
    print(f"barcode v{VERSION}\n\tDeveloped By Hervé Beraud")


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('argument', help='Your code (max length 13 char from [0, 9])')
    parser.add_argument('-m', '--motif', help='Display motif', action='store_true')
    parser.add_argument('-o', '--outfile', help='Output filename. Save SVG/ASCII/HTML output(s) into a file with this filename. Extensions will be set automatically. Defaults to argument')
    parser.add_argument('-c', '--copy', help='Copy to clipboard', action='store_true')
    parser.add_argument('--ascii', help='Display the ASCII value on the standard output', action='store_true')
    parser.add_argument('--svg', help='Display the svg value on the standard output', action='store_true')
    parser.add_argument('--html', help='Display the svg value on the standard output', action='store_true')
    parser.add_argument('-a', '--author', help='Hide software informations (No Brand)', action='store_true')
    parser.add_argument('-v', '--version', help='Display version', action='store_true')
    parser.set_defaults(m=False)
    parser.set_defaults(c=False)
    parser.set_defaults(ascii=False)
    parser.set_defaults(svg=False)
    parser.set_defaults(html=False)
    parser.set_defaults(version=False)
    parser.set_defaults(author=False)
    
    args = parser.parse_args()
    
    if args.version:
        version()
    if args.author:
        brand()
    
    main(args)

if __name__ == "__main__":
    parse()
