## Credit to Haider Imtiaz
# Wikipedia Searcher
# pip install Wikipedia-API

import wikipediaapi as wiki

# Create a Wikipedia object
wiki = wiki.Wikipedia('en')

# Search for a page
page = wiki.page('Machine Learning')

# Print the page summary
print(page.summary)

# Print the page content
print(page.text)

# Print the page title
print(page.title)

# Print the page URL
print(page.fullurl)

# Print Categories
print(page.categories)

# Print Backlinks
print(page.backlinks)