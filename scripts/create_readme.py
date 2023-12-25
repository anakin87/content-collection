import csv

markdown_str = """
# My content collection 🎮📚

A simple (and incomplete) collection of content I have created and shared over time.
Mostly about NLP, LLMs, Information Retrieval, and Vector Search.

| Title  | ≈ Date | type |
|---|---|---|
"""

with open("./data/data.csv", "r") as f:
    reader = csv.reader(f, delimiter=",", quotechar='"')
    for i,row in enumerate(reader):
        try:
            title, url, date, type_ = row
        except ValueError as e:
            raise ValueError(f"Error in row {i}: {row}") from e
        markdown_str += f"| {title} | {date} | [{type_}](url) |\n"

with open("./README.md", "w") as fo:
    fo.write(markdown_str)
