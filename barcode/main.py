#! -*-coding:utf8-*-
from __future__ import print_function
import argparse

'''

'''

VERSION = "0.1rc15"
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


def check_input_validity(current_code):
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


def get_user_input(input_value):
    """
    Question user for input
    :return:
    """
    if input_value:
        if check_input_validity(input_value):
            return input_value
    while True:
        try:
            current_code = raw_input("Your code (max len 13 char): ")
        except:
            current_code = input("Your code (max len 13 char): ")
        if check_input_validity(current_code):
            return current_code


def retrieve_motif(current_code):
    """
    Retrieve scheme from a valid user input
    Scheme is determined by the first digit of the user input
    :param current_code:
    :return:
    """
    corresponding = int(current_code[0])
    return scheme[corresponding]


def retrieve_value(current_scheme, current_digit):
    '''
    Retrieve display representation for digit.
    Value corresponding to scheme applying on this digit
    :param current_motif:
    :param current_digit:
    :return:
    '''
    return elements[current_scheme][int(current_digit)]


def convert_value_to_ascii(values):
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


def convert_value_to_color(values):
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


def extract_values_to_encode(current_code):
    '''
    Extract the digits to convert on a displayable representation
    :param current_code:
    :return:
    '''
    return current_code[1:]


def append_side_delimiter():
    '''
    Generate a side delimiter
    :return:
    '''
    return {"value": 0, "mask": WILDCARD}


def append_middle_delimiter():
    '''
    Generate a center delimiter
    :return:
    '''
    return {"value": 1, "mask": WILDCARD}


def assemble_value_representation(extracted_value, current_scheme):
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


def construct_barcode(current_formated_code):
    '''
    Convert digit/scheme information into displayable representation
    :param current_formated_code: associated values and schemes
    :return: List of displayable elements (7 bits per digits)
    '''
    converted_list = []
    for digit in current_formated_code:
        converted_list.append(retrieve_value(digit["mask"], digit["value"]))
    return converted_list


def display_barcode_to_ascii(converted_list):
    '''
    Display barcode on the stdin.
    Diplay on ASCII format
    :param converted_list: list of displayable value
    :return: None
    '''
    print("\nBarcode : ")
    for line in range(0, 5):
        for value in converted_list:
            print(convert_value_to_ascii(value), end="")
        print("\r")


def display_selected_scheme(current_scheme):
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


def unify_value(converted_list):
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


def generate_svg(converted_list, current_code):
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


def generate_html_content(svg):
    '''
    Generate HTML content file
    :param svg: SVG to integrate into html
    :return: HTML formated content file
    '''
    return "<html><body>" + svg + "</body></html>"


def save(svg, filename):
    '''
    Save HTML content in file
    :param svg:
    :param filename:
    :return:
    '''
    with open(filename, "w+") as output:
        output.write(generate_html_content(svg))
    print("\nResult saved into {0}".format(filename))


def main(ascii_output, input_value=None, output=None):
    '''
    Launch barcode.py
    :return:
    '''
    current_code = get_user_input(input_value)
    current_motif = retrieve_motif(current_code)
    display_selected_scheme(current_motif)
    extracted_value = extract_values_to_encode(current_code)
    current_code_formated = assemble_value_representation(extracted_value, current_motif)
    converted_list = construct_barcode(current_code_formated)
    if ascii_output:
        display_barcode_to_ascii(converted_list)
    svg = generate_svg(converted_list, current_code)
    if output:
        save(svg, output)
    else:
        print("\n{0}".format(svg))


def version():
    print("version : {0}".format(VERSION))


def brand():
    print("barcode\nDeveloped By Hervé Beraud")


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', help='User input (digits list, len 13 digits strict)')
    parser.add_argument('-o', help='Output filename. Save SVG output into a file with this filename')
    parser.add_argument('-ascii', help='Display the ASCII value on the standard output', action='store_true')
    parser.add_argument('-version', help='Display version', action='store_true')
    parser.add_argument('-nb', help='Hide software informations (No Brand)', action='store_true')
    parser.set_defaults(ascii=False)
    parser.set_defaults(version=False)
    parser.set_defaults(nb=False)
    args = parser.parse_args()
    if args.version:
        version()
    if not args.nb:
        brand()
    main(args.ascii, args.i, args.o)

if __name__ == "__main__":
    run()
