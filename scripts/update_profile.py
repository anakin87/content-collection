import csv
import re

markdown_str="<!--content start-->\n"       
with open('content/data/data.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    for row in reader:
        title, url, date, type_ = row
        markdown_str+= f'- [{title} ({type_})]({url})\n'
markdown_str+="<!--content end-->"

with open('profile/README.md', 'r') as fin:
    profile_readme = fin.read()

profile_readme = re.sub(r'<!--content start-->.*<!--content end-->', markdown_str, profile_readme)

print(profile_readme)