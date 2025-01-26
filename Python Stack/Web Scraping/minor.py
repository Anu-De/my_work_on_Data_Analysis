from bs4 import BeautifulSoup
import requests

url = "http://www.scrapethissite.com/pages/ajax-javascript/#2014"
page = requests.get(url)
print(page)

Soup = BeautifulSoup(page.text, "html")

Soup.find('p', class_ = "lead" ).text.strip()

#Output: 'Click through a bunch of great films. Learn how content is added to the page asynchronously with Javascript and how you can scrape it.\n                            Look for ways that you can tell visually when a site is loading content with AJAX. Then, browse through your network tab to see those AJAX requests and scrape them.'
