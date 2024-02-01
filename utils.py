import math


def is_header(line: str):
    splitted = line.split(' ')
    if len(splitted) < 0:
        return False
    if "#" not in splitted[0]:
        return False
    return True


def extract_header_name(line: str):
    if is_header == False:
        return ""
    splitted = line.split(' ')
    return ' '.join(splitted[1:]).strip()


def get_header_level(line: str):
    if is_header == False:
        return ""
    splitted = line.split(' ')
    level = len(splitted[0])
    return level


def print_tabs(level):
    tabs = ""
    for _ in range(level - 1):
        tabs += "\t"
    return tabs


def check_error_indentation(level, prev_level):
    return int(math.fabs(prev_level - level)) > 1 and level > prev_level


def process_headers(header_list, input_name, cutoff_level=3):

    def add_child(node, child):
        if "children" not in node:
            node["children"] = []
        node["children"].append(child)

    def process(headers, index, level):
        if index >= len(headers) or level > cutoff_level:
            return None, index

        node = {"name": headers[index]["header"]}
        index += 1

        while index < len(headers) and headers[index]["level"] > level:
            if headers[index]["level"] <= cutoff_level:
                child, index = process(headers, index, headers[index]["level"])
                add_child(node, child)
            else:
                index += 1

        return node, index

    root = {"name": input_name, "children": []}

    i = 0
    while i < len(header_list):
        child, i = process(header_list, i, header_list[i]["level"])
        add_child(root, child)

    return root


def extract_headers(md_lines, input_name, cutoff_level):
    prev_level = 1
    level = 1
    all_headers = []

    for line in md_lines:
        if is_header(line):
            header = extract_header_name(line)
            level = get_header_level(line)

            if check_error_indentation(level, prev_level):
                print(prev_level, level)
                print(print_tabs(level), level, header)
                break

            all_headers.append({
                "level": level,
                "header": header
            })
            prev_level = level

    # for header in all_headers:
    #     print(header)

    return process_headers(all_headers, input_name, cutoff_level=cutoff_level)
