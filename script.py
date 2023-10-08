import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <csv_file_src> Optional: <destination_dir>")
    
    lines = []
    try: 
        with open(sys.argv[1], "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("File not found: " + sys.argv[1])
        sys.exit(1)

    template_html_content = ""
    try:
        with open("template.html", "r") as f:
            template_html_content = f.read()
    except FileNotFoundError:
        print("File not found: template.html")
        sys.exit(1)

    template_html_content = template_html_content.replace("{TITLE}", sys.argv[1].split("/")[-1].split(".")[0])

    headers = lines.pop(0).replace('\n', '').split(",")

    table_headers = "<tr>\n"
    for header in headers:
        table_headers += "<th>" + header + "</th>\n"
    table_headers += "</tr>\n"

    template_html_content = template_html_content.replace("{HEADER}", table_headers)

    table_rows = ""
    for line in lines:
        table_rows += "<tr>\n"
        for cell in line.replace('\n', '').split(","):
            table_rows += "<td>" + cell + "</td>\n"
        table_rows += "</tr>\n"

    template_html_content = template_html_content.replace("{ROWS}", table_rows)

    if len(sys.argv) == 3:
        try:
            with open(sys.argv[2] + "/index.html", "w+") as f:
                f.write(template_html_content)
        except:
            print("Directory not found: " + sys.argv[2])
            sys.exit(1)
    else:
        try:
            with open("index.html", "w+") as f:
                f.write(template_html_content)
        except:
            print("Directory not found: " + sys.argv[2])
            sys.exit(1)


if __name__ == "__main__":
    main()
