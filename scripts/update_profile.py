import csv
import re

markdown_str = "<!--content start-->\n"
with open("data/data.csv", "r") as f:
    reader = csv.reader(f, delimiter=",", quotechar='"')
    for i, row in enumerate(reader):
        title, url, date, type_ = row
        markdown_str += f"- [{title} ({type_})]({url})\n"
        if i == 4:
            break
markdown_str += "<!--content end-->"

with open("profile/README.md", "r") as fin:
    profile_readme = fin.read()

profile_readme = re.sub(
    r"<!--content start-->.*<!--content end-->",
    markdown_str,
    profile_readme,
    flags=re.DOTALL,
)

with open("profile/README.md", "w") as fout:
    fout.write(profile_readme)