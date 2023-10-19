import csv

markdown_str="""
# My content collection 🎮📚

A simple (and incomplete) collection of content I have created and shared over time.

| Title  | ≈ Date |
| ------------- |:-------------:|
"""
        
with open('./data/data.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';', quotechar='"')
    for row in reader:
        title, url, date = row
        markdown_str+= f'| [{title}]({url}) | {date}\n'

with open('./README.md', 'w') as fo:
    fo.write(markdown_str)