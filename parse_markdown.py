import json
import math

from utils import is_header, extract_header_name, get_header_level, print_tabs, check_error_indentation, process_headers, extract_headers


def main():
    # Replace with the path to your Markdown file
    input_file = "assets/CS 445 Final Exam Review.md"
    # input_name = ' '.join(input_file.split('.')[0:-1])

    input_name = "CS 445"
    print(input_name)

    with open(input_file, "r", encoding="utf-8") as file:
        md_text = file.readlines()

    outline = extract_headers(md_text, input_name, cutoff_level=3)
    # print(json.dumps(outline, indent=2))

    # result = {"name": input_name, "children": outline}
    output_file = input_name + ".json"
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(outline, file, indent=2)


if __name__ == "__main__":
    main()
