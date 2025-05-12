from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time 

# # Task 6: Scraping Structured Data

# # Extract a web page section and store the information.

# # Use your browser developer tools to view this page: [https://owasp.org/www-project-top-ten/].  You are going to extract the top 10 security risks reported there.  Figure out how you will find them.

# # Within your python_homework/assignment9 directory, write a script called owasp_top_10.py.  Use selenium to read this page.

# # Find each of the top 10 vulnerabilities.  Hint: You will need XPath.  For each of the top 10 vulnerabilites, keep the vulnerability title and the href link in a dict.  Accumulate these dict objects in a list.

# # Print out the list to make sure you have the right data.  Then, add code to the program to write it to a file called owasp_top_10.csv.  Verify that this file appears correct.

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://owasp.org/www-project-top-ten")

time.sleep(3)

top_ten = driver.find_elements(By.XPATH, '//a[contains(@href, "https://owasp.org/Top10/A")]')

top_ten_list = []
for risk in top_ten:
    try:
        title = risk.text
        link = risk.get_attribute("href")
        top_ten_list.append({"Title": title, "Link": link})
    except:
        continue

print(top_ten_list)

df = pd.DataFrame(top_ten_list)
df.to_csv('../assignment9/owasp_top_10.csv', index=False)

driver.quit()
