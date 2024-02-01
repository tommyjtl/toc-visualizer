import re
import json

from utils import process_headers


def extract_latex_sections(filename):
    # Regular expression to match \section, \subsection, and \subsubsection
    regex = r"\\(sub){0,2}section\{([^\}]+)\}"

    with open(filename, 'r') as file:
        content = file.read()

    matches = re.findall(regex, content)

    # Processing matches to create a list of dictionaries
    sections = []
    for match in matches:
        level = 1 if match[0] == '' else 2 if match[0] == 'sub' else 3
        header = match[1]
        sections.append({
            "level": level,
            "header": header.replace("\\&", "&")
        })

    return sections


def main():
    # Replace with the path to your Markdown file
    input_file = "assets/cs361_note.tex"
    input_name = "CS 361"
    print(input_name)

    sections = extract_latex_sections(input_file)
    # for section in sections:
    #     print(section)

    outline = process_headers(sections, input_name, cutoff_level=3)
    print(json.dumps(outline, indent=2))

    # result = {"name": input_name, "children": outline}
    output_file = input_name + ".json"
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(outline, file, indent=2)


if __name__ == "__main__":
    main()
