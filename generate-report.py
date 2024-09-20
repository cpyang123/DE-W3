markdown_text = """
# This is a sample report of the <train.csv> containing Californian house prices


Here's some summary data:

![Summary Data](./fig/summary.png)

Here is a box 'n whisker graph containing all the columns of a the data.

![Box Plot 1](./fig/sample.png)


After some cleaning, it'll look like: 

![Box Plot 2](./fig/sample2.png)

"""


# Open a file to write the markdown content
with open("report.md", "w", encoding="utf-8") as file:
    file.write(markdown_text)

print("Markdown file created!")
