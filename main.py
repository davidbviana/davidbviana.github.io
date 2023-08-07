import csv
from jinja2 import Environment, FileSystemLoader
from pathlib import Path


def read_csv(file_path):
    with open(file_path, "r", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data


def generate_html(data):
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("template.html")
    return template.render(data=data)


if __name__ == "__main__":
    data = read_csv("data.csv")
    html_content = generate_html(data)

    (output_path := Path("_site")).mkdir(parents=True, exist_ok=True)
    with open(output_file := str(output_path / "index.html"), "w") as htmlfile:
        htmlfile.write(html_content)

    print(f"{output_file} generated successfully!")
