from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json
import time 

# Task 3: Write a Program to Extract this Data
# get_books.py. The program should import from selenium and webdriver_manager, as shown in your lesson.  You also need pandas and json.

# Add code to load the web page given in task 2.

# Find all the li elements in that page for the search list results.  You use the class values you stored in task 2 step 3.  Also use the tag name when you do the find, to make sure you get the right elements.

# Within your program, create an empty list called results.  You are going to add dict values to this list, one for each search result.

# Main loop: You iterate through the list of li entries.  For each, you find the entry that contains title of the book, and get the text for that entry.  Then you find the entries that contain the authors of the book, and get the text for each.  If you find more than one author, you want to join the author names with a semicolon ; between each.  Then you find the div that contains the format and the year, and then you find the span entry within it that contains this information.  You get that text too.  You now have three pieces of text.  Create a dict that stores these values, with the keys being Title, Author, and Format-Year.  Then append that dict to your results list.

# Create a DataFrame from this list of dicts.  Print the DataFrame.

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")

time.sleep(3)
results_list= driver.find_elements(By.CSS_SELECTOR,'li.cp-search-result-item')
print(f"Found {len(results_list)} results")
results = []

for item in results_list:
    try:
        title_container = item.find_element(By.CSS_SELECTOR,'h2.cp-title')
        title = title_container.find_element(By.CSS_SELECTOR,'span.title-content').text
    except:
        title = "N/A"
    
    try:
        authors = item.find_elements(By.CSS_SELECTOR,'a.author-link')
        authors_text = "; ".join([a.text for a in authors])
    except:
        authors_text = "N/A"

    try:
        format_year_container = item.find_element(By.CSS_SELECTOR,'div.cp-format-info')
        format_year = format_year_container.find_element(By.TAG_NAME, 'span').text
    except:
        format_year = "N/A"

    results_dict = {
        "Title": title,
        "Author": authors_text,
        "Format-Year": format_year
    }

    results.append(results_dict)


df = pd.DataFrame(results)
print(df)

driver.quit()

# Task 4: Write out the Data

# Write the DataFrame to a file called get_books.csv, within the assignment9 folder.  Examine the file to see if it looks right.

df.to_csv('../assignment9/get_books.csv', index=False)

# Write the results list out to a file called get_books.json, also within the assignment9 folder.  You should write it out in JSON format.  Examine the file to see if it looks right.

with open('../assignment9/get_books.json', 'w') as file:
    json.dump(results, file, indent=4)
