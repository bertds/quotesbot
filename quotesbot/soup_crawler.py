from bs4 import BeautifulSoup
import shadow_useragent
import requests

#shadow user agent
ua = shadow_useragent.ShadowUserAgent()
ua = ua.most_common

# Here, we're just importing both Beautiful Soup and the Requests library
page_link = 'https://www.goudengids.be/bedrijf/Aalst/L1180354/KPM-INVEST/'
# this is the url that we've already determined is safe and legal to scrape from.
headers = {'User-Agent': ua}
print(headers)
page_response = requests.get(page_link, timeout=5, headers=headers)
# here, we fetch the content from the url, using the requests library
page_content = BeautifulSoup(page_response.content, "html.parser")
#we use the html parser to parse the url content and store it in a variable.
print('response : ',page_response.content)
textContent = []
for i in range(0, 2):
    paragraphs = page_content.find_all("p")[i].text
    print(paragraphs)
    textContent.append(paragraphs)
# In my use case, I want to store the speech data I mentioned earlier.  so in this example, I loop through the paragraphs, and push them into an array so that I can manipulate and do fun stuff with the data.


