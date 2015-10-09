__author__ = 'Herve.Beraud'

A = 0
B = 1
C = 2
WILDCARD = 3
SPACE = " "
BAR = "_"
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

motif = {
    0: [A, A, A, A, A, A],
    1: [A, A, B, A, B, B],
    2: [A, A, B, B, A, B],
    3: [A, A, B, B, B, A],
    4: [A, B, A, A, B, B],
    5: [A, B, B, A, A, B],
    6: [A, B, B, B, A, A],
    7: [A, B, A, B, A, B],
    8: [A, B, A, B, B, A],
    9: [A, B, B, A, B, A],
}


def retrieve_value(current_motif, current_digit):
    return elements[current_motif][int(current_digit)]


def convert_value_to_ascii(values):
    output = ""
    for value in values:
        current = SPACE
        if value == 1:
            current = BAR
        output += current
    return output


def convert_value_to_color(values):
    output = []
    for value in values:
        current = WHITE
        if value == 1:
            current = BLACK
        output.append(current)
    return output


def retrieve_motif(current_code):
    """
    Retrieve motif from a valid user input
    :param current_code:
    :return:
    """
    return motif[int(current_code[0])]


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


def get_user_input():
    """
    Question user for input
    :return:
    """
    while True:
        current_code = input("Your code (max len 13 char): ")
        if check_input_validity(current_code):
            return current_code


def split_current_code(current_code):
    """
    
    :param current_code:
    :return:
    """
    return current_code[1:7], current_code[7:]


def append_side_delimiter():
    return {"value": 0, "mask": WILDCARD}


def append_middle_delimiter():
    return {"value": 1, "mask": WILDCARD}


def assemble_value_representation(first, second, current_motif):
    # Initialize with a start marker
    current_code_formated = [append_side_delimiter()]
    for index, value in enumerate(first):
        current_code_formated.append({"value": int(value), "mask": current_motif[index]})

    # Add center marker
    current_code_formated.append(append_middle_delimiter())
    for index, value in enumerate(second):
        current_code_formated.append({"value": int(value), "mask": C})

    # Append a end marker
    current_code_formated.append(append_side_delimiter())
    return current_code_formated


def construct_barcode(current_code_formated):
    converted_list = []
    for value in current_code_formated:
        converted_list.append(retrieve_value(value["mask"], value["value"]))
    return converted_list


def display_barcode_to_ascii(converted_list):
    print("\nBarcode : ", end="")
    for value in converted_list:
        print(convert_value_to_ascii(value), end="")


def display_selected_configuration(current_motif):
    print("Selected motif: ", end="")
    for value in current_motif:
        current_value = "A"
        if value == B:
            current_value = "B"
        print(current_value, end="")



def unify_value(converted_list):
    unified_values = []
    for value in converted_list:
        unified_values.extend(convert_value_to_color(value))
    return unified_values


def generate_svg(converted_list, current_code):
    unified_value = unify_value(converted_list)
    current_x_position = 1
    svg_output = "\n<svg>\n"
    template_line = '<line x1="{0}" y1="5" x2="{0}" y2="45" stroke-width="2" stroke="{1}" />\n'
    template_text = '<text x="30" y="60" fill="black" font-family="Arial">{1}</text>\n'
    for bar_color in unified_value:
        svg_output += template_line.format(current_x_position, bar_color)
        current_x_position += 2
    text_align = current_x_position / 3
    svg_output += template_text.format(text_align, current_code)
    svg_output += '</svg>'
    return svg_output


def main():
    current_code = get_user_input()
    current_motif = retrieve_motif(current_code)
    display_selected_configuration(current_motif)
    first_part, second_part = split_current_code(current_code)
    current_code_formated = assemble_value_representation(first_part, second_part, current_motif)
    converted_list = construct_barcode(current_code_formated)
    display_barcode_to_ascii(converted_list)
    svg = generate_svg(converted_list, current_code)
    print(svg)

if __name__ == "__main__":
    main()


